from util.location.generic import genericCoordinatesCenter


def isExposing():
    return genericCoordinatesCenter('ff/xray_exposing')


# AWS
def blockedIcon():
    return genericCoordinatesCenter('aws/xray_blocked')


def stdbyIcon():
    return genericCoordinatesCenter('aws/xray_standby')


def okExposure():
    return genericCoordinatesCenter('aws/ok')


def calib_button():
    return genericCoordinatesCenter('aws/calib_button')


def fieldCalib():
    return genericCoordinatesCenter('aws/fieldcalib_button')
