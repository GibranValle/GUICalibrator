from util.location.generic import genericCoordinatesCenter, genericCoordinates
from shell.generic import openApp, process_exists, closeApp, changeWindow

def openMUTLMU():
    if process_exists('MUTL.exe'):
        return changeWindow('MU0')
    openApp('MU')


def MU_page_0():
    x0, y0, w, h = genericCoordinates('mutl/MU/mua')
    if x0 and y0 > 0:
        x = x0 + w / 2
        y = y0 + h / 2
        return x, y


def calibration_MU():
    print('LOOKING FOR CALIBRATION MU')
    x0, y0, w, h = genericCoordinates('mutl/MU/mub')
    if x0 and y0 > 0:
        x = x0 + (1 * w / 5)
        y = y0 + h / 2
        return x, y
    x0, y0, w, h = genericCoordinates('mutl/MU/generator_selected', 0.55)
    if x0 and y0 > 0:
        x = x0 + (1 * w / 5)
        y = y0 + h / 2
        return x, y
    x0, y0, w, h = genericCoordinates('mutl/MU/calibration_selected')
    if x0 and y0 > 0:
        return 'selected', 'selected'
    # if x0 and y0 > 0:
    #     x = x0 + (1 * w / 5)
    #     y = y0 + h / 2
    #     return x, y
    print('nothing found')
    return -1, -1


def generator_MU():
    print('LOOKING FOR CALIBRATION gen')
    x0, y0, w, h = genericCoordinates('mutl/MU/mub')
    if x0 and y0 > 0:
        print('mub')
        x = x0 + w / 2
        y = y0 + h / 2
        return x, y

    x0, y0, w, h = genericCoordinates('mutl/MU/calibration_selected')
    if x0 and y0 > 0:
        x = x0 + w / 2
        y = y0 + h / 2
        return x, y

    x0, y0, w, h = genericCoordinates('mutl/MU/generator_selected')
    if x0 and y0 > 0:
        print('gen selected')
        x = x0 + w / 2
        y = y0 + h / 2
        return x, y
    print('nothing found')
    return -1, -1


def enable_ment():
    x, y = genericCoordinatesCenter('mutl/MU/enable_ment')
    if x and y > 0:
        return x, y
    print('nothing found')
    return -1, -1


def toggle_MAG():
    x0, y0, w, h = genericCoordinates('mutl/MU/MAG_HVL')
    if x0 and y0 > 0:
        x = x0 + w / 2
        y = y0 + h / 4
        return x, y
    print('nothing found')
    return -1, -1


def toggle_HVL():
    x0, y0, w, h = genericCoordinates('mutl/MU/MAG_HVL')
    if x0 and y0 > 0:
        x = x0 + w / 2
        y = y0 + 3 * h / 4
        return x, y
    print('nothing found')
    return -1, -1


def MU0():
    x, y = genericCoordinatesCenter('ru/MU0')
    x1, y1 = genericCoordinatesCenter('ru/MU0_S')
    if x > 0 and y > 0:
        return x, y
    if x1 > 0 and y1 > 0:
        return x1, y1
    else:
        return -1, -1


def openCalibrationMUMenu():
    openMUTLMU()
    # is MCU FIRST PAGE?
    x, y = MU_page_0()
    if x > 0 and y > 0:
        # NO FIRST PAGE, CHANGE TO NEXT
        x, y = right()
        if x > 0 and y > 0:
            moveTo(x, y, duration=0.5)
            click(x, y)

    x, y = calibration_MU()
    if x > 0 and y > 0:
        moveTo(x, y, duration=0.5)
        click(x, y)
        return


def openGeneratorMUMenu():
    openMUTLMU()
    # is MCU FIRST PAGE?
    x, y = MU_page_0()
    if x > 0 and y > 0:
        # NO FIRST PAGE, CHANGE TO NEXT
        x, y = right()
        if x > 0 and y > 0:
            moveTo(x, y, duration=0.5)
            click(x, y)

    x, y = generator_MU()
    if x > 0 and y > 0:
        moveTo(x, y, duration=0.5)
        click(x, y)
        return
