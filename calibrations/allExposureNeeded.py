from time import sleep
from util.serialCOM import communicate
import customtkinter as ck
from util.delayManager import isCalibPass
from shell.AWS import clickOK
from classes.constants import prep_exp_time, scale_factor, max_exposure_duration, time_between_exposures


def smartCalibration(name, gui_object: ck.CTk = None, ):
    gui = gui_object
    print('SMART CALIB')
    gui.delay.startStatus()
    total = 0
    count = 0

    while True:
        while gui.delay.status == 'pause':
            sleep(1)
        if gui.delay.status == 'stop':
            print('stop button')
            return gui.generic.abort_requested()
        if isCalibPass():
            break
        if gui.is_auto_ok:
            clickOK()
        gui.generic.count(count)
        time = gui.delay.wait_for_stdby_signal(1, prep_exp_time)
        total += time
        if time >= prep_exp_time * scale_factor:
            return gui.generic.abnormal()
        if not communicate("S"):
            return gui.generic.not_responding()
        text1 = f'Requested exposure {count}'
        gui.generic.edit_output(text1)
        time = gui.delay.wait_for_exposure_signal(1, max_exposure_duration)
        if time > max_exposure_duration * scale_factor:
            return gui.generic.abnormal()
        total += time
        time = gui.delay.wait_for_block_signal(1, time_between_exposures)
        if time > time_between_exposures * scale_factor:
            return gui.generic.abnormal()
        total += time
        gui.generic.request_end()
        if not communicate("X"):
            return gui.generic.not_responding()
        if isCalibPass():
            break
        count += 1

    gui.generic.exposure_done_counter(total, count)
    gui.manual.pushed('stop')
    return total


def allRequired(gui_object: ck.CTk = None):
    total = smartCalibration('all', gui_object)
    return total
