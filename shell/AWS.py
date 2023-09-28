from time import sleep
from util.location.AWS import okExposure, calib_button, fieldCalib
from util.misc import advancedClick, moveNclick, moveN2Click, printSuccess


def enable_FPD_calib():
    x, y = calib_button()
    if x > 0 and y > 0:
        printSuccess('CALIB BUTTON FOUND!')
        moveN2Click(x, y)
        sleep(0.5)
        x, y = fieldCalib()
        if x > 0 and y > 0:
            printSuccess('FIELD CALIB BUTTON FOUND!')
            moveNclick(x, y)
            return True


def click_calib_button():
    x, y = calib_button()
    moveN2Click(x, y)


def click_field_calib():
    x, y = fieldCalib()
    moveNclick(x, y)


def clickOK():
    x, y = okExposure()
    advancedClick(x, y)
