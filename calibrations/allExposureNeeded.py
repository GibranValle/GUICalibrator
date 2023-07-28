import time
from util.serialCOM import communicate
import customtkinter as ck
from util.delayManager import createMessage, isCalibPass


def smartCalibration(name, gui_object: ck.CTk = None, ):
    gui = gui_object
    print('SMART CALIB')
    gui.delay.resetFlags()
    duration = 15
    pause = 30
    total = 0
    count = 0

    while True:
        print('inside while')
        if gui.delay.stopFlag:
            text1 = 'Calibration aborted'
            text2 = 'Please try again'
            gui.generic.edit_output(text1, text2)
            return

        if isCalibPass():
            break

        print('waiting for ready signal')
        text1 = f'Exposures count: {count}'
        gui.generic.edit_output(text1)
        total += gui.delay.waitTillReady(1, pause)

        if not communicate("S"):
            text1 = 'Failed exposure request'
            gui.generic.edit_output(text1)
            return
        print('adding 1 exposure')
        count += 1
        text1 = f'Requested exposure {count}'
        gui.generic.edit_output(text1)
        total += gui.delay.waitTillEnd(1, duration)

        text1 = 'Requested end of exposure'
        gui.generic.edit_output(text1)
        if not communicate("X"):
            text1 = 'Failed requested end'
            gui.generic.edit_output(text1)
            return

    if name == 'all' and not gui.delay.stopFlag:
        text1 = 'Calibration passed!'
        text2 = createMessage('Time', total)
        gui.generic.edit_output(text1, text2 + f' exposures: {count}')
        gui.manual.pushed('stop')


def allRequired(gui_object: ck.CTk = None):
    smartCalibration('all', gui_object)
