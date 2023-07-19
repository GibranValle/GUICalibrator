from util.location.AWS import *
from shell.RU_MUTL import *
from shell.MCU import *
from shell.MU import *
from util.misc import moveNclick, moveN2Click


def windowOptions(option):
    print(option)
    if option == 'Ok red':
        x, y = okExposure()
        moveNclick(x, y)

    elif option == 'Calib button':
        x, y = calib_button()
        moveN2Click(x, y)

    elif option == 'Field calib button':
        enable_calib_button()

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
        toggle_HVL()

    elif option == 'Toggle MAG':
        toggle_MAG()

    elif option == 'Enable Ment Mode':
        enable_ment()

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
