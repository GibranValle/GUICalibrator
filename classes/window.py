from pyautogui import moveTo, click
from shell.MCU import *
from util.location.MUTL import *
from util.location.MUTL_MCU import *


def windowOptions(option):
    if option == 'Ok red':
        moveTo(okExposure(), duration=0.5)
        click(okExposure())

    elif option == 'Calib button':
        moveTo(calib_button(), duration=0.5)
        click(calib_button())
        time.sleep(0.25)
        click(calib_button())

    elif option == 'Field calib button':
        moveTo(calib_button(), duration=0.25)
        click(calib_button())
        time.sleep(0.25)
        click(calib_button())
        time.sleep(0.25)
        moveTo(fieldCalib(), duration=0.25)
        click(fieldCalib())

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
        moveTo(toggle_HVL(), duration=0.25)
        click(toggle_HVL())

    elif option == 'Toggle MAG':
        openCalibrationMUMenu()
        moveTo(toggle_MAG(), duration=0.25)
        click(toggle_MAG())

    elif option == 'Enable Ment Mode':
        openGeneratorMUMenu()
        moveTo(enable_ment(), duration=0.25)
        click(enable_ment())

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
