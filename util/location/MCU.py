from util.location.generic import genericCoordinatesCenter, genericCoordinates
from util.CustomExceptions import IconNotFoundError, AlreadySelectedError


def search_MCU0_button() -> tuple[int, int]:
    try:
        x, y = genericCoordinatesCenter("ru/MCU0")
        return x, y
    except IconNotFoundError:
        pass
    try:
        x, y = genericCoordinatesCenter("ru/MCU0_S")
        return x, y
    except IconNotFoundError:
        raise IconNotFoundError("MCU BUTTON NOT FOUND")


def search_MCU_page_0() -> tuple[int, int]:
    try:
        x0, y0, w, h = genericCoordinates("mutl/MCU/mcua")
        x = int(x0 + w / 2)
        y = int(y0 + h / 2)
        return x, y
    except IconNotFoundError:
        raise IconNotFoundError("MCU PAGE 0 NOT FOUND")


def search_calibration_tab() -> tuple[int, int]:
    try:
        x0, y0, w, h = genericCoordinates("mutl/MCU/calibration_unselected")
        x = int(x0 + w / 2)
        y = int(y0 + h / 2)
        return x, y
    except IconNotFoundError:
        pass

    try:
        x0, y0, w, h = genericCoordinates("mutl/MCU/calibration_opt_selected")
        x = int(x0 + w / 2)
        y = int(y0 + h / 2)
        return x, y
    except IconNotFoundError:
        pass

    try:
        x0, y0, w, h = genericCoordinates("mutl/MCU/calibration_selected")
        raise AlreadySelectedError("CALIBRATION TAB ALREADY SELECTED")

    except IconNotFoundError:
        raise IconNotFoundError


def search_calibration_optional_tab() -> tuple[int, int]:
    try:
        x0, y0, w, h = genericCoordinates("mutl/MCU/calibration_selected")
        x = int(x0 + 4 * w / 5)
        y = int(y0 + h / 2)
        return x, y
    except IconNotFoundError:
        pass

    try:
        x0, y0, w, h = genericCoordinates("mutl/MCU/calibration_unselected")
        x = int(x0 + (4 * w / 5))
        y = int(y0 + h / 2)
        return x, y
    except IconNotFoundError:
        pass

    try:
        x0, y0, w, h = genericCoordinates("mutl/MCU/calibration_opt_selected")
        raise AlreadySelectedError("CALIBRATION TAB ALREADY SELECTED")
    except IconNotFoundError:
        raise IconNotFoundError


# CALIBRATION MENU
def search_offset_button():
    return genericCoordinatesCenter("mutl/calib_offset")


def search_defect_button():
    return genericCoordinatesCenter("mutl/calib_defect")


def search_defect_solid_button():
    return genericCoordinatesCenter("mutl/calib_defect_solid")


def search_defect_solid_stereo_button():
    return genericCoordinatesCenter("mutl/calib_defect_solid_stereo")


def search_defect_solid_bpy_button():
    return genericCoordinatesCenter("mutl/calib_defect_solid_bpy")


def search_defect_solid_tomo_button():
    return genericCoordinatesCenter("mutl/calib_defect_solid_tomo")


def search_pixel_defect_button():
    return genericCoordinatesCenter("mutl/calib_pixel_defect")


def search_shading_button():
    return genericCoordinatesCenter("mutl/calib_shading")


def search_uniformity_button():
    return genericCoordinatesCenter("mutl/calib_uniformity")


def search_uniformity_stereo_button():
    return genericCoordinatesCenter("mutl/calib_uniformity_stereo")


def search_uniformity_bpy_button():
    return genericCoordinatesCenter("mutl/calib_uniformity_bpy")


def search_uniformity_tomo_button():
    return genericCoordinatesCenter("mutl/calib_uniformity_tomo")


def search_uniformity_ES_button():
    return genericCoordinatesCenter("mutl/calib_uniformity_es")


def search_sensitivity_button():
    return genericCoordinatesCenter("mutl/calib_sensitivity")
