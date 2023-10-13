from util.location.generic import genericCoordinatesCenter, genericCoordinates


def mutl():
    return genericCoordinatesCenter("ru/mutl")


def new():
    return genericCoordinatesCenter("ru/new")


def install():
    return genericCoordinatesCenter("ru/install")


# MUTL
def left() -> tuple[int, int]:
    x0, y0, w, h = genericCoordinates("mutl/right_noleft")
    if x0 and y0 > 0:
        x = int(x0 + w / 3)
        y = int(y0 + h / 2)
        return x, y

    x0, y0, w, h = genericCoordinates("mutl/left_right")
    if x0 and y0 > 0:
        x = int(x0 + w / 3)
        y = int(y0 + h / 2)
        return x, y

    x0, y0, w, h = genericCoordinates("mutl/left_noright")
    if x0 and y0 > 0:
        x = int(x0 + w / 3)
        y = int(y0 + h / 2)
        return x, y

    print("No icon found")
    return -1, -1


def right() -> tuple[int, int]:
    x0, y0, w, h = genericCoordinates("mutl/right_noleft")
    if x0 and y0 > 0:
        x = int(x0 + 2 * w / 3)
        y = int(y0 + h / 2)
        return x, y

    x0, y0, w, h = genericCoordinates("mutl/left_right")
    if x0 and y0 > 0:
        x = int(x0 + 2 * w / 3)
        y = int(y0 + h / 2)
        return x, y

    x0, y0, w, h = genericCoordinates("mutl/left_noright")
    if x0 and y0 > 0:
        x = int(x0 + 2 * w / 3)
        y = int(y0 + h / 2)
        return x, y
    print("No icon found")
    return -1, -1
