from time import sleep
from util.serialCOM import communicate
import customtkinter as ck


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

        text1 = f'Requested exposure {i} of {exposures}'
        gui.generic.edit_output(text1)
        total += gui.delay.waitTillEnd(1, duration)

        if not communicate("X"):
            return gui.generic.not_responding()

        if i == exposures + 1:
            return gui.generic.request_end()

        if exposures > 1:
            gui.generic.request_end()
            total += gui.delay.waitTillReady(1, pause)

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
