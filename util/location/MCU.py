from util.location.generic import genericCoordinatesCenter, genericCoordinates
from util.misc import printError


def search_MCU0_button():
    x, y = genericCoordinatesCenter('ru/MCU0')
    x1, y1 = genericCoordinatesCenter('ru/MCU0_S')
    if x > 0 and y > 0:
        return x, y
    if x1 > 0 and y1 > 0:
        return x1, y1
    else:
        return -1, -1


def search_MCU_page_0():
    x0, y0, w, h = genericCoordinates('mutl/MCU/mcua')
    if x0 and y0 > 0:
        x = x0 + w / 2
        y = y0 + h / 2
        return x, y
    printError('MCU PAGE 0 NOT FOUND')
    return -1, -1


def search_calibration_tab():
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
        print('ALREADY SELECTED')
        return 'selected', 'selected'
        # x = x0 + w / 2
        # y = y0 + h / 2
        # return x, y
    printError('CALIBRATION TAB NOT FOUND')
    return -1, -1


def search_calibration_optional_tab():
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
    printError('CALIBRATION OPT TAB NOT FOUND')
    return -1, -1


# CALIBRATION MENU
def search_offset_button():
    return genericCoordinatesCenter('mutl/calib_offset')


def search_defect_button():
    return genericCoordinatesCenter('mutl/calib_defect')


def search_defect_solid_button():
    return genericCoordinatesCenter('mutl/calib_defect_solid')


def search_defect_solid_stereo_button():
    return genericCoordinatesCenter('mutl/calib_defect_solid_stereo')


def search_defect_solid_bpy_button():
    return genericCoordinatesCenter('mutl/calib_defect_solid_bpy')


def search_defect_solid_tomo_button():
    return genericCoordinatesCenter('mutl/calib_defect_solid_tomo')


def search_pixel_defect_button():
    return genericCoordinatesCenter('mutl/calib_pixel_defect')


def search_shading_button():
    return genericCoordinatesCenter('mutl/calib_shading')


def search_uniformity_button():
    return genericCoordinatesCenter('mutl/calib_uniformity')


def search_uniformity_stereo_button():
    return genericCoordinatesCenter('mutl/calib_uniformity_stereo')


def search_uniformity_bpy_button():
    return genericCoordinatesCenter('mutl/calib_uniformity_bpy')


def search_uniformity_tomo_button():
    return genericCoordinatesCenter('mutl/calib_uniformity_tomo')


def search_uniformity_ES_button():
    return genericCoordinatesCenter('mutl/calib_uniformity_es')


def search_sensitivity_button():
    return genericCoordinatesCenter('mutl/calib_sensitivity')
