from time import sleep
from util.serialCOM import communicate
import customtkinter as ck
from util.delayManager import isCalibPass


def smartCalibration(name, gui_object: ck.CTk = None, ):
    gui = gui_object
    print('SMART CALIB')
    gui.delay.startStatus()
    scale_factor = 0.75
    max_exposure_duration = 15
    time_between_exposures = 30
    prep_exp_time = 1200
    total = 0
    count = 0

    while True:
        while gui.delay.status == 'pause':
            sleep(1)

        if gui.delay.status == 'stop':
            return gui.generic.abort_requested()

        if isCalibPass():
            break

        gui.generic.count(count)
        time = gui.delay.waitTillReady(1, prep_exp_time)
        total += time
        if time >= prep_exp_time * scale_factor:
            return gui.generic.abnormal()

        if not communicate("S"):
            return gui.generic.not_responding()

        text1 = f'Requested exposure {count}'
        gui.generic.edit_output(text1)
        time = gui.delay.waitTillExposing(1, max_exposure_duration)
        if time > max_exposure_duration * scale_factor:
            return gui.generic.abnormal()
        total += time

        time = gui.delay.waitTillEnd(1, time_between_exposures)
        if time > time_between_exposures * scale_factor:
            return gui.generic.abnormal()
        total += time

        gui.generic.request_end()

        if not communicate("X"):
            return gui.generic.not_responding()

        count += 1

    if name == 'all':
        gui.generic.exposure_done_exp(total, count)
        gui.manual.pushed('stop')


def allRequired(gui_object: ck.CTk = None):
    smartCalibration('all', gui_object)
