from customtkinter import CTkFrame, CTkButton, CTkLabel, CTkOptionMenu, CTkTextbox  # type: ignore
from util.menu_list import MenuList as m
from classes.constants import *
from classes.generic import *
from classes.GUI import App


class Utils:
    def __init__(self, gui_object: App):
        self.gui = gui_object

    def pushed(self):
        print(self.menu_utils.get())

    def create_utils_frame(self):
        self.frame_utils = CTkFrame(self, fg_color=BG_COLOR_1)
        self.label_utils = CTkLabel(
            self.frame_utils, text="Utils Menu", font=self.gui.font_title
        )
        self.label_utils.pack(pady=10, padx=20)  # type: ignore

        self.menu_utils = CTkOptionMenu(
            self.frame_utils, values=m.utils_menu, font=self.gui.font_text
        )
        self.menu_utils.pack(pady=5, padx=30, fill="x")  # type: ignore

        self.run_button = CTkButton(
            self.frame_utils,
            command=lambda: self.pushed(),
            font=self.gui.font_text,
            text="Run",
            text_color_disabled=DISABLED_COLOR,
        )
        self.run_button.pack(pady=5, padx=30, fill="x")  # type: ignore

        self.textBoxOutput = CTkTextbox(
            self.frame_utils, font=self.gui.font_output, state="normal", height=100
        )
        self.textBoxOutput.pack(pady=5, padx=30, fill="x")  # type: ignore

        self.main_menu = CTkButton(
            self.frame_utils,
            command=lambda: self.gui.generic.back2main(),
            font=self.gui.font_text,
            text="Main menu",
            fg_color=ERR_COLOR,
            hover_color=ERR_COLOR_HOVER,
        )
        self.main_menu.pack(pady=10, padx=10)  # type: ignore
