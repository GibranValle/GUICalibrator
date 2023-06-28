import time

from util.delayManager import waitTillEnd, waitTillReady, createText
from util.serialCOM import communicate


def editLabel1(text, label_output1):
    if len(text) > 0:
        label_output1.configure(text=text)


def editLabel2(text, label_output2):
    if len(text) > 0:
        label_output2.configure(text=text)


def genericCalibration(name, exposures, label_output1, label_output2):
    duration = 8
    pause = 30
    totaltime = 0

    for i in range(1, exposures+1):
        if not communicate("S"):
            text = f'Failed exposure request'
            editLabel1(text, label_output1)
            return  # return if no communication is established
        text = f'Requested exposure {i} of {exposures}'
        editLabel1(text, label_output1)

        totaltime += waitTillEnd(1, duration, label_output2)

        if not communicate("X"):
            text = f'Failed requested end'
            editLabel1(text, label_output1)
            return  # return if no communication is established
        if exposures > 1:
            text = f'Requested end of exposure'
            editLabel1(text, label_output1)
            totaltime += waitTillReady(1, pause, label_output2)

    text = createText('This calibration took', totaltime)
    if name == 'single':
        text = createText('This exposure took', totaltime)
    editLabel1(text, label_output1)

    text = 'Calibration completed!'
    if name == 'single':
        text = 'Exposure completed!'
    editLabel2(text, label_output2)


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
    
    
def singleShot(label_output1, label_output2):
    exposures = 1
    genericCalibration('single', exposures, label_output1, label_output2)
