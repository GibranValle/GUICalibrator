from customtkinter import set_default_color_theme, set_appearance_mode, CTk

from classes.frames.manual import *
from classes.frames.auto import *
from classes.frames.main import *
from classes.frames.serial import *
from classes.frames.utils import *
from classes.generic import Generic
from util.delayManager import DelayManager

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
        self.is_auto_ok = False
        # Make the window jump above all
        self.attributes('-topmost', True)
        self.geometry("300x350")
        self.title("FPD Calibration bot")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # ----------------------------------- COMPONENTS ------------------------------------------------
        self.label_serial_main = CTkLabel(self, text='Offline', font=self.font_title, text_color='red')
        self.label_serial_main.pack(pady=(10, 0), padx=20)
        self.manual = Manual(self)
        create_main_frame(self)
        create_serial_frame(self)
        self.manual.create_manual_frame()
        self.auto = Auto(self)
        self.auto.create_auto_frame()
        create_utils_frame(self)
        self.generic.display_main_frame()

    # ---------------------------------- HANDLE EVENTS -----------------------------------------------------
    def on_closing(self):
        if com.isListening:
            com.endListening()
        self.destroy()
