from util.location.generic import genericCoordinatesCenter, genericCoordinates
from util.misc import printError


def search_MCU0():
    x, y = genericCoordinatesCenter('ru/MCU0')
    x1, y1 = genericCoordinatesCenter('ru/MCU0_S')
    if x > 0 and y > 0:
        return x, y
    if x1 > 0 and y1 > 0:
        return x1, y1
    else:
        return -1, -1


def MCU_page_0():
    x0, y0, w, h = genericCoordinates('mutl/MCU/mcua')
    if x0 and y0 > 0:
        x = x0 + w / 2
        y = y0 + h / 2
        return x, y
    printError('MCU PAGE 0 NOT FOUND')
    return -1, -1


def calibration():
    x0, y0, w, h = genericCoordinates('mutl/MCU/calibration_unselected')
    if x0 and y0 > 0:
        x = x0 + w / 2
        y = y0 + h / 2
        return x, y
    x0, y0, w, h = genericCoordinates('mutl/MCU/calibration_opt_selected')
    if x0 and y0 > 0:
        x = x0 + w / 2
        y = y0 + h / 2
        return x, y
    x0, y0, w, h = genericCoordinates('mutl/MCU/calibration_selected')
    if x0 and y0 > 0:
        return 'selected', 'selected'
        # x = x0 + w / 2
        # y = y0 + h / 2
        # return x, y
    printError('CALIBRATION BUTTON NOT FOUND')
    return -1, -1


def calibrationOptional():
    x0, y0, w, h = genericCoordinates('mutl/MCU/calibration_selected')
    if x0 and y0 > 0:
        x = x0 + 4 * w / 5
        y = y0 + h / 2
        return x, y
    x0, y0, w, h = genericCoordinates('mutl/MCU/calibration_unselected')
    if x0 and y0 > 0:
        x = x0 + (4 * w / 5)
        y = y0 + h / 2
        return x, y
    x0, y0, w, h = genericCoordinates('mutl/MCU/calibration_opt_selected')
    if x0 and y0 > 0:
        return 'selected', 'selected'
    #     x = x0 + (4 * w / 5)
    #     y = y0 + h / 2
    #     return x, y
    printError('CALIBRATION OPT BUTTON NOT FOUND')
    return -1, -1


# CALIBRATION MENU
def offset():
    return genericCoordinatesCenter('mutl/calib_offset')


def defect():
    return genericCoordinatesCenter('mutl/calib_defect')


def defectSolid():
    return genericCoordinatesCenter('mutl/calib_defect_solid')


def defectSolidStereo():
    return genericCoordinatesCenter('mutl/calib_defect_solid_stereo')


def defectSolidBpy():
    return genericCoordinatesCenter('mutl/calib_defect_solid_bpy')


def defectSolidTomo():
    return genericCoordinatesCenter('mutl/calib_defect_solid_tomo')


def pixelDefect():
    return genericCoordinatesCenter('mutl/calib_pixel_defect')


def shading():
    return genericCoordinatesCenter('mutl/calib_shading')


def uniformity():
    return genericCoordinatesCenter('mutl/calib_uniformity')


def uniformityStereo():
    return genericCoordinatesCenter('mutl/calib_uniformity_stereo')


def uniformityBpy():
    return genericCoordinatesCenter('mutl/calib_uniformity_bpy')


def uniformityTomo():
    return genericCoordinatesCenter('mutl/calib_uniformity_tomo')


def uniformityES():
    return genericCoordinatesCenter('mutl/calib_uniformity_es')


def sensitivity():
    return genericCoordinatesCenter('mutl/calib_sensitivity')
