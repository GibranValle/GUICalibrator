from pyautogui import moveTo, click
from shell.generic import _process_exists, changeWindow, openApp
from util.location.MUTL import *
from util.location.MUTL_MCU import *


def openMUTLMCU():
    if _process_exists('MUTL.exe'):
        return changeWindow('MCU0')
    openApp('MCU')


def openCalibrationMenu():
    openMUTLMCU()
    # is MCU FIRST PAGE?
    x, y = MCU_page_0()
    if x > 0 and y > 0:
        # NO FIRST PAGE, CHANGE TO NEXT
        x, y = right()
        if x > 0 and y > 0:
            moveTo(x, y, duration=0.5)
            click(x, y)

    x, y = calibration()
    if x > 0 and y > 0:
        moveTo(x, y, duration=0.5)
        click(x, y)
    elif x == 'selected':
        print('Already selected')


def openCalibrationOptMenu():
    openMUTLMCU()
    # is MCU FIRST PAGE?
    x, y = MCU_page_0()
    if x > 0 and y > 0:
        # NO FIRST PAGE, CHANGE TO NEXT
        x, y = right()
        if x > 0 and y > 0:
            moveTo(x, y, duration=0.5)
            click(x, y)
    # NO CALIB SELECTED
    x, y = calibrationOptional()
    if x > 0 and y > 0:
        moveTo(x, y, duration=0.5)
        click(x, y)
    elif x == 'selected':
        print('Already selected')


def startOffsetCalib():
    openCalibrationMenu()
    x, y = offset()
    if x <= 0 and y <= 0:
        return
    moveTo(x, y, duration=0.5)
    click(x, y)


def startDefectCalib():
    openCalibrationMenu()
    x, y = defect()
    if x <= 0 and y <= 0:
        return
    moveTo(x, y, duration=0.5)
    click(x, y)


def startDefectSolidCalib():
    openCalibrationMenu()
    x, y = defectSolid()
    if x <= 0 and y <= 0:
        return
    moveTo(x, y, duration=0.5)
    click(x, y)


def startPixelDefectCalib():
    openCalibrationMenu()
    x, y = pixelDefect()
    if x <= 0 and y <= 0:
        return
    moveTo(x, y, duration=0.5)
    click(x, y)


def startShadingCalib():
    openCalibrationMenu()
    x, y = shading()
    if x <= 0 and y <= 0:
        return
    moveTo(x, y, duration=0.5)
    click(x, y)


def startUniformityCalib():
    openCalibrationMenu()
    x, y = shading()
    if x <= 0 and y <= 0:
        return
    moveTo(x, y, duration=0.5)
    click(x, y)


def startDefectSolidStereoCalib():
    openCalibrationMenu()
    x, y = defectSolidStereo()
    if x <= 0 and y <= 0:
        return
    moveTo(x, y, duration=0.5)
    click(x, y)


def startDefectSolidBpyCalib():
    openCalibrationMenu()
    x, y = defectSolidBpy()
    if x <= 0 and y <= 0:
        return
    moveTo(x, y, duration=0.5)
    click(x, y)


def startDefectSolidTomoCalib():
    openCalibrationMenu()
    x, y = defectSolidTomo()
    if x <= 0 and y <= 0:
        return
    moveTo(x, y, duration=0.5)
    click(x, y)


def startUniformityStereoCalib():
    openCalibrationMenu()
    x, y = offset()
    if x <= 0 and y <= 0:
        return
    moveTo(x, y, duration=0.5)
    click(x, y)


def startUniformityBpyCalib():
    openCalibrationMenu()
    x, y = uniformityBpy()
    if x <= 0 and y <= 0:
        return
    moveTo(x, y, duration=0.5)
    click(x, y)


def startUniformityTomoCalib():
    openCalibrationMenu()
    x, y = uniformityTomo()
    if x <= 0 and y <= 0:
        return
    moveTo(x, y, duration=0.5)
    click(x, y)


def startUniformityESCalib():
    openCalibrationMenu()
    x, y = uniformityES()
    if x <= 0 and y <= 0:
        return
    moveTo(x, y, duration=0.5)
    click(x, y)
