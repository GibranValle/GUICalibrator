from time import sleep
from util.serialCOM import communicate
from util.delayManager import isCalibPass
from shell.AWS import clickOK
from classes.constants import PREP_EXP_TIME, MAX_EXP_DURATION, TIME_BTW_EXP, MAX_MA_EXP_DURATION

CALIB_TYPE = 'ma_calib' or 'manual' or 'auto'


def smart_exposure_loop(gui_object, exposures=100, calib_type: CALIB_TYPE = 'auto'):
    f"""" Generic exposure loop, must be usefully for every shot or calibration process
    Parameters
    ---------
    :param calib_type: 'ma_calib' or 'manual' or 'auto'
    :param gui_object: from GUI class contains delay, generic
    :param exposures: needed only if manual mode (single or ten)
    Return
    ---------
    :return Total time of exposure (manual) or calibration time(auto, mA)
    """

    # AUTO
    countdown = 0
    skip_pass = False

    if calib_type == 'ma_calib':
        exposures = 1
        countdown = 10
        skip_pass = True

    elif calib_type == 'manual':
        skip_pass = True
        countdown = 0

    gui = gui_object
    gui.delay.startStatus()
    total = 0
    count = 0

    communicate("T")
    gui.generic.clear_output()
    total += gui.delay.countdown(countdown)

    try:
        while True:
            if countdown > 0:
                communicate("L")
            else:
                communicate("S")

            while gui.delay.status == 'pause':
                sleep(1)

            if gui.delay.status == 'stop':
                return gui.generic.abort_requested()

            if isCalibPass() and not skip_pass:
                break

            if gui.is_auto_ok:
                clickOK()

            if count >= exposures:
                break

            if countdown <= 0:
                total += gui.delay.wait_for_stdby_signal(1, PREP_EXP_TIME)

            gui.generic.edit_title(f'Requested exposure {count + 1}')
            total += gui.delay.wait_for_exposure_signal(1, MAX_EXP_DURATION)

            if countdown <= 0:
                total += gui.delay.wait_for_block_signal(1, TIME_BTW_EXP)

            elif countdown > 0:
                total += gui.delay.wait_for_no_exposure_signal(1, MAX_MA_EXP_DURATION)

            gui.generic.request_end()
            communicate("X")

            if isCalibPass() and not skip_pass:
                break

            count += 1
            gui.generic.change_exp_count(count)

    except ValueError:
        return gui.generic.abnormal()
    except ConnectionError:
        return gui.generic.not_responding()

    if calib_type == 'ma_calib':
        gui.generic.end_exp_msg(total, 'Exposure')
        gui.manual.pushed('stop')

    elif calib_type == 'manual':
        gui.generic.end_exp_msg(total, 'Set')
        gui.manual.pushed('stop')

    # AUTO MODE
    gui.generic.end_calib_msg(total, count)
    gui.auto.pushed('stop')
    return total
