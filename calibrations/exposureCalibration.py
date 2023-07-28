import time
from util.serialCOM import communicate
import customtkinter as ck
from util.delayManager import createMessage


def genericCalibration(name, exposures, gui_object: ck.CTk = None, duration=8):
    gui = gui_object
    print('GENERIC CALIB')
    gui.delay.resetFlags()
    pause = 30
    total = 0

    for i in range(1, exposures + 1):
        if gui.delay.stopFlag:
            break

        if not communicate("S"):
            text1 = 'Failed exposure request'
            gui.generic.edit_output(text1)
            return  # return if no communication is established
        text1 = f'Requested exposure {i} of {exposures}'
        gui.generic.edit_output(text1)
        total += gui.delay.waitTillEnd(1, duration)

        if not communicate("X"):
            text1 = 'Failed requested end'
            gui.generic.edit_output(text1)
            return  # return if no communication is established
        if exposures > 1:
            text1 = 'Requested end of exposure'
            gui.generic.edit_output(text1)
            total += gui.delay.waitTillReady(1, pause)

    if gui.delay.stopFlag:
        text1 = 'Calibration aborted'
        text2 = 'Please try again'
        gui.generic.edit_output(text1, text2)
        return

    if name == 'single':
        text1 = 'Exposure completed!'
        text2 = createMessage('This exposure took', total)
        gui.manual.pushed('stop')

    text1 = 'Calibration completed!'
    text2 = createMessage('This calibration took', total)
    gui.generic.edit_output(text1, text2)


def defectSolidCalib(gui_object: ck.CTk = None):
    exposures = 1
    genericCalibration('defect-solid', exposures, gui_object)


def pixedDefectCalib(gui_object: ck.CTk = None):
    exposures = 1
    genericCalibration('pixel-defect', exposures, gui_object)


def shadingCalib(gui_object: ck.CTk = None):
    exposures = 44
    genericCalibration('shading', exposures, gui_object)


def uniformityCalib(gui_object: ck.CTk = None):
    exposures = 7
    genericCalibration('uniformity', exposures, gui_object)


def defectSolidStereoCalib(gui_object: ck.CTk = None):
    exposures = 2
    genericCalibration('uniformity', exposures, gui_object)


def defectSolidBpyCalib(gui_object: ck.CTk = None):
    exposures = 4
    genericCalibration('uniformity', exposures, gui_object)


def defectSolidTomoCalib(gui_object: ck.CTk = None):
    exposures = 2
    genericCalibration('uniformity', exposures, gui_object)


def uniformityCalibStereo(gui_object: ck.CTk = None):
    exposures = 2
    genericCalibration('uniformity', exposures, gui_object)


def uniformityCalibBpy(gui_object: ck.CTk = None):
    exposures = 4
    genericCalibration('uniformity', exposures, gui_object)


def uniformityCalibTomo(gui_object: ck.CTk = None):
    exposures = 2
    genericCalibration('uniformity', exposures, gui_object)


def uniformityCalibES(gui_object: ck.CTk = None):
    exposures = 2
    genericCalibration('uniformity', exposures, gui_object)


def singleShot(gui_object: ck.CTk = None):
    exposures = 1
    genericCalibration('single', exposures, gui_object, duration=15)


def TenShots(gui_object: ck.CTk = None):
    exposures = 10
    genericCalibration('single', exposures, gui_object, duration=15)


