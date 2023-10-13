from customtkinter import CTkFrame, CTkButton, CTkLabel  # type: ignore
from classes.constants import *
from shell.MCU import *
from threading import Thread
from calibrations.automaticCalibrations import autoCalibLoop
from typing import Any
from util.CustomExceptions import AbortionRequestError


class Auto:
    def __init__(self, gui_object: Any):
        self.gui = gui_object

    def only_start(self):
        gui = self.gui
        gui.start_button_auto.configure(state="normal")  # type: ignore
        gui.pause_button_auto.configure(state="disabled")  # type: ignore
        gui.stop_button_auto.configure(state="disabled")  # type: ignore

    def not_only_start(self):
        gui = self.gui
        gui.start_button_auto.configure(state="disabled")  # type: ignore
        gui.pause_button_auto.configure(state="normal")  # type: ignore
        gui.stop_button_auto.configure(state="normal")  # type: ignore

    def only_stop(self):
        gui = self.gui
        gui.start_button_auto.configure(state="disabled")  # type: ignore
        gui.pause_button_auto.configure(state="disabled")  # type: ignore
        gui.stop_button_auto.configure(state="normal")  # type: ignore

    def not_only_pause(self):
        gui = self.gui
        gui.start_button_auto.configure(state="normal")  # type: ignore
        gui.pause_button_auto.configure(state="disabled")  # type: ignore
        gui.stop_button_auto.configure(state="normal")  # type: ignore

    def pushed(self, button: BUTTONS):
        gui = self.gui
        self.status = button

        if button == "pause":
            gui.delay.pauseStatus()  # type: ignore
            self.not_only_pause()
            return

        elif button == "stop":
            gui.delay.stopStatus()
            self.only_start()
            raise AbortionRequestError

        elif button == "start":
            size = len(gui.selected)
            if size > 0:
                gui.delay.startStatus()
                self.not_only_start()
                Thread(target=autoCalibLoop, args=[self.gui], daemon=True).start()
            else:
                gui.generic.edit_output("No calib selected!", "Please select options")

    def create_auto_frame(self):
        gui = self.gui
        gui.toplevel_window = None
        gui.frame_auto = CTkFrame(gui, fg_color=BG_COLOR_1)  # type: ignore
        gui.label_auto = CTkLabel(gui.frame_auto, text="Auto Mode", font=gui.font_title)  # type: ignore
        gui.label_auto.pack(pady=(5, 0), padx=20)  # type: ignore

        gui.selection = CTkButton(  # type: ignore
            gui.frame_auto,  # type: ignore
            command=self.gui.open_toplevel,
            font=gui.font_text,
            text="Select calibs",
            text_color_disabled=DISABLED_COLOR,
        )
        gui.selection.pack(pady=5, padx=20, fill="x")  # type: ignore

        gui.frame_buttons = CTkFrame(gui.frame_auto, fg_color=BG_COLOR_1)  # type: ignore
        gui.frame_buttons.pack(pady=5, padx=20, fill="x")  # type: ignore

        gui.start_button_auto = CTkButton(  # type: ignore
            gui.frame_buttons,  # type: ignore
            command=lambda: self.pushed("start"),
            font=gui.font_text,
            width=WIDTH_3,
            text=PLAY,
            text_color_disabled=DISABLED_COLOR,
        )
        gui.start_button_auto.grid(row=0, column=1)  # type: ignore

        gui.pause_button_auto = CTkButton(  # type: ignore
            gui.frame_buttons,  # type: ignore
            command=lambda: self.pushed("pause"),
            font=gui.font_text,
            width=WIDTH_3,
            text=PAUSE,
            state="disabled",
            text_color_disabled=DISABLED_COLOR,
            fg_color=OK_COLOR,
            hover_color=OK_COLOR_HOVER,
        )
        gui.pause_button_auto.grid(row=0, column=2, padx=20)  # type: ignore

        gui.stop_button_auto = CTkButton(  # type: ignore
            gui.frame_buttons,  # type: ignore
            command=lambda: self.pushed("stop"),
            font=gui.font_text,
            width=WIDTH_3,
            text=STOP,
            state="disabled",
            text_color_disabled=DISABLED_COLOR,
            fg_color=ERR_COLOR,
            hover_color=ERR_COLOR_HOVER,
        )
        gui.stop_button_auto.grid(row=0, column=3)  # type: ignore

        gui.label_output1_auto = CTkLabel(  # type: ignore
            gui.frame_auto, text="M1:", font=gui.font_output, anchor="w", height=20  # type: ignore
        )
        gui.label_output1_auto.pack(padx=20, fill="x")  # type: ignore

        gui.label_output2_auto = CTkLabel(  # type: ignore
            gui.frame_auto, text="M2:", font=gui.font_output, anchor="w", height=20  # type: ignore
        )
        gui.label_output2_auto.pack(padx=20, fill="x")  # type: ignore

        gui.main_menu = CTkButton(  # type: ignore
            gui.frame_auto,  # type: ignore
            command=gui.generic.back2main,
            font=gui.font_text,
            text="Main menu",
            fg_color=ERR_COLOR,
            hover_color=ERR_COLOR_HOVER,
        )
        gui.main_menu.pack(pady=(5, 10), padx=10)  # type: ignore
