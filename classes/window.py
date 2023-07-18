from pyautogui import moveTo, click
from shell.MCU import *
from util.location.MUTL import *
from util.location.MUTL_MCU import *
from util.location.AWS import *
from shell.generic import *
from shell.RU import *
from shell.MCU import *
from shell.MU import *
from time import sleep


def _moveNclick(x, y):
    if x > 0 and y > 0:
        moveTo(x, y, duration=0.5)
        click(x, y)
        sleep(0.25)


def _moveN2Click(x, y):
    if x > 0 and y > 0:
        moveTo(x, y, duration=0.5)
        click(x, y)
        sleep(0.25)
        click(x, y)


def windowOptions(option):
    if option == 'Ok red':
        x, y = okExposure()
        _moveNclick(x, y)

    elif option == 'Calib button':
        x, y = calib_button()
        _moveN2Click(x, y)

    elif option == 'Field calib button':
        x, y = calib_button()
        _moveN2Click(x, y)

        x, y = fieldCalib()
        _moveNclick(x, y)

    elif option == 'Open RU':
        openRU()

    elif option == 'Close RU':
        closeRU()

    elif option == 'Open MUTL MU':
        openMUTLMU()

    elif option == 'Open MUTL MCU':
        openMUTLMCU()

    elif option == 'Close MUTL':
        closeMUTL()

    elif option == 'Toggle HVL':
        openCalibrationMUMenu()
        x, y = toggle_HVL()
        _moveNclick(x, y)

    elif option == 'Toggle MAG':
        openCalibrationMUMenu()
        x, y = toggle_MAG()
        _moveNclick(x, y)

    elif option == 'Enable Ment Mode':
        openGeneratorMUMenu()
        x, y = enable_ment()
        _moveNclick(x, y)

    elif 'offset' in option:
        startOffsetCalib()

    elif 'defect' in option:
        startDefectCalib()

    elif 'defect solid' in option:
        startDefectCalib()

    elif 'pixel defect' in option:
        startPixelDefectCalib()

    elif 'shading' in option:
        startShadingCalib()

    elif 'uniformity' in option:
        startUniformityCalib()

    elif 'defect solid stereo' in option:
        startDefectSolidCalib()

    elif 'defect solid biopsy' in option:
        startDefectSolidBpyCalib()

    elif 'defect solid tomo' in option:
        startDefectSolidTomoCalib()

    elif 'x-ray uniformity stereo' in option:
        startUniformityStereoCalib()

    elif 'x-ray uniformity biopsy' in option:
        startUniformityBpyCalib()

    elif 'x-ray uniformity tomo' in option:
        startUniformityTomoCalib()

    elif 'x-ray uniformity ES' in option:
        startUniformityESCalib()
