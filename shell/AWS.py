from time import sleep
from util.location.AWS import okExposure, calib_button, fieldCalib
from util.misc import advancedClick, moveN2Click, click_move
from util.CustomExceptions import IconNotFoundError


def enable_FPD_calib():
    x, y = calib_button()
    if x > 0 and y > 0:
        moveN2Click(x, y)
        sleep(1)
        x, y = fieldCalib()
        if x > 0 and y > 0:
            click_move(x, y)
            return True
        raise TypeError("FIELD BUTTON NOT FOUND")
    raise TypeError("CALIB BUTTON NOT FOUND")


def click_calib_button():
    try:
        x, y = calib_button()
        moveN2Click(x, y)
    except IconNotFoundError:
        pass


def click_field_calib():
    try:
        x, y = fieldCalib()
        click_move(x, y)
    except IconNotFoundError:
        pass


def clickOK():
    try:
        x, y = okExposure()
        advancedClick(x, y)
    except IconNotFoundError:
        pass
