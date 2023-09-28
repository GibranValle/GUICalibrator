from util.location.generic import genericCoordinates, genericCoordinatesCenter
from util.misc import printError


def MU_page_0():
    """ Look if is in page 0 """
    x0, y0, w, h = genericCoordinates('mutl/MU/mua')
    if x0 and y0 > 0:
        x = x0 + w / 2
        y = y0 + h / 2
        return x, y
    printError('not in page 0')
    return -1, -1


def search_MU0():
    x, y = genericCoordinatesCenter('ru/MU0')
    x1, y1 = genericCoordinatesCenter('ru/MU0_S')
    if x > 0 and y > 0:
        return x, y
    if x1 > 0 and y1 > 0:
        return x1, y1
    printError('MU0 BUTTON NOT FOUND')
    return -1, -1


def search_calibration_MU():
    """ Look for calibration button if not pressed """
    x0, y0, w, h = genericCoordinates('mutl/MU/mub')
    if x0 and y0 > 0:
        x = x0 + (1 * w / 5)
        y = y0 + h / 2
        return x, y
    x0, y0, w, h = genericCoordinates('mutl/MU/generator_selected')
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
    printError('MU CALIB BUTTON NOT FOUND')
    return -1, -1


def search_generator_MU():
    """ Look for generator button if not pressed """
    x0, y0, w, h = genericCoordinates('mutl/MU/mub')
    if x0 and y0 > 0:
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
        return 'selected', 'selected'
        # x = x0 + w / 2
        # y = y0 + h / 2
        # return x, y
    printError('GENERATOR BUTTON NOT FOUND')
    return -1, -1


def search_toggle_MAG():
    x0, y0, w, h = genericCoordinates('mutl/MU/MAG_HVL')
    if x0 and y0 > 0:
        x = x0 + w / 2
        y = y0 + h / 4
        return x, y
    printError('MAG BUTTON NOT FOUND')
    return -1, -1


def search_toggle_HVL():
    x0, y0, w, h = genericCoordinates('mutl/MU/MAG_HVL')
    if x0 and y0 > 0:
        x = x0 + w / 2
        y = y0 + h / 4
        return x, y
    printError('HVL BUTTON NOT FOUND')
    return -1, -1


def search_enable_ment():
    x, y = genericCoordinatesCenter('mutl/MU/enable_ment')
    if x and y > 0:
        return x, y
    printError('HVL BUTTON NOT FOUND')
    return -1, -1

