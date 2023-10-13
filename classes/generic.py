from time import sleep
from classes.constants import KIND
from typing import Any

STABILIZING_TIME = 2


def createMessage(msg: str, count: int):
    minutes: int = count // 60
    secs = count % 60
    text = f"{msg}: {secs}s" if minutes <= 0 else f"{msg}: {minutes}m {secs}s"
    return text


class Generic:
    def __init__(self, gui_object: Any):
        self.gui = gui_object

    def clearScreen(self):
        self.gui.serial.frame_serial.pack_forget()  # type: ignore
        self.gui.frame_auto.pack_forget()  # type: ignore
        self.gui.frame_manual.pack_forget()  # type: ignore
        self.gui.main.frame_main.pack_forget()  # type: ignore

    def updateGui(self, gui_object: Any):
        self.gui = gui_object

    def back2main(self):
        self.clearScreen()
        self.gui.main.frame_main.pack(pady=20, padx=20, fill="x")  # type: ignore

    def open_serial_config(self):
        self.clearScreen()
        self.gui.serial.frame_serial.pack(pady=20, padx=20, fill="x")  # type: ignore

    def display_main_frame(self):
        self.clearScreen()
        self.gui.main.frame_main.pack(pady=(3, 20), padx=20, fill="x")  # type: ignore

    def display_serial_frame(self):
        self.clearScreen()
        self.gui.serial.frame_serial.pack(pady=(5, 15), padx=20, fill="x")  # type: ignore

    def display_manual_frame(self):
        self.clearScreen()
        self.gui.frame_manual.pack(pady=(5, 15), padx=20, fill="x")  # type: ignore

    def display_auto_frame(self):
        self.clearScreen()
        self.gui.frame_auto.pack(pady=(5, 15), padx=20, fill="x")  # type: ignore

    def edit_output(self, msg1: str = "", msg2: str = ""):
        if msg1 != "":
            self.gui.label_output1_man.configure(text=msg1)  # type: ignore
            self.gui.label_output1_auto.configure(text=msg1)  # type: ignore

        if msg2 != "":
            self.gui.label_output2_man.configure(text=msg2)  # type: ignore
            self.gui.label_output2_auto.configure(text=msg2)  # type: ignore

    def edit_title(self, msg: str = ""):
        if msg != "":
            self.gui.label_output1_man.configure(text=msg)  # type: ignore
            self.gui.label_output1_auto.configure(text=msg)  # type: ignore

    def edit_subtitle(self, msg: str = ""):
        if msg != "":
            self.gui.label_output2_man.configure(text=msg)  # type: ignore
            self.gui.label_output2_auto.configure(text=msg)  # type: ignore

    def clear_output(self):
        self.edit_output(" ", " ")

    def not_responding(self):
        self.edit_output("BOT NOT RESPONDING!", "Please verify")
        self.gui.isRunning = False

    def abort_requested(self):
        text1 = "Exposure aborted"
        text2 = "----------------"
        self.edit_output(text1, text2)
        self.gui.isRunning = False

    def aborted(self):
        text1 = "Premature end of exposure"
        text2 = "Please verify system"
        self.edit_output(text1, text2)
        self.gui.isRunning = False

    def stabilizing(self):
        text1 = f"Stabilizing..."
        text2 = f"Please wait..."
        self.edit_output(text1, text2)
        sleep(STABILIZING_TIME)

    def abnormal(self):
        text1 = "App abnormal behavior"
        text2 = "Please verify system"
        self.edit_output(text1, text2)
        self.gui.isRunning = False

    def under_exposure(self):
        text1 = "UNDER EXPOSURE..."
        text2 = "----------------"
        self.edit_output(text1, text2)

    def request_end(self):
        print("requesting end of exposure")
        text1 = "Requesting End of exposure"
        self.edit_output(text1)

    def end_manually(self):
        text1 = " "
        text2 = "Please end exposure manually"
        self.edit_output(text1, text2)

    def accepted(self, kind: KIND = "Short"):
        text1 = f"Accepted {kind} exposure"
        self.edit_output(text1)

    def end_exp_msg(self, total: int, kind: KIND = "Exposure"):
        text1 = "Exposure done"
        text2 = createMessage(f"This {kind} took", total)
        self.edit_output(text1, text2)

    def end_calib_msg(self, total: int, exposures: int):
        text1 = "Calibration passed!"
        text2 = createMessage("Time", total)
        self.edit_output(text1, text2 + f" exposures: {exposures}")

    def change_exp_count(self, exposures: int):
        text1 = f"Exposures count: {exposures}"
        self.edit_output(text1)
