from util.location.MU import MU_page_0, search_calibration_MU, search_generator_MU, search_toggle_MAG, \
    search_enable_ment, search_toggle_HVL
from util.location.RU_MUTL import right
from shell.generic import openApp, process_exists, changeWindow
from util.misc import printError, move_n_click, moveN2Click


def openMUTLMU():
    """ Open MUTL without RUPCTools if it is running only change window """
    if process_exists('MUTL.exe'):
        return changeWindow('MU0')
    openApp('MU')


def is_MU_page_0():
    x, y = MU_page_0()
    if x > 0 and y > 0:
        # NO FIRST PAGE, CHANGE TO NEXT
        x, y = right()
        move_n_click(x, y)


def enable_ment():
    openMUTLMU()
    openGeneratorMUMenu()
    x, y = search_enable_ment()
    if x and y > 0:
        move_n_click(x, y)


def toggle_MAG():
    openMUTLMU()
    openCalibrationMUMenu()
    x, y = search_toggle_MAG()
    if x and y > 0:
        move_n_click(x, y)


def toggle_HVL():
    openMUTLMU()
    openCalibrationMUMenu()
    x, y = search_toggle_HVL()
    if x and y > 0:
        move_n_click(x, y)
    printError('TOGGLE HVL BUTTON NOT FOUND')


def openCalibrationMUMenu():
    is_MU_page_0()
    x, y = search_calibration_MU()
    if x == 'selected':
        print('ALREADY SELECTED')
        return
    elif x > 0 and y > 0:
        move_n_click(x, y)
        return
    printError('CALIB MU BUTTON NOT FOUND')


def openGeneratorMUMenu():
    is_MU_page_0()
    x, y = search_generator_MU()
    if x == 'selected':
        print('ALREADY SELECTED')
        return
    elif x > 0 and y > 0:
        move_n_click(x, y)
        return
    printError('GENERATOR MU BUTTON NOT FOUND')
