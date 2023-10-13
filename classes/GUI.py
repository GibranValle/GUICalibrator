from customtkinter import (  # type: ignore
    set_default_color_theme,
    set_appearance_mode,
    StringVar,
    CTkCheckBox,
    CTkToplevel,
    CTk,
    CTkLabel,
    CTkButton,
    CTkFrame,
    LEFT,
    TOP,
    BOTH,
)
from classes.generic import Generic


from util.delayManager import DelayManager
from util.menu_list import MenuList
from classes.constants import BG_COLOR_1
from classes.frames.manual import Manual
from classes.frames.auto import Auto
from classes.frames.main import Main
from classes.frames.serial import Serial
import util.serialCOM as com

basic_menu = MenuList.basic_menu
calib_opt_menu = MenuList.calib_opt_menu
tomo_menu = MenuList.tomo_menu
full_menu = MenuList.full_menu

# theme settings
set_appearance_mode("dark")
set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class ToplevelWindow(CTkToplevel):
    def __init__(self, *args):  # type: ignore
        super().__init__(*args)  # type: ignore
        self.gui: App = args[0]
        self.all_calibs: list[str] = self.gui.all_calibs  # type: ignore
        self.attributes("-topmost", True)  # type: ignore
        self.geometry("300x500")
        self.label = CTkLabel(
            self, text="Select Calibration to run", font=self.gui.font_title  # type: ignore
        )
        self.label.pack(pady=5)  # type: ignore

        self.frame_buttons = CTkFrame(self, fg_color=BG_COLOR_1)
        self.basic_button = CTkButton(
            self.frame_buttons, text="BASIC", width=75, command=self.basic
        )
        self.basic_button.pack(padx=10, pady=10, side=LEFT)  # type: ignore
        self.tomo_button = CTkButton(
            self.frame_buttons, text="TOMO", width=75, command=self.tomo
        )
        self.tomo_button.pack(padx=10, pady=10, side=LEFT)  # type: ignore
        self.full_button = CTkButton(
            self.frame_buttons, text="FULL", width=75, command=self.full
        )
        self.full_button.pack(padx=10, pady=10, side=LEFT)  # type: ignore
        self.frame_buttons.pack(padx=10, pady=10)  # type: ignore
        self.createCheckbox()

    def createCheckbox(self):
        for option in self.all_calibs:
            name = "var" + option.replace(" ", "_")
            if option in self.gui.selected:
                globals()[name] = StringVar(value="on")
            else:
                globals()[name] = StringVar(value="off")
            self.checkbox = CTkCheckBox(
                self,
                text=option,
                variable=globals()[name],
                onvalue="on",
                offvalue="off",
                command=self.checkbox_event,
            )
            self.checkbox.pack(pady=3, padx=10, side=TOP, fill=BOTH)  # type: ignore

    def basic(self):
        self.gui.selected = basic_menu
        for option in self.all_calibs:
            name = "var" + option.replace(" ", "_")
            if option in self.gui.selected:
                globals()[name].set("on")
            else:
                globals()[name].set("off")

    def tomo(self):
        self.gui.selected = tomo_menu
        for option in self.all_calibs:
            name = "var" + option.replace(" ", "_")
            if option in self.gui.selected:
                globals()[name].set("on")
            else:
                globals()[name].set("off")

    def full(self):
        self.gui.selected = full_menu
        for option in self.all_calibs:
            name = "var" + option.replace(" ", "_")
            if option in self.gui.selected:
                globals()[name].set("on")
            else:
                globals()[name].set("off")

    def checkbox_event(self):
        for option in self.all_calibs:
            name = "var" + option.replace(" ", "_")
            if globals()[name].get() == "on":
                if not option in self.gui.selected:
                    self.gui.selected.append(option)
            elif globals()[name].get() == "off":
                if option in self.gui.selected:
                    self.gui.selected.remove(option)
        print(self.gui.selected)


class App(CTk):
    def __init__(self) -> None:
        super().__init__()  # type: ignore
        self.toplevel_window = None
        self.generic = Generic(self)
        self.delay = DelayManager(self)
        self.font_title: tuple[str, int, str] = (
            "Consolas",
            18,
            "bold",
        )
        self.font_text: tuple[str, int] = ("Consolas", 16)
        self.font_output: tuple[str, int] = ("Consolas", 13)
        self.is_auto_ok: bool = True
        self.isRunning: bool = False
        self.selected: list[str] = []
        self.all_calibs: list[str] = []
        self.all_calibs.extend(basic_menu)
        self.all_calibs.extend(calib_opt_menu)
        # Make the window jump above all
        self.attributes("-topmost", True)  # type: ignore
        self.geometry("300x280")  # type: ignore
        self.title("FPD Calibration bot")  # type: ignore
        self.resizable(False, False)  # type: ignore
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # type: ignore

        # ----------------------------------- COMPONENTS ------------------------------------------------
        self.main = Main(self)
        self.manual = Manual(self)
        self.serial = Serial(self)
        self.auto = Auto(self)

        self.main.create_main_frame()
        self.manual.create_manual_frame()
        self.serial.create_serial_frame()
        self.auto.create_auto_frame()
        self.generic.display_main_frame()

    # ---------------------------------- HANDLE EVENTS -----------------------------------------------------
    def on_closing(self):
        if com.isListening:
            com.endListening()
        self.destroy()

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(
                self
            )  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it
