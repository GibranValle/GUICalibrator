from customtkinter import CTkFrame, CTkButton, CTkLabel, LEFT  # type: ignore
from classes.constants import BG_COLOR_1, BG_COLOR_0
from typing import Any


class Main:
    def __init__(self, gui_object: Any):
        self.gui = gui_object

    def create_main_frame(self):
        self.frame_main = CTkFrame(self.gui, fg_color=BG_COLOR_1)

        self.serial_frame = CTkFrame(self.gui, fg_color=BG_COLOR_0)
        self.serial_label = CTkLabel(
            self.serial_frame, text="Offline", font=self.gui.font_title, text_color="red"  # type: ignore
        )
        self.serial_label.pack(side=LEFT, padx=10)  # type: ignore
        self.serial_button = CTkButton(
            self.serial_frame,  # type: ignore
            command=self.gui.generic.display_serial_frame,
            font=self.gui.font_text,
            text="Serial config",
        )
        self.serial_button.pack(side=LEFT, pady=5, padx=10)  # type: ignore
        self.serial_frame.pack(padx=10, pady=(5, 0))  # type: ignore

        self.manual_menu = CTkButton(
            self.frame_main,  # type: ignore
            command=self.gui.generic.display_manual_frame,
            font=self.gui.font_text,
            text="Manual Mode",
        )
        self.manual_menu.pack(pady=(10, 5), padx=10)  # type: ignore

        self.auto_menu = CTkButton(
            self.frame_main,  # type: ignore
            command=self.gui.generic.display_auto_frame,
            font=self.gui.font_text,
            text="Auto",
        )
        self.auto_menu.pack(pady=(5, 10), padx=10)  # type: ignore
