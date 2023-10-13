from customtkinter import CTkFrame, CTkButton  # type: ignore
from classes.constants import *
import util.serialCOM as com
from threading import Thread
from time import sleep
from typing import Any


class Serial:
    def __init__(self, gui_object: Any):
        self.gui = gui_object

    def create_serial_frame(self):
        self.frame_serial = CTkFrame(self.gui, fg_color=BG_COLOR_1)

        self.button_serial = CTkButton(
            self.frame_serial,
            command=lambda: self.toggle_serial(),
            font=self.gui.font_text,
            text="Connect",
        )
        self.button_serial.pack(pady=20, padx=10)  # type: ignore

        self.main_menu = CTkButton(
            self.frame_serial,
            command=self.gui.generic.back2main,
            font=self.gui.font_text,
            text="Main menu",
            fg_color=ERR_COLOR,
            hover_color=ERR_COLOR_HOVER,
        )
        self.main_menu.pack(pady=(0, 20), padx=10)  # type: ignore

    def toggle_serial(self):
        if com.isListening:
            com.endListening()
            self.button_serial.configure(text="Open serial port")  # type: ignore
            self.serial_label.configure(text_color="red", text="Offline")  # type: ignore
            return

        serialThread = Thread(target=com.startListening)
        serialThread.start()
        sleep(1.5)
        if com.isListening:
            self.serial_label.configure(text_color="green", text="Online")  # type: ignore
            self.button_serial.configure(text="Close serial port")  # type: ignore
