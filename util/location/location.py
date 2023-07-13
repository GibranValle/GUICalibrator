import pyautogui
import os

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


def genericCoordinates(name, confidence=0.9):
    try:
        x, y, w, h = pyautogui.locateOnScreen(f'{path}/img/{name}.png', confidence=confidence)
        return x, y, w, h
    except TypeError:
        return -1, -1, -1, -1


def genericCoordinatesCenter(name, confidence=0.9):
    x, y = -1, -1
    try:
        x, y = pyautogui.locateCenterOnScreen(f'{path}/img/{name}.png', confidence=confidence)
        print(x, y)
        return x, y

    except TypeError:
        return x, y


# FF_tools
def isExposing():
    return genericCoordinatesCenter('ff/xray_exposing')


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
