from exposures.man_exp_options import start_smart_exposure
from typing import Any
from util.CustomExceptions import IconNotFoundError


def smart_FPD_calibration(name: str, gui_object: Any, duration: int = 600) -> int:
    gui = gui_object
    total = 0
    gui.generic.edit_title(f"{name} calib starting...")

    try:
        total += gui.delay.wait_for_calib_signal(1, duration)
        total += start_smart_exposure(gui_object)
    except IconNotFoundError:
        return gui.generic.abnormal()
    return total
