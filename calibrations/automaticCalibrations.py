from shell.MCU import *
from shell.AWS import enable_FPD_calib
from calibrations.noExposure import noExposureCalibration
from calibrations.smartFPD import smart_FPD_calibration
from typing import Any
from util.PossibleValuesMenu import VALID_CALIBRATION_NAMES
from util.menu_list import MenuList
from util.CustomExceptions import (
    AbnormalBehaviorError,
    IconNotFoundError,
    AbortionRequestError,
)

NO_EXP_MENU = MenuList.no_exp_menu
FULL_MENU = MenuList.full_menu


def autoCalibLoop(gui_object: Any) -> None:
    grand_total = 0
    options: list[VALID_CALIBRATION_NAMES] = gui_object.selected
    gui_object.generic.stabilizing()

    for option in options:
        if gui_object.delay.status == "stop":
            break
        try:
            grand_total += start_mcu_calibration(gui_object, option)
        except AbortionRequestError:
            gui_object.generic.abort_requested()
            return
        except IconNotFoundError:
            gui_object.generic.abnormal()
            gui_object.auto.pushed("stop")
        except AbnormalBehaviorError:
            gui_object.generic.abnormal()
            gui_object.auto.pushed("stop")
            return
    gui_object.generic.end_exp_msg(grand_total, "selection")
    gui_object.auto.pushed("stop")


def start_mcu_calibration(gui_object: Any, calib_name: VALID_CALIBRATION_NAMES):
    try:
        gui_object.generic.edit_output(
            f"{calib_name.capitalize()} calib", "Please wait"
        )
        click_mcu_calib_button(calib_name)
        enable_FPD_calib()
    except IconNotFoundError:
        raise IconNotFoundError
    try:
        if calib_name in NO_EXP_MENU:
            return noExposureCalibration(calib_name, gui_object, duration=600)
        else:
            return smart_FPD_calibration(calib_name, gui_object)
    except AbortionRequestError:
        raise AbortionRequestError
