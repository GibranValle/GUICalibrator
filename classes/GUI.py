import customtkinter
import util.serialCOM as com
from util import menu_list as m

# theme settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    def __init__(self):
        font_title = ("Consolas", 25, 'bold')
        font_text = ("Consolas", 20)
        font_output = ("Consolas", 16)
        self.index = -1
        self.mode_name = ''
        self.subname = ''
        self.lastname = ''

        super().__init__()
        self.geometry("500x400")
        self.minsize(width=500, height=400)
        self.title("FPD Calibration bot")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # create 8x2 grid system
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        # ROW0
        self.label_serial = customtkinter.CTkLabel(master=self, font=font_title, height=50, text_color='red')
        self.label_serial.configure(text='Offline')
        self.label_serial.grid(row=0, column=0, sticky="ew", pady=(10, 0))
        self.button_serial = customtkinter.CTkButton(master=self, command=self.connectButton, font=font_text, height=40, text='Open serial port')
        if com.offline:
            self.button_serial.configure(text='Open port')
        else:
            self.button_serial.configure(text='Close port')
        self.button_serial.grid(row=0, column=1, sticky="ew", padx=(0, 20), pady=(10, 0))

        # MODE MENU
        # ROW 1
        self.label_1 = customtkinter.CTkLabel(master=self, font=font_text, height=50)
        # ROW 2
        self.menu_1 = customtkinter.CTkOptionMenu(master=self, values=m.mode, font=font_text, command=self.mode_changed, height=50)

        # SUB MENU | TEXTBOX
        # ROW 3
        self.label_2 = customtkinter.CTkLabel(master=self, font=font_text, height=50)
        # ROW 4
        self.menu_2 = customtkinter.CTkOptionMenu(master=self, font=font_text, command=self.submenu_changed, height=50)
        # ROW 3 & 4
        self.textBoxOutput = customtkinter.CTkTextbox(master=self, font=font_output, state='normal')

        # LAST MENU
        # ROW 5
        self.label_3 = customtkinter.CTkLabel(master=self, font=font_text, height=50)
        # ROW 6
        self.menu_3 = customtkinter.CTkOptionMenu(master=self, font=font_text, command=self.lastmenu_changed, height=50)

        # BUTTONS
        # ROW 7
        self.button_run = customtkinter.CTkButton(master=self, command=self.Exec, font=font_text, height=60, fg_color='#003366')

    def create_main_menu(self):
        # WORKING
        # ROW 1
        self.label_1.configure(text='Select Mode:')
        self.label_1.grid(row=1, column=0, sticky="ew", padx=(10, 0), pady=(20, 0))
        # ROW 2
        self.menu_1.set('Select: ')
        self.menu_1.grid(row=2, column=0, sticky="ew", pady=(0, 30), padx=(20, 50), columnspan=2)

    def mode_changed(self, name: str):
        self.mode_name = name
        # clear submenu and last menu
        self.button_run.grid_forget()
        self.textBoxOutput.grid_forget()
        self.label_2.grid_forget()
        self.menu_2.grid_forget()
        self.label_3.grid_forget()
        self.menu_3.grid_forget()

        if name in m.with_menu:
            # ADD BUTON
            # ROW 7
            self.button_run.configure(text='Start Exposue')
            self.button_run.grid(row=7, column=0, sticky="ew", padx=(20, 5), pady=(0, 20))

        elif name in m.with_menu_output:
            # ADD BUTON & OUTPUT
            # ROW 7
            self.button_run.configure(text='Create File')
            self.textBoxOutput.grid(row=3, column=0, sticky="ew", padx=(20, 20), pady=(0, 30), columnspan=2, rowspan=2)
            self.button_run.grid(row=7, column=0, sticky="ew", padx=(20, 5), pady=(0, 20))

        elif name in m.with_submenu:
            # ADD SUBMENU
            # ROW 3
            self.label_2.configure(text='Calibration: ')
            self.label_2.grid(row=3, column=0, sticky="ew", padx=(10, 0))
            # ROW 4
            self.menu_2.set('Select: ')
            self.menu_2.grid(row=4, column=0, sticky="ew", pady=(0, 30), padx=(20, 50), columnspan=2)
            # selective values of menu
            if name == 'Basic':
                self.menu_2.configure(values=m.basic)
            elif name == 'Stereo':
                self.menu_2.configure(values=m.stereo)
            elif name == 'Tomo':
                self.menu_2.configure(values=m.tomo)
            elif name == 'ES':
                self.menu_2.configure(values=m.es)

        elif name in m.with_lastmenu:
            # ADD SUBMENU
            # ROW 3
            self.label_2.configure(text='From: ')
            self.label_2.grid(row=3, column=0, sticky="ew", padx=(10, 0))
            # ROW 4
            self.menu_2.set('Select: ')
            self.menu_2.grid(row=4, column=0, sticky="NSEW", pady=(0, 30), padx=(20, 50), columnspan=2)
            self.menu_2.configure(values=m.icons)

    def submenu_changed(self, name: str):
        self.subname = name
        if self.mode_name in m.with_submenu:
            # ADD BUTON
            # ROW 7
            self.button_run.configure(text='Start Calib')
            self.button_run.grid(row=7, column=0, sticky="ew", padx=(20, 5), pady=(0, 20))

        elif self.mode_name in m.with_lastmenu:
            # ADD LAST MENU
            # ROW 5
            self.label_3.configure(text='Icon: ')
            self.label_3.grid(row=5, column=0, sticky="ew", padx=(10, 0))
            # ROW 6
            self.menu_3.set('Select: ')
            self.menu_3.grid(row=6, column=0, sticky="NSEW", pady=(0, 30), padx=(20, 50), columnspan=2)

            if self.mode_name == 'IconFinder':
                if name == 'AWS':
                    self.menu_3.configure(values=m.icons_aws)
                if name == 'RUPCTools':
                    self.menu_3.configure(values=m.icons_RU)
                if name == 'MUTL MU':
                    self.menu_3.configure(values=m.icons_mutl)
                if name == 'Calibration':
                    self.menu_3.configure(values=m.icons_calib)
                if name == 'Calibration Opt':
                    self.menu_3.configure(values=m.icons_calib_opt)

            if self.mode_name == 'Window':
                if name == 'AWS':
                    self.menu_3.configure(values=m.w_aws)
                if name == 'RUPCTools':
                    self.menu_3.configure(values=m.w_RU)
                if name == 'MUTL MU':
                    self.menu_3.configure(values=m.w_mutl)
                if name == 'Calibration':
                    self.menu_3.configure(values=m.w_calib)
                if name == 'Calibration Opt':
                    self.menu_3.configure(values=m.w_calib_opt)

    def lastmenu_changed(self, name: str):
        self.lastname = name
        if self.mode_name == 'IconFinder':
            # ADD BUTON
            # ROW 7
            self.button_run.configure(text='Find object')
            self.button_run.grid(row=7, column=0, sticky="ew", padx=(20, 5), pady=(0, 20))

        elif self.mode_name == 'Window':
            # ADD BUTON
            # ROW 7
            self.button_run.configure(text='Click object')
            self.button_run.grid(row=7, column=0, sticky="ew", padx=(20, 5), pady=(0, 20))

    def on_closing(self):
        com.endListening()
        self.destroy()

    @staticmethod
    def connectButton():
        if com.isListening:
            com.endListening()
            button_serial.configure(text='Open serial port')
            title.configure(text_color='red', text='Offline')

        else:
            serialThread = threading.Thread(target=com.startListening)
            serialThread.start()
            time.sleep(1.5)
            title.configure(text_color='green', text='Online')
            button_serial.configure(text='Close serial port')

    def Exec(self):
        print('RUNNIG')
