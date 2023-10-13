from util.location.generic import genericCoordinatesCenter
from util.CustomExceptions import IconNotFoundError


def exposureIconLarge() -> tuple[int, int]:
    return genericCoordinatesCenter("ff/xray_exposing")


# AWS
def exposureIcon() -> tuple[int, int]:
    return genericCoordinatesCenter("aws/xray_exposure", 0.95)


def blockedIcon() -> tuple[int, int]:
    return genericCoordinatesCenter("aws/xray_blocked", 0.9)


def stdbyIcon() -> tuple[int, int]:
    return genericCoordinatesCenter("aws/xray_standby", 0.95)


def okExposure() -> tuple[int, int]:
    return genericCoordinatesCenter("aws/ok")


def okExposure_green() -> tuple[int, int]:
    return genericCoordinatesCenter("aws/ok2")


def calib_button() -> tuple[int, int]:
    return genericCoordinatesCenter("aws/calib_button")


def fieldCalib() -> tuple[int, int]:
    return genericCoordinatesCenter("aws/fieldcalib_button")


def fpd_calibrating() -> tuple[int, int]:
    try:
        genericCoordinatesCenter("aws/pasar", 0.95)
        genericCoordinatesCenter("aws/saltar", 0.95)
    except IconNotFoundError:
        pass
    return genericCoordinatesCenter("aws/calibracion", 0.98)


def pass_icon() -> tuple[int, int]:
    return genericCoordinatesCenter("aws/pasar", 0.95)


def saltar_icon() -> tuple[int, int]:
    return genericCoordinatesCenter("aws/saltar", 0.95)
