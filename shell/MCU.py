from shell.generic import changeWindow, openApp, process_exists
from util.PossibleValuesMenu import VALID_CALIBRATION_NAMES
from util.location.MCU import (
    search_MCU_page_0,
    search_calibration_optional_tab,
    search_calibration_tab,
    search_defect_button,
    search_defect_solid_bpy_button,
    search_defect_solid_button,
    search_defect_solid_stereo_button,
    search_defect_solid_tomo_button,
    search_offset_button,
    search_pixel_defect_button,
    search_shading_button,
    search_uniformity_ES_button,
    search_uniformity_bpy_button,
    search_uniformity_button,
    search_uniformity_stereo_button,
    search_uniformity_tomo_button,
)
from util.location.RU_MUTL import right
from util.misc import click_move, printError
from util.menu_list import MenuList
from util.CustomExceptions import IconNotFoundError, AlreadySelectedError

CALIB_MENU = MenuList.basic_menu
OPT_CALIB_MENU = MenuList.calib_opt_menu


def open_MUTL_MCU():
    if process_exists("MUTL.exe"):
        changeWindow("MCU0")
        return
    printError("MUTL.exe not running")
    openApp("MCU")


def open_calibration_menu():
    try:
        x, y = search_MCU_page_0()
        x, y = right()
    except IconNotFoundError:
        pass

    try:
        x, y = search_calibration_tab()
        click_move(x, y)
    except AlreadySelectedError:
        return
    except IconNotFoundError:
        raise IconNotFoundError("CALIB TAB NOT FOUND")


def openCalibrationOptMenu():
    try:
        x, y = search_MCU_page_0()
        x, y = right()
    except IconNotFoundError:
        pass

    try:
        x, y = search_calibration_optional_tab()
        click_move(x, y)
    except AlreadySelectedError:
        return
    except IconNotFoundError:
        raise IconNotFoundError("CALIB OPT TAB NOT FOUND")


def click_mcu_calib_button(button: VALID_CALIBRATION_NAMES):
    """
    :param button: name of the button to push
    """
    open_MUTL_MCU()
    try:
        if button in CALIB_MENU:
            open_calibration_menu()
        elif button in OPT_CALIB_MENU:
            open_calibration_menu()
        if button == "offset":
            x, y = search_offset_button()
        elif button == "defect":
            x, y = search_defect_button()
        elif button == "defect solid":
            x, y = search_defect_solid_button()
        elif button == "pixel defect":
            x, y = search_pixel_defect_button()
        elif button == "shading":
            x, y = search_shading_button()
        elif button == "x-ray uniformity":
            x, y = search_uniformity_button()
        elif button == "defect solid stereo":
            x, y = search_defect_solid_stereo_button()
        elif button == "defect solid biopsy":
            x, y = search_defect_solid_bpy_button()
        elif button == "defect solid tomo":
            x, y = search_defect_solid_tomo_button()
        elif button == "x-ray uniformity stereo":
            x, y = search_uniformity_stereo_button()
        elif button == "x-ray uniformity biopsy":
            x, y = search_uniformity_bpy_button()
        elif button == "x-ray uniformity tomo":
            x, y = search_uniformity_tomo_button()
        elif button == "x-ray uniformity ES":
            x, y = search_uniformity_ES_button()
        click_move(x, y)
    except IconNotFoundError:
        return
