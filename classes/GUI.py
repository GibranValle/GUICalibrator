from customtkinter import set_default_color_theme, set_appearance_mode, CTk

import util.serialCOM as com
from shell.network.network import *
from shell.generic import *
from threading import Thread
from calibrations.maFullCalib import mAFullCalibration
from calibrations.exposureCalibration import *
from classes.frames.manual import *
from classes.frames.auto import *
from classes.frames.main import *
from classes.frames.serial import *
from classes.frames.utils import *
from classes.generic import Generic
from util.delayManager import DelayManager
from classes.window import windowOptions

# theme settings
set_appearance_mode("dark")
set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(CTk):
    def __init__(self):
        super().__init__()
        self.generic = Generic(self)
        self.delay = DelayManager(self)
        self.font_title = ("Consolas", 18, 'bold')
        self.font_text = ("Consolas", 16)
        self.font_output = ("Consolas", 13)
        self.status = 'stop'
        self.index = -1
        self.mode = ''
        self.submode = ''
        self.option = ''
        # Make the window jump above all
        self.attributes('-topmost', True)

        self.geometry("300x350")
        self.title("FPD Calibration bot")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # ------------------------------------------------------------ COMPONENTS ------------------------------------------------------------------------
        self.label_serial_main = CTkLabel(self, text='Offline', font=self.font_title, text_color='red')
        self.label_serial_main.pack(pady=(10, 0), padx=20)
        self.manual = Manual(self)
        create_main_frame(self)
        create_serial_frame(self)
        self.manual.create_manual_frame()
        create_auto_frame(self)
        create_utils_frame(self)
        self.generic.display_main_frame()


    # --------------------------------------------------------- HANDLE EVENTS ----------------------------------------------------------------------
    def on_closing(self):
        if com.isListening:
            com.endListening()
        self.destroy()



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
            try:
                createWOLsetupFile('Ethernet')
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
