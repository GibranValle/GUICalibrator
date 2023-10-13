from time import sleep
from typing import Any
from util.serialCOM import communicate
from util.delayManager import check_status
from util.CustomExceptions import AbortionRequestError, AbnormalBehaviorError
from classes.constants import (
    CALIB_TYPE,
    PREP_EXP_TIME,
    MAX_EXP_DURATION,
    TIME_BTW_EXP,
    MAX_MA_EXP_DURATION,
)


def smart_exposure_loop(
    gui_object: Any, exposures: int = 100, calib_type: CALIB_TYPE = "auto"
) -> int:
    """
    Generic exposure loop, must be usefully for every shot or calibration process
    Parameters
    ---------
    :param calib_type: 'ma_calib' or 'manual' or 'auto'
    :param gui_object: from GUI class contains delay, generic
    :param exposures: needed only if manual mode (single or ten)
    Return
    ---------
    :return Total time of exposure (manual) or calibration time(auto, mA)
    """
    from classes.GUI import App

    gui: App = gui_object
    gui.generic.clear_output()
    total = 0
    count = 0

    try:
        communicate("T")
        gui.delay.startStatus()

        while True:
            while gui.delay.status == "pause":
                sleep(1)

            if gui.delay.status == "stop":
                raise AbortionRequestError("Abort requested")

            if count >= exposures:
                break

            if calib_type == "ma_calib":
                gui.generic.edit_title("MA FULL CALIBRATION IN COURSE...")
                print("ma calibration")
                total += gui.delay.countdown(init=10)
                communicate("L")
                total += gui.delay.wait_for_exposure_signal(1, MAX_EXP_DURATION)
                total += gui.delay.wait_for_no_exposure_signal(1, MAX_MA_EXP_DURATION)
                gui.generic.end_exp_msg(total, "Exposure")
                gui.manual.pushed("stop")
                return total

            elif calib_type == "manual" or calib_type == "auto":
                communicate("S")
                total += gui.delay.wait_for_stdby_signal(1, PREP_EXP_TIME)
                gui.generic.edit_title(f"Requested exposure {count + 1}")
                total += gui.delay.wait_for_exposure_signal(1, MAX_EXP_DURATION)
                total += gui.delay.wait_for_block_signal(1, TIME_BTW_EXP)

            gui.generic.request_end()
            communicate("X")

            if check_status("isCalibPass"):
                break

            count += 1
            gui.generic.change_exp_count(count)

    except AbnormalBehaviorError:
        gui.generic.abnormal()

    except AbortionRequestError:
        gui.generic.abnormal()

    except ConnectionError:
        print("connection error")
        gui.generic.not_responding()

    else:
        if calib_type == "manual":
            kind = "Exposure"
            if total > 1:
                kind = "Set"
            gui.generic.end_exp_msg(total, kind)
        elif calib_type == "auto":
            gui.generic.end_calib_msg(total, count)

    finally:
        gui.manual.pushed("stop")
        gui.auto.pushed("stop")
        return total
