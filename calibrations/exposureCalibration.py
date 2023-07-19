import time

from util.delayManager import waitTillEnd, waitTillReady, createMessage, resetStopFlag, editOutput, getStopFlag, \
    editButton
from util.serialCOM import communicate
import customtkinter as ck


def genericCalibration(name, exposures, gui_object: ck.CTk = None, duration=8):
    label_output1 = gui_object.label_output1
    label_output2 = gui_object.label_output2
    button = gui_object.button_run

    resetStopFlag()
    pause = 30
    total = 0

    for i in range(1, exposures + 1):
        if getStopFlag():
            break

        if not communicate("S"):
            text = f'Failed exposure request'
            editOutput(text, label_output1)
            return  # return if no communication is established
        text = f'Requested exposure {i} of {exposures}'
        editOutput(text, label_output1)

        total += waitTillEnd(1, duration, label_output2)

        if not communicate("X"):
            text = f'Failed requested end'
            editOutput(text, label_output1)
            return  # return if no communication is established
        if exposures > 1:
            text = f'Requested end of exposure'
            editOutput(text, label_output1)
            total += waitTillReady(1, pause, label_output2)

    if getStopFlag():
        text = 'Calibration aborted'
        editOutput(text, label_output1)
        text = 'Please try again'
        editOutput(text, label_output2)
        return

    text = createMessage('This calibration took', total)
    if name == 'single':
        text = createMessage('This exposure took', total)
    editOutput(text, label_output1)

    text = 'Calibration completed!'
    if name == 'single':
        text = 'Exposure completed!'
    editOutput(text, label_output2)
    gui_object.isRunning = False
    editButton('Start Calibration', button)


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
