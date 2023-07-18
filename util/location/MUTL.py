from util.location.generic import genericCoordinatesCenter, genericCoordinates


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

