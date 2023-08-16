from shell.MU import enable_calib_button
from shell.generic import openApp, process_exists, changeWindow
from util.location.RU_MUTL import *
from util.location.MCU import *
from util.misc import moveNclick

import customtkinter as ck


def openMUTLMCU():
    if process_exists('MUTL.exe'):
        return changeWindow('MCU0')
    openApp('MCU')


def openCalibrationMenu():
    # is MCU FIRST PAGE?
    x, y = MCU_page_0()
    if x > 0 and y > 0:
        # NO FIRST PAGE, CHANGE TO NEXT
        x, y = right()
        moveNclick(x, y)
    x, y = calibration()
    if x == 'selected':
        print('Already selected')
        return
    moveNclick(x, y)


def openCalibrationOptMenu():
    # is MCU FIRST PAGE?
    x, y = MCU_page_0()
    if x > 0 and y > 0:
        # NO FIRST PAGE, CHANGE TO NEXT
        x, y = right()
        moveNclick(x, y)
    # NO CALIB SELECTED
    x, y = calibrationOptional()
    if x == 'selected':
        print('Already selected')
        return
    moveNclick(x, y)


def startOffsetCalib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = offset()
    moveNclick(x, y)


def startDefectCalib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = defect()
    moveNclick(x, y)


def startDefectSolidCalib(gui_object: ck.CTk = None):
    openMUTLMCU()
    openCalibrationMenu()
    x, y = defectSolid()
    moveNclick(x, y)
    enable_calib_button()


def startPixelDefectCalib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = pixelDefect()
    moveNclick(x, y)
    enable_calib_button()


def startShadingCalib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = shading()
    moveNclick(x, y)
    enable_calib_button()


def startUniformityCalib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = shading()
    moveNclick(x, y)
    enable_calib_button()


def startDefectSolidStereoCalib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = defectSolidStereo()
    moveNclick(x, y)
    enable_calib_button()


def startDefectSolidBpyCalib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = defectSolidBpy()
    moveNclick(x, y)
    enable_calib_button()


def startDefectSolidTomoCalib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = defectSolidTomo()
    moveNclick(x, y)
    enable_calib_button()


def startUniformityStereoCalib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = offset()
    moveNclick(x, y)
    enable_calib_button()


def startUniformityBpyCalib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = uniformityBpy()
    moveNclick(x, y)
    enable_calib_button()


def startUniformityTomoCalib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = uniformityTomo()
    moveNclick(x, y)
    enable_calib_button()


def startUniformityESCalib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = uniformityES()
    moveNclick(x, y)
    enable_calib_button()
