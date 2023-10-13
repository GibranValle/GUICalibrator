from typing import Any
from util.CustomExceptions import AbortionRequestError


def noExposureCalibration(name: str, gui_object: Any, duration: int = 600) -> int:
    try:
        total = 0
        gui = gui_object
        print("NO EXPOSURE CALIB")
        gui.generic.clear_output()

        text1 = f"{name} calib starting..."
        text2 = f"Wait for calib signal"
        gui.generic.edit_output(text1, text2)
        total += gui.delay.wait_for_calib_signal(1, duration)

        text1 = f"{name} calib running..."
        text2 = f"Wait for pass signal"
        gui.generic.edit_output(text1, text2)
        total += gui.delay.wait_for_calib_pass(1, duration)
        gui.generic.end_calib_msg(total, 0)
        return total
    except AbortionRequestError:
        raise AbortionRequestError
