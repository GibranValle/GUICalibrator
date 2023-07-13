from util.location.location import genericCoordinatesCenter, genericCoordinates


def mutl():
    return genericCoordinatesCenter('ru/mutl')


def new():
    return genericCoordinatesCenter('ru/new')


def install():
    return genericCoordinatesCenter('ru/install')


# MUTL
def left():
    x0, y0, w, h = genericCoordinates('mutl/right_noleft')
    if x0 and y0 > 0:
        x = x0 + w / 3
        y = y0 + h / 2
        return x, y

    x0, y0, w, h = genericCoordinates('mutl/left_right')
    if x0 and y0 > 0:
        x = x0 + w / 3
        y = y0 + h / 2
        return x, y

    x0, y0, w, h = genericCoordinates('mutl/left_noright')
    if x0 and y0 > 0:
        x = x0 + w / 3
        y = y0 + h / 2
        return x, y

    print('No icon found')
    return -1, -1


def right():
    x0, y0, w, h = genericCoordinates('mutl/right_noleft')
    if x0 and y0 > 0:
        x = x0 + 2 * w / 3
        y = y0 + h / 2
        return x, y

    x0, y0, w, h = genericCoordinates('mutl/left_right')
    if x0 and y0 > 0:
        x = x0 + 2 * w / 3
        y = y0 + h / 2
        return x, y

    x0, y0, w, h = genericCoordinates('mutl/left_noright')
    if x0 and y0 > 0:
        x = x0 + 2 * w / 3
        y = y0 + h / 2
        return x, y
    print('No icon found')
    return -1, -1


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

    x0, y0, w, h = genericCoordinates('mutl/MU/calibration_selected')
    if x0 and y0 > 0:
        x = x0 + (1 * w / 5)
        y = y0 + h / 2
        return x, y

    x0, y0, w, h = genericCoordinates('mutl/MU/generator_selected', 0.55)
    if x0 and y0 > 0:
        x = x0 + (1 * w / 5)
        y = y0 + h / 2
        return x, y
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
