import pyautogui
import os

path = os.getcwd()


def genericCoordinates(name):
    confidence = 0.9
    if name == 'mutl/calibration_s':
        confidence = 0.55
    x, y = -1, -1
    try:
        x, y = pyautogui.locateCenterOnScreen(f'{path}/img/{name}.png', confidence=confidence)
        return x, y

    except TypeError:
        return x, y


# FF_tools
def isExposing():
    return genericCoordinates('ff/xray_exposing')


# AWS
def blockedIcon():
    return genericCoordinates('aws/xray_blocked')


def stdbyIcon():
    return genericCoordinates('aws/xray_standby')


def okExposure():
    return genericCoordinates('aws/ok')


def calib_button():
    return genericCoordinates('aws/calib_button')


def fieldCalib():
    return genericCoordinates('aws/fieldcalib_button')


# RUPCTOOL SCREEN
def MU0():
    x, y = genericCoordinates('ru/MU0')
    x1, y1 = genericCoordinates('ru/MU0_S')
    if x > 0 and y > 0:
        return x, y
    if x1 > 0 and y1 > 0:
        return x1, y1
    else:
        return -1, -1


def MCU0():
    x, y = genericCoordinates('ru/MCU0')
    x1, y1 = genericCoordinates('ru/MCU0_S')
    if x > 0 and y > 0:
        return x, y
    if x1 > 0 and y1 > 0:
        return x1, y1
    else:
        return -1, -1


def mutl():
    return genericCoordinates('ru/mutl')


def new():
    return genericCoordinates('ru/new')


def install():
    return genericCoordinates('ru/install')


# MUTL
def calibration():
    x, y = genericCoordinates('mutl/calibration')
    x1, y1 = genericCoordinates('mutl/calibration_s')
    print(x, x1, y, y1)
    if x > 0 and y > 0:
        return x, y
    if x1 > 0 and y1 > 0:
        return x1, y1
    else:
        return -1, -1


def calibrationOptional():
    x, y = genericCoordinates('mutl/calibration_option')
    x1, y1 = genericCoordinates('mutl/calibration_option_s')
    print(x, x1, y, y1)
    if x > 0 and y > 0:
        return x, y
    if x1 > 0 and y1 > 0:
        return x1, y1
    else:
        return -1, -1


def left():
    return genericCoordinates('mutl/left')


def right():
    return genericCoordinates('mutl/right')


#CALIBRATION MENU
def offset():
    return genericCoordinates('mutl/calib_offset')


def defect():
    return genericCoordinates('mutl/calib_defect')


def defectSolid():
    return genericCoordinates('mutl/calib_defect_solid')


def defectSolidStereo():
    return genericCoordinates('mutl/calib_defect_solid_stereo')


def defectSolidBpy():
    return genericCoordinates('mutl/calib_defect_solid_bpy')


def defectSolidTomo():
    return genericCoordinates('mutl/calib_defect_solid_tomo')


def pixelDefect():
    return genericCoordinates('mutl/calib_pixel_defect')


def shading():
    return genericCoordinates('mutl/calib_shading')


def uniformity():
    return genericCoordinates('mutl/calib_uniformity')


def uniformityStereo():
    return genericCoordinates('mutl/calib_uniformity_stereo')


def uniformityBpy():
    return genericCoordinates('mutl/calib_uniformity_bpy')


def uniformityTomo():
    return genericCoordinates('mutl/calib_uniformity_tomo')


def uniformityES():
    return genericCoordinates('mutl/calib_uniformity_es')


def sensitivity():
    return genericCoordinates('mutl/calib_sensitivity')


