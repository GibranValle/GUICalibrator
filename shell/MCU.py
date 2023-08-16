from shell.MU import enable_calib_button
from shell.generic import openApp, process_exists, changeWindow
from util.location.RU_MUTL import *
from util.location.MCU import *
from util.misc import moveNclick
from util.location.AWS import okExposure
from threading import Thread
from calibrations.exposureCalibration import defectSolidCalib
import customtkinter as ck

def openMUTLMCU():
    if process_exists('MUTL.exe'):
        return changeWindow('MCU0')
    openApp('MCU')


def waitThread(gui_object: ck.CTk = None, calib_name=''):
    label = gui_object.label
    gui_object.delay.waitTillOk(0, 10 * 60, label)
    x, y = okExposure()
    moveNclick(x, y)
    gui_object.delay.waitTillOk(0, 20, label)
    if calib_name == 'defect solid':
        defectSolidCalib()


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
    Thread(target=waitThread, args=[gui_object, 'defect solid'], daemon=True).start()


def startPixelDefectCalib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = pixelDefect()
    moveNclick(x, y)


def startShadingCalib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = shading()
    moveNclick(x, y)


def startUniformityCalib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = shading()
    moveNclick(x, y)


def startDefectSolidStereoCalib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = defectSolidStereo()
    moveNclick(x, y)


def startDefectSolidBpyCalib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = defectSolidBpy()
    moveNclick(x, y)


def startDefectSolidTomoCalib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = defectSolidTomo()
    moveNclick(x, y)


def startUniformityStereoCalib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = offset()
    moveNclick(x, y)


def startUniformityBpyCalib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = uniformityBpy()
    moveNclick(x, y)


def startUniformityTomoCalib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = uniformityTomo()
    moveNclick(x, y)


def startUniformityESCalib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = uniformityES()
    moveNclick(x, y)
