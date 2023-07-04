import pyautogui
import os
import sys

path = os.getcwd()
"""
from pathlib import Path
def fetch_resource(resource_path: Path) -> Path:
    Function needed to run --onefile
    :param resource_path:
    :return:
    try:  # running as *.exe; fetch resource from temp directory
        base_path = Path(sys._MEIPASS)
    except AttributeError:  # running as script; return unmodified path
        return resource_path
    else:  # return temp resource path
        return base_path.joinpath(resource_path)
"""

def genericCoordinates(name):
    confidence = 0.9
    try:
        x, y, w, h = pyautogui.locateOnScreen(f'{path}/img/{name}.png', confidence=confidence)
        return x, y, w, h
    except TypeError:
        return -1, -1


def genericCoordinatesCenter(name):
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
    return genericCoordinatesCenter('ff/xray_exposing')


# AWS
def blockedIcon():
    return genericCoordinatesCenter('aws/xray_blocked')


def stdbyIcon():
    return genericCoordinatesCenter('aws/xray_standby')


def okExposure():
    return genericCoordinatesCenter('aws/ok')


def calib_button():
    return genericCoordinatesCenter('aws/calib_button')


def fieldCalib():
    return genericCoordinatesCenter('aws/fieldcalib_button')


# RUPCTOOL SCREEN
def MU0():
    x, y = genericCoordinatesCenter('ru/MU0')
    x1, y1 = genericCoordinatesCenter('ru/MU0_S')
    if x > 0 and y > 0:
        return x, y
    if x1 > 0 and y1 > 0:
        return x1, y1
    else:
        return -1, -1


def MCU0():
    x, y = genericCoordinatesCenter('ru/MCU0')
    x1, y1 = genericCoordinatesCenter('ru/MCU0_S')
    if x > 0 and y > 0:
        return x, y
    if x1 > 0 and y1 > 0:
        return x1, y1
    else:
        return -1, -1


def mutl():
    return genericCoordinatesCenter('ru/mutl')


def new():
    return genericCoordinatesCenter('ru/new')


def install():
    return genericCoordinatesCenter('ru/install')


# MUTL
def calibration():
    x0, y0, w, h = genericCoordinates('mutl/calibration_selected')
    if x0 and y0 > 0:
        x = x0 + w/2
        y = y0 + h/2
        return x, y
    x0, y0, w, h = genericCoordinates('mutl/calibration_unselected')
    if x0 and y0 > 0:
        x = x0 + 3*w/7
        y = y0 + h/2
        return x, y
    x0, y0, w, h = genericCoordinates('mutl/calibration_opt_selected')
    if x0 and y0 > 0:
        x = x0 + (2*w/5)
        y = y0 + h/2
        return x, y
    return -1, -1


def calibrationOptional():
    x0, y0, w, h = genericCoordinates('mutl/calibration_selected')
    if x0 and y0 > 0:
        x = x0 + 4*w/5
        y = y0 + h/2
        return x, y
    x0, y0, w, h = genericCoordinates('mutl/calibration_unselected')
    if x0 and y0 > 0:
        x = x0 + (4*w/5)
        y = y0 + h/2
        return x, y
    x0, y0, w, h = genericCoordinates('mutl/calibration_opt_selected')
    if x0 and y0 > 0:
        x = x0 + (4*w/5)
        y = y0 + h/2
        return x, y
    return -1, -1


def lastPage():
    # only left
    x0, y0, w, h = genericCoordinates('mutl/left_noright')
    if x0 > 0 and y0 > 0:
        y = y0 + h/2
        x = x0 + w/4
        return x, y
    return -1, -1


def firstPage():
    x0, y0, w, h = genericCoordinates('mutl/right_noleft')
    if x0 > 0 and y0 > 0:
        y = y0 + h/2
        x = x0 + (3*w/4)
        return x, y
    return -1, -1


def midPage(side):
    x0, y0, w, h = genericCoordinates('mutl/left_right')
    if x0 > 0 and y0 > 0:
        if side == 'left' and x0 > 0:
            y = y0 + h / 2
            x = x0 + w / 4
            return x, y
        if side == 'right' and x0 > 0:
            y = y0 + h / 2
            x = x0 + (3 * w / 4)
            return x, y
    return -1, -1


def left():
    x, y = lastPage()
    if x > 0 and y > 0:
        return x, y
    x, y = midPage('left')
    if x > 0 and y > 0:
        return x, y
    print('No icon found')
    return -1, -1


def right():
    x, y = firstPage()
    if x > 0 and y > 0:
        return x, y
    x, y = midPage('right')
    if x > 0 and y > 0:
        return x, y
    print('No icon found')
    return -1, -1



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


