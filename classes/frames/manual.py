from customtkinter import (  # type: ignore
    CTkFrame,
    CTkButton,
    CTkLabel,
    CTkOptionMenu,
    CTkSwitch,
    StringVar,
)
from util.CustomExceptions import AbortionRequestError
from util.menu_list import MenuList as m
from classes.constants import *
from calibrations.maFullCalib import mAFullCalibration
from threading import Thread
from exposures.man_exp_options import start_smart_exposure, singleShot, TenShots
from typing import Any


class Manual:
    def __init__(self, gui_object: Any):
        self.gui = gui_object

    def only_start(self):
        gui = self.gui
        gui.start_button_man.configure(state="normal")  # type: ignore
        gui.pause_button_man.configure(state="disabled")  # type: ignore
        gui.stop_button_man.configure(state="disabled")  # type: ignore

    def not_only_start(self):
        gui = self.gui
        gui.start_button_man.configure(state="disabled")  # type: ignore
        gui.pause_button_man.configure(state="normal")  # type: ignore
        gui.stop_button_man.configure(state="normal")  # type: ignore

    def only_stop(self):
        gui = self.gui
        gui.start_button_man.configure(state="disabled")  # type: ignore
        gui.pause_button_man.configure(state="disabled")  # type: ignore
        gui.stop_button_man.configure(state="normal")  # type: ignore

    def not_only_pause(self):
        gui = self.gui
        gui.start_button_man.configure(state="normal")  # type: ignore
        gui.pause_button_man.configure(state="disabled")  # type: ignore
        gui.stop_button_man.configure(state="normal")  # type: ignore

    def handleSwitch(self):
        self.gui.is_auto_ok = not self.gui.is_auto_ok

    def pushed(self, button: BUTTONS):
        gui = self.gui

        if button == "pause":
            gui.delay.pauseStatus()
            self.not_only_pause()
            return

        elif button == "stop":
            gui.delay.stopStatus()
            self.only_start()
            raise AbortionRequestError

        elif button == "start":
            option = self.gui.menu_manual.get()  # type: ignore
            if option == "Single Shot":
                self.only_stop()
                if gui.delay.status == "pause":
                    gui.delay.startStatus()
                    return
                Thread(target=singleShot, args=[gui], daemon=True).start()

            elif option == "mA full calib shot":
                self.not_only_start()
                if gui.delay.status == "pause":
                    gui.delay.startStatus()
                    return
                Thread(target=mAFullCalibration, args=[gui], daemon=True).start()

            elif option == "10 shots":
                self.not_only_start()
                if gui.delay.status == "pause":
                    gui.delay.startStatus()
                    return
                Thread(target=TenShots, args=[gui], daemon=True).start()

            elif option == "All needed (FPD)":
                self.not_only_start()
                if gui.delay.status == "pause":
                    gui.delay.startStatus()
                    return
                Thread(target=start_smart_exposure, args=[gui], daemon=True).start()

            else:
                return

            gui.delay.startStatus()

    def create_manual_frame(self):
        gui = self.gui
        gui.frame_manual = CTkFrame(gui, fg_color=BG_COLOR_1)  # type: ignore
        gui.label_manual = CTkLabel(  # type: ignore
            gui.frame_manual, text="Manual Mode", font=gui.font_title  # type: ignore
        )
        gui.label_manual.pack(pady=(5, 0), padx=20)  # type: ignore
        gui.menu_manual = CTkOptionMenu(  # type: ignore
            gui.frame_manual, values=m.manual_menu, font=gui.font_text  # type: ignore
        )
        gui.menu_manual.pack(pady=5, padx=30, fill="x")  # type: ignore
        gui.frame_buttons = CTkFrame(gui.frame_manual, fg_color=BG_COLOR_1)  # type: ignore
        gui.frame_buttons.pack(pady=5, padx=20)  # type: ignore
        gui.start_button_man = CTkButton(  # type: ignore
            gui.frame_buttons,  # type: ignore
            command=lambda: self.pushed("start"),
            font=gui.font_text,
            width=WIDTH_3,
            text=PLAY,
            text_color_disabled=DISABLED_COLOR,
        )
        gui.start_button_man.grid(row=0, column=1)  # type: ignore
        gui.pause_button_man = CTkButton(  # type: ignore
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
        gui.pause_button_man.grid(row=0, column=2, padx=10)  # type: ignore
        gui.stop_button_man = CTkButton(  # type: ignore
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
        gui.stop_button_man.grid(row=0, column=3)  # type: ignore
        gui.label_output1_man = CTkLabel(  # type: ignore
            gui.frame_manual, text="M1:", font=gui.font_output, anchor="w", height=20  # type: ignore
        )
        gui.label_output1_man.pack(padx=30, fill="x")  # type: ignore
        gui.label_output2_man = CTkLabel(  # type: ignore
            gui.frame_manual, text="M2:", font=gui.font_output, anchor="w", height=20  # type: ignore
        )
        gui.label_output2_man.pack(padx=30, fill="x")  # type: ignore
        gui.main_menu = CTkButton(  # type: ignore
            gui.frame_manual,  # type: ignore
            command=gui.generic.back2main,
            font=gui.font_text,
            text="Main menu",
            fg_color=ERR_COLOR,
            hover_color=ERR_COLOR_HOVER,
        )
        gui.main_menu.pack(pady=(5, 0), padx=10)  # type: ignore

        if self.gui.is_auto_ok:
            switch_var = switch_var = StringVar(value="on")
        else:
            switch_var = switch_var = StringVar(value="off")

        gui.switch_auto = CTkSwitch(  # type: ignore
            gui.frame_manual,  # type: ignore
            text="Autoclick ok",
            font=gui.font_text,
            variable=switch_var,
            onvalue="on",
            offvalue="off",
            command=self.handleSwitch,
        )
        gui.switch_auto.pack(pady=5, padx=10)  # type: ignore
