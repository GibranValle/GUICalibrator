from util.location.location import genericCoordinatesCenter, genericCoordinates


def MCU_page_0():
    x0, y0, w, h = genericCoordinates('mutl/MCU/mcua')
    if x0 and y0 > 0:
        x = x0 + w / 2
        y = y0 + h / 2
        return x, y


def calibration():
    print('LOOKING FOR CALIBRATION')
    x0, y0, w, h = genericCoordinates('mutl/MCU/calibration_selected')
    print(x0, y0)
    if x0 and y0 > 0:
        x = x0 + w / 2
        y = y0 + h / 2
        return x, y
    x0, y0, w, h = genericCoordinates('mutl/MCU/calibration_unselected')
    print(x0, y0)

    if x0 and y0 > 0:
        x = x0 + w / 2
        y = y0 + h / 2
        return x, y
    x0, y0, w, h = genericCoordinates('mutl/MCU/calibration_opt_selected')
    print(x0, y0)
    if x0 and y0 > 0:
        x = x0 + w / 2
        y = y0 + h / 2
        return x, y
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
        x = x0 + (4 * w / 5)
        y = y0 + h / 2
        return x, y
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
