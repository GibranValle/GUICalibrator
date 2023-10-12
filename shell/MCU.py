from shell.generic import openApp, process_exists, changeWindow
from util.location.RU_MUTL import *
from util.location.MCU import *
from util.misc import moveNclick
from util.menu_list import no_exp_menu, exp_calib_menu, only_full_menu, ES_menu, full_menu
from util.PossibleValuesMenu import PossibleValuesMenu, list_values


def openMUTLMCU():
    if process_exists('MUTL.exe'):
        changeWindow('MCU0')
        return
    printError('MUTL.exe not running')
    openApp('MCU')


def openCalibrationMenu():
    # is MCU FIRST PAGE?
    x, y = search_MCU_page_0()
    if x > 0 and y > 0:
        # NO FIRST PAGE, CHANGE TO NEXT
        x, y = right()
        moveNclick(x, y)
    x, y = search_calibration_tab()
    if x == 'selected':
        print('Already selected')
        return
    moveNclick(x, y)


def openCalibrationOptMenu():
    # is MCU FIRST PAGE?
    x, y = search_MCU_page_0()
    if x > 0 and y > 0:
        # NO FIRST PAGE, CHANGE TO NEXT
        x, y = right()
        moveNclick(x, y)
    # NO CALIB SELECTED
    x, y = search_calibration_optional_tab()
    if x == 'selected':
        print('Already selected')
        return
    moveNclick(x, y)


def click_mcu_calib_button(button: list_values):
    openMUTLMCU()
    openCalibrationMenu()
    if button == 'offset':
        x, y = search_offset_button()
    elif button == 'defect':
        x, y = search_defect_button()
    elif button == 'defect solid':
        x, y = search_defect_solid_button()
    elif button == 'text':

    moveNclick(x, y)


def click_defect_solid_calib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = search_defect_solid_button()
    moveNclick(x, y)


def click_pixel_defect_calib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = search_pixel_defect_button()
    moveNclick(x, y)


def click_shading_calib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = search_shading_button()
    moveNclick(x, y)


def click_uniformity_calib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = search_shading_button()
    moveNclick(x, y)


def click_defect_solid_stereo_calib():
    openMUTLMCU()
    openCalibrationOptMenu()
    x, y = search_defect_solid_stereo_button()
    moveNclick(x, y)


def click_defect_solid_bpy_calib():
    openMUTLMCU()
    openCalibrationOptMenu()
    x, y = search_defect_solid_Bpy()
    moveNclick(x, y)


def click_defect_solid_tomo_calib():
    openMUTLMCU()
    openCalibrationOptMenu()
    x, y = search_defect_solid_tomo_button()
    moveNclick(x, y)


def click_uniformity_stereo_calib():
    openMUTLMCU()
    openCalibrationOptMenu()
    x, y = search_offset_button()
    moveNclick(x, y)


def click_uniformity_bpy_calib():
    openMUTLMCU()
    openCalibrationOptMenu()
    x, y = search_uniformity_bpy_button()
    moveNclick(x, y)


def click_uniformity_tomo_calib():
    openMUTLMCU()
    openCalibrationOptMenu()
    x, y = search_uniformity_tomo_button()
    moveNclick(x, y)


def click_uniformity_es_calib():
    openMUTLMCU()
    openCalibrationOptMenu()
    x, y = search_uniformity_ES_button()
    moveNclick(x, y)
