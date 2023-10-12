from time import sleep
from pyautogui import moveTo, click, position

PRE_CLICK_TIME = 0.5
INTER_CLICK_TIME = 0.5
POST_CLICK_TIME = 0.2


def printError(text: str):
    print('\x1b[31m' + text + '\x1b[0m')


def printSuccess(text: str):
    print('\x1b[6;30;42m' + text + '\x1b[0m')


def moveNclick(x, y):
    x0, y0 = position()
    if x > 0 and y > 0:
        sleep(PRE_CLICK_TIME)
        click(x, y)
        sleep(POST_CLICK_TIME)
        moveTo(x0, y0)
        return
    raise ValueError('POSITION NOT REAL')


def moveN2Click(x, y):
    x0, y0 = position()
    if x > 0 and y > 0:
        sleep(PRE_CLICK_TIME)
        click(x, y)
        sleep(INTER_CLICK_TIME)
        click(x, y)
        sleep(POST_CLICK_TIME)
        moveTo(x0, y0)
        return
    raise ValueError('POSITION NOT REAL')


def advancedClick(x, y):
    x0, y0 = position()
    if x > 0 and y > 0:
        sleep(PRE_CLICK_TIME)
        click(x, y)
        moveTo(x0, y0)
        sleep(POST_CLICK_TIME)
        return
    raise ValueError('POSITION NOT REAL')
