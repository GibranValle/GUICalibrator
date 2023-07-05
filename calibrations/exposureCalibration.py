import time

from util.delayManager import waitTillEnd, waitTillReady, createMessage, resetStopFlag, editOutput, getStopFlag
from util.serialCOM import communicate
import customtkinter as ck


def genericCalibration(name, exposures, label_output1, label_output2, duration=8):
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


def defectSolidCalib(label_output1, label_output2):
    exposures = 1
    genericCalibration('defect-solid', exposures, label_output1, label_output2)


def pixedDefectCalib(label_output1, label_output2):
    exposures = 1
    genericCalibration('pixel-defect', exposures, label_output1, label_output2)


def shadingCalib(label_output1, label_output2):
    exposures = 44
    genericCalibration('shading', exposures, label_output1, label_output2)


def uniformityCalib(label_output1, label_output2):
    exposures = 7
    genericCalibration('uniformity', exposures, label_output1, label_output2)


def defectSolidStereoCalib(label_output1, label_output2):
    exposures = 2
    genericCalibration('uniformity', exposures, label_output1, label_output2)


def defectSolidBpyCalib(label_output1, label_output2):
    exposures = 4
    genericCalibration('uniformity', exposures, label_output1, label_output2)


def defectSolidTomoCalib(label_output1, label_output2):
    exposures = 2
    genericCalibration('uniformity', exposures, label_output1, label_output2)


def uniformityCalibStereo(label_output1, label_output2):
    exposures = 2
    genericCalibration('uniformity', exposures, label_output1, label_output2)


def uniformityCalibBpy(label_output1, label_output2):
    exposures = 4
    genericCalibration('uniformity', exposures, label_output1, label_output2)


def uniformityCalibTomo(label_output1, label_output2):
    exposures = 2
    genericCalibration('uniformity', exposures, label_output1, label_output2)


def uniformityCalibES(label_output1, label_output2):
    exposures = 2
    genericCalibration('uniformity', exposures, label_output1, label_output2)


def singleShot(label1: ck.CTkLabel, label2: ck.CTkLabel):
    exposures = 1
    genericCalibration('single', exposures, label1, label2, duration=15)
