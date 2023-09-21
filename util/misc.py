from time import sleep
from pyautogui import moveTo, click, position


def printError(text: str):
    print('\x1b[31m' + text + '\x1b[0m')


def printSuccess(text: str):
    print('\x1b[6;30;42m' + text + '\x1b[0m')


def moveNclick(x, y):
    x0, y0 = position()
    if x > 0 and y > 0:
        sleep(0.5)
        click(x, y)
        moveTo(x0, y0)


def moveN2Click(x, y):
    if x > 0 and y > 0:
        moveTo(x, y, duration=0.5)
        click(x, y)
        sleep(0.25)
        click(x, y)
        sleep(0.25)


def advancedClick(x, y):
    x0, y0 = position()
    if x > 0 and y > 0:
        click(x, y)
        moveTo(x0, y0)
