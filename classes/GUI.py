import customtkinter

import util.serialCOM as com
from shell.network.network import *
from shell.generic import *
from util import menu_list as m
from threading import Thread
from calibrations.maFullCalib import mAFullCalibration
from calibrations.exposureCalibration import *
from util.delayManager import setStopFlag
from classes.window import windowOptions

# theme settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

HEIGHT_1 = 50
HEIGHT_2 = 40
HEIGHT_3 = 30
WIDTH_1 = 240
WIDTH_2 = 180

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.font_title = ("Consolas", 18, 'bold')
        self.font_text = ("Consolas", 16)
        self.font_output = ("Consolas", 13)
        self.isRunning = False
        self.index = -1
        self.mode = ''
        self.submode = ''
        self.option = ''
        # Make the window jump above all
        self.attributes('-topmost', True)

        self.geometry("300x400")
        self.title("FPD Calibration bot")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # ------------------------------------------------------------ COMPONENTS ------------------------------------------------------------------------

        # serial
        self.frame1 = customtkinter.CTkFrame(master=self, height=HEIGHT_1, fg_color="#353535")
        self.frame1.pack(pady=10, padx=10, fill='both')
        self.label_serial = customtkinter.CTkLabel(master=self.frame1, font=self.font_title, text_color='red',
                                                   text='Offline')
        self.label_serial.place(relx=0.05, rely=0.25)
        self.button_serial = customtkinter.CTkButton(master=self.frame1, command=self.connectButton,
                                                     font=self.font_text, text='Open serial port', height=HEIGHT_3)
        self.button_serial.place(relx=0.40, rely=0.175)

        # MAIN MENU
        # ROW 1
        self.label_1 = customtkinter.CTkLabel(master=self, font=self.font_text)
        self.label_1.configure(text='Select Mode:')
        self.label_1.place(relx=0.1, rely=0.18)
        # ROW 2
        self.menu_1 = customtkinter.CTkOptionMenu(master=self, values=m.mode, font=self.font_text,
                                                  command=self.mode_changed, width=WIDTH_2, height=HEIGHT_3)
        self.menu_1.set('Select: ')
        self.menu_1.place(relx=0.1, rely=0.25)

        self.label_2 = customtkinter.CTkLabel(master=self, font=self.font_text)
        self.menu_2 = customtkinter.CTkOptionMenu(master=self, font=self.font_text, command=self.submenu_changed,
                                                  width=WIDTH_2, height=HEIGHT_3)

        self.textBoxOutput = customtkinter.CTkTextbox(master=self, font=self.font_output, state='normal', width=WIDTH_1,
                                                      height=120)

        self.label_3 = customtkinter.CTkLabel(master=self, font=self.font_text)
        self.menu_3 = customtkinter.CTkOptionMenu(master=self, font=self.font_text, command=self.lastmenu_changed,
                                                  width=WIDTH_2, height=HEIGHT_3)

        self.button_run = customtkinter.CTkButton(master=self, command=self.Exec, font=self.font_text,
                                                  fg_color='#003366', hover_color='#002255', height=HEIGHT_2, width=WIDTH_2)

        self.label_output1 = customtkinter.CTkLabel(master=self, font=self.font_text)
        self.label_output2 = customtkinter.CTkLabel(master=self, font=self.font_text)

    def edit_serial(self):
        if com.offline:
            self.label_serial.configure(text='Offline')
            self.button_serial.configure(text='Open port')
            return
        self.button_serial.configure(text='Close port')
        self.label_serial.configure(text='Online')

    def edit_submenu(self, submenu='Basic'):
        # ROW 3
        self.label_2.place(relx=0.1, rely=0.38)
        # ROW 4
        self.menu_2.set('Select: ')
        self.menu_2.place(relx=0.1, rely=0.45)

        if submenu in m.with_submenu:
            self.label_2.configure(text='Calibration: ')

        elif submenu in m.with_submenu_lastmenu:
            self.label_2.configure(text='From: ')

        if submenu == 'Basic':
            self.menu_2.configure(values=m.basic)
        elif submenu == 'Stereo':
            self.menu_2.configure(values=m.stereo)
        elif submenu == 'Tomo':
            self.menu_2.configure(values=m.tomo)
        elif submenu == 'ES':
            self.menu_2.configure(values=m.es)
        elif submenu == 'IconFinder':
            self.menu_2.configure(values=m.iconFinder)
        elif submenu == 'Window':
            self.menu_2.configure(values=m.window)

    def edit_output(self):
        # ROW 3 & 4
        self.textBoxOutput.place(relx=0.1, rely=0.35)

    def edit_last_menu(self, menu):
        # ROW 5
        self.label_3.configure(text='Icon: ')
        self.label_3.place(relx=0.1, rely=0.58)
        label2 = self.label_3
        # ROW 6
        self.menu_3.set('Select: ')
        self.menu_3.configure(values=menu)
        self.menu_3.place(relx=0.1, rely=0.65)

    def edit_button(self, text, error=False):
        # ROW 7
        if not error:
            self.button_run.configure(text=text, fg_color='#003366', hover_color='#002255')
        else:
            self.button_run.configure(text=text, fg_color='#880015', hover_color='#6E0011')
        self.button_run.place(relx=0.20, rely=0.8)

    # ---------------------- CLEAR----------------
    def clearAll(self):
        self.clearLastmenu()
        self.clearSubmenu()

    def clearSubmenu(self):
        self.label_2.place_forget()
        self.menu_2.place_forget()
        self.textBoxOutput.place_forget()
        self.label_output1.place_forget()
        self.label_output2.place_forget()

    def clearLastmenu(self):
        self.button_run.place_forget()
        self.label_3.place_forget()
        self.menu_3.place_forget()
        self.label_output1.configure(text='')
        self.label_output2.configure(text='')

    # --------------------------------------------------------- HANDLE EVENTS ----------------------------------------------------------------------
    def mode_changed(self, name: str):
        self.mode = name
        self.clearAll()

        if name in m.only_menu:
            self.edit_button(text='Start exposure')
            self.label_output1.configure(text='')
            self.label_output1.place(relx=0.1, rely=0.55)
            self.label_output2.configure(text='')
            self.label_output2.place(relx=0.1, rely=0.60)

        elif name in m.with_output:
            self.edit_output()
            self.edit_button('Create file')

        elif name in m.with_submenu:
            self.edit_submenu(name)
            self.label_output1.configure(text='')
            self.label_output1.place(relx=0.1, rely=0.58)
            self.label_output2.configure(text='')
            self.label_output2.place(relx=0.1, rely=0.65)

        elif name in m.with_submenu_lastmenu:
            self.edit_submenu(name)

    def submenu_changed(self, name: str):
        print('submenu changed')
        self.submode = name
        self.clearLastmenu()

        if self.mode == 'Window':
            if name == 'AWS':
                self.edit_last_menu(menu=m.w_aws)
            elif name == 'RUPCTools':
                self.edit_last_menu(menu=m.w_ru)
            elif name == 'MUTL MU':
                self.edit_last_menu(menu=m.w_mutl)
            elif name == 'MUTL MCU':
                self.edit_last_menu(menu=m.w_mutl_mcu)

        elif name in m.window:
            self.edit_last_menu()

        elif self.mode in m.with_submenu:
            self.edit_button('Start calibration')

    def lastmenu_changed(self, name: str):
        print('last menu changed')
        self.option = name
        if self.mode == 'IconFinder':
            self.edit_button('Find icon')
        elif self.mode == 'Window':
            self.edit_button('Execute')

    def on_closing(self):
        com.endListening()
        self.destroy()

    def connectButton(self):
        if com.isListening:
            com.endListening()
            self.button_serial.configure(text='Open serial port')
            self.label_serial.configure(text_color='red', text='Offline')
            return

        serialThread = Thread(target=com.startListening)
        serialThread.start()
        time.sleep(1.5)
        if com.isListening:
            self.label_serial.configure(text_color='green', text='Online')
            self.button_serial.configure(text='Close serial port')

    def Exec(self):
        print('BUTTON')
        if self.isRunning:
            setStopFlag()
            self.isRunning = False
            self.edit_button('Start Exposure')
            return

        if self.mode == 'mA Full':
            self.isRunning = True
            self.edit_button('Stop Exposure', error=True)
            Thread(target=mAFullCalibration, args=[self], daemon=True).start()

        elif self.mode == 'Single shot':
            self.isRunning = True
            self.edit_button('Stop Exposure', error=True)
            Thread(target=singleShot, args=[self], daemon=True).start()

        elif self.mode == '10 Shots':
            self.isRunning = True
            self.edit_button('Stop Exposure', error=True)
            Thread(target=TenShots, args=[self], daemon=True).start()

        elif self.mode == 'Save MAC':
            macs = saveMACs()
            self.textBoxOutput.insert(index=0.0, text=macs)

        elif self.mode == 'Create WOL file':
            createWOLsetupFile('Ethernet')
            try:
                copyFile('setup.ini', '"C:\\Program Files (x86)\\Fujifilm\\WOL\\"')
                text = 'File saved successfully'
            except subprocess.CalledProcessError:
                text = 'Access denied!\nPlease copy file manually to:\n\nC:/Program Files (x86)/Fujifilm/WOL'
            self.textBoxOutput.insert(index=0.0, text=text)

        elif self.mode == 'Basic':

            if self.submode == 'Defect-solid':
                self.isRunning = True
                self.edit_button('Stop Exposure', error=True)
                Thread(target=defectSolidCalib, args=[self], daemon=True).start()

            elif self.submode == 'Pixel-defect':
                self.isRunning = True
                self.edit_button('Stop Exposure', error=True)
                Thread(target=pixedDefectCalib, args=[self], daemon=True).start()

            elif self.submode == 'Shading':
                self.isRunning = True
                self.edit_button('Stop Exposure', error=True)
                Thread(target=shadingCalib, args=[self], daemon=True).start()

            elif self.submode == 'X-ray uniformity':
                self.isRunning = True
                self.edit_button('Stop Exposure', error=True)
                Thread(target=uniformityCalib, args=[self], daemon=True).start()

        elif self.mode == 'Stereo':
            pass

        elif self.mode == 'Tomo':
            pass

        elif self.mode == 'ES':
            pass

        elif self.mode == 'Window':
            windowOptions(self.option)

    def editLabel1(self, text=''):
        self.label_2.configure(text=text)

    def editLabel2(self, text=''):
        self.label_3.configure(text=text)
