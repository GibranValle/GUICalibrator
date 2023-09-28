from time import sleep
from pyautogui import moveTo, click, position


def printError(text: str):
    print('\x1b[31m' + text + '\x1b[0m')


def printSuccess(text: str):
    print('\x1b[6;30;42m' + text + '\x1b[0m')


def moveNclick(x, y):
    x0, y0 = position()
    if x > 0 and y > 0:
        click(x, y)
        moveTo(x0, y0)


def moveN2Click(x, y):
    x0, y0 = position()
    if x > 0 and y > 0:
        click(x, y)
        sleep(0.4)
        click(x, y)
        moveTo(x0, y0)


def advancedClick(x, y):
    x0, y0 = position()
    if x > 0 and y > 0:
        click(x, y)
        moveTo(x0, y0)
        return
