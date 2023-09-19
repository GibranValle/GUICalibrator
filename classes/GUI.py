from customtkinter import set_default_color_theme, set_appearance_mode, StringVar, CTkCheckBox, CTkToplevel
import customtkinter as tk

from classes.frames.manual import *
from classes.frames.auto import *
from classes.frames.main import *
from classes.frames.serial import *
from classes.frames.utils import *
from classes.generic import Generic
from util.delayManager import DelayManager
from util.menu_list import basic_menu, calib_opt_menu, tomo_menu, full_menu

# theme settings
set_appearance_mode("dark")
set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class ToplevelWindow(CTkToplevel):
    def __init__(self, *args):
        super().__init__(*args)
        self.gui = args[0]
        self.all_calibs = self.gui.all_calibs
        self.attributes('-topmost', True)
        self.geometry("300x500")
        self.label = CTkLabel(self, text="Select Calibration to run", font=self.gui.font_title)
        self.label.pack(pady=5)

        self.frame_buttons = CTkFrame(self, fg_color=BG_COLOR_1)
        self.basic_button = CTkButton(self.frame_buttons, text='BASIC', width=75, command=self.basic)
        self.basic_button.pack(padx=10, pady=10, side=tk.LEFT)
        self.tomo_button = CTkButton(self.frame_buttons, text='TOMO', width=75, command=self.tomo)
        self.tomo_button.pack(padx=10, pady=10, side=tk.LEFT)
        self.full_button = CTkButton(self.frame_buttons, text='FULL', width=75, command=self.full)
        self.full_button.pack(padx=10, pady=10, side=tk.LEFT)
        self.frame_buttons.pack(padx=10, pady=10)
        self.createCheckbox()

    def createCheckbox(self):
        for option in self.all_calibs:
            name = 'var' + option.replace(' ', '_')
            if option in self.gui.selected:
                globals()[name] = StringVar(value="on")
            else:
                globals()[name] = StringVar(value="off")
            self.checkbox = CTkCheckBox(self, text=option, variable=globals()[name], onvalue='on', offvalue='off',
                                        command=self.checkbox_event)
            self.checkbox.pack(pady=3, padx=10, side=tk.TOP, fill=tk.BOTH)

    def basic(self):
        self.gui.selected = basic_menu
        for option in self.all_calibs:
            name = 'var' + option.replace(' ', '_')
            if option in self.gui.selected:
                globals()[name].set("on")
            else:
                globals()[name].set("off")

    def tomo(self):
        self.gui.selected = tomo_menu
        for option in self.all_calibs:
            name = 'var' + option.replace(' ', '_')
            if option in self.gui.selected:
                globals()[name].set("on")
            else:
                globals()[name].set("off")

    def full(self):
        self.gui.selected = full_menu
        for option in self.all_calibs:
            name = 'var' + option.replace(' ', '_')
            if option in self.gui.selected:
                globals()[name].set("on")
            else:
                globals()[name].set("off")

    def checkbox_event(self):
        for option in self.all_calibs:
            name = 'var' + option.replace(' ', '_')
            if globals()[name].get() == 'on':
                if not option in self.gui.selected:
                    self.gui.selected.append(option)
            elif globals()[name].get() == 'off':
                if option in self.gui.selected:
                    self.gui.selected.remove(option)
        print(self.gui.selected)


class App(CTk):
    def __init__(self):
        super().__init__()
        self.toplevel_window = None
        self.generic = Generic(self)
        self.delay = DelayManager(self)
        self.font_title = ("Consolas", 18, 'bold')
        self.font_text = ("Consolas", 16)
        self.font_output = ("Consolas", 13)
        self.is_auto_ok = True
        self.selected = []
        self.all_calibs = []
        self.all_calibs.extend(basic_menu)
        self.all_calibs.extend(calib_opt_menu)
        # Make the window jump above all
        self.attributes('-topmost', True)
        self.geometry("300x280")
        self.title("FPD Calibration bot")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # ----------------------------------- COMPONENTS ------------------------------------------------
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

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it
