from time import sleep
from calibrations.allExposureNeeded import allRequired
from util.misc import printSuccess
from util.serialCOM import communicate
import customtkinter as ck
from classes.constants import prep_exp_time, scale_factor, max_exposure_duration


def smart_exposure_calibration(name: str, gui_object: ck.CTk = None, duration=600):
    gui = gui_object
    print('EXPOSURE CALIB')
    total = 0

    text1 = f'{name} calib starting...'
    text2 = f'Wait for calib signal'
    gui.generic.edit_output(text1, text2)
    time = gui.delay.wait_for_calib_signal(1, duration)
    printSuccess('CALIBRATION SIGNAL FOUND!')
    if time < 0:
        print('aborted')
        text1 = f'{name} calib aborting...'
        text2 = f'Please retry'
        gui.generic.edit_output(text1, text2)
        return
    total += time
    printSuccess('CALIBRATION SIGNAL FOUND!')

    time = allRequired(gui_object)
    if time < 0:
        print('aborted')
        text1 = f'{name} calib aborting...'
        text2 = f'Please retry'
        gui.generic.edit_output(text1, text2)
        return
    total += time
    printSuccess('CALIBRATION FINISHED!')
    return total


def genericCalibration(name, exposures, gui_object: ck.CTk = None, duration=8):
    gui = gui_object
    print('GENERIC CALIB')
    gui.delay.startStatus()
    pause = 30
    total = 0

    gui.generic.clear_output()

    for i in range(1, exposures + 1):

        if gui.delay.status == 'stop':
            break

        if gui.delay.status == 'pause':
            while gui.delay.status == 'pause':
                sleep(1)

        if not communicate("S"):
            return gui.generic.not_responding()

        time = gui.delay.wait_for_stdby_signal(1, prep_exp_time)
        if time >= prep_exp_time * scale_factor:
            return gui.generic.abnormal()
        total += time
        printSuccess('STDBY SIGNAL FOUND!')

        text1 = f'Requested exposure {i} of {exposures}'
        gui.generic.edit_output(text1)
        time = gui.delay.wait_for_exposure_signal(0, 10)
        if time >= prep_exp_time * scale_factor:
            return gui.generic.abnormal()
        total += time
        printSuccess('EXPOSURE SIGNAL FOUND!')

        time += gui.delay.wait_for_block_signal(1, duration)
        if time > max_exposure_duration * scale_factor:
            return gui.generic.abnormal()
        total += time
        printSuccess('BLOCK SIGNAL FOUND!')

        if not communicate("X"):
            return gui.generic.not_responding()

        if i == exposures:
            return gui.generic.request_end()

        if exposures > 1:
            gui.generic.request_end()
            time = gui.delay.wait_for_stdby_signal(1, pause)
            if time < 0:
                return gui.generic.abnormal()
            total += time
            printSuccess('STDBY SIGNAL FOUND!')

    if gui.delay.status == 'stop':
        return gui.generic.abort_requested()

    if name == 'single' or name == 'ten':
        gui.generic.exposure_done(total)
        gui.manual.pushed('stop')
        return

    gui.generic.exposure_done(total, 'Calibration')


def singleShot(gui_object: ck.CTk = None):
    exposures = 1
    genericCalibration('single', exposures, gui_object, duration=15)


def TenShots(gui_object: ck.CTk = None):
    exposures = 10
    genericCalibration('ten', exposures, gui_object, duration=15)
