from shell.MU import enable_calib_button
from shell.generic import openApp, process_exists, changeWindow
from util.location.RU_MUTL import *
from util.location.MCU import *
from util.misc import moveNclick

import customtkinter as ck


def openMUTLMCU():
    if process_exists('MUTL.exe'):
        return changeWindow('MCU0')
    openApp('MCU')


def openCalibrationMenu():
    # is MCU FIRST PAGE?
    x, y = MCU_page_0()
    if x > 0 and y > 0:
        # NO FIRST PAGE, CHANGE TO NEXT
        x, y = right()
        moveNclick(x, y)
    x, y = calibration()
    if x == 'selected':
        print('Already selected')
        return
    moveNclick(x, y)


def openCalibrationOptMenu():
    # is MCU FIRST PAGE?
    x, y = MCU_page_0()
    if x > 0 and y > 0:
        # NO FIRST PAGE, CHANGE TO NEXT
        x, y = right()
        moveNclick(x, y)
    # NO CALIB SELECTED
    x, y = calibrationOptional()
    if x == 'selected':
        print('Already selected')
        return
    moveNclick(x, y)


def click_offset_calib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = offset()
    moveNclick(x, y)


def click_defect_calib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = defect()
    moveNclick(x, y)


def click_defect_solid_calib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = defectSolid()
    moveNclick(x, y)
    enable_calib_button()


def click_pixel_defect_calib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = pixelDefect()
    moveNclick(x, y)
    enable_calib_button()


def click_shading_calib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = shading()
    moveNclick(x, y)
    enable_calib_button()


def click_uniformity_calib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = shading()
    moveNclick(x, y)
    enable_calib_button()


def click_defect_solid_stereo_calib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = defectSolidStereo()
    moveNclick(x, y)
    enable_calib_button()


def click_defect_solid_bpy_calib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = defectSolidBpy()
    moveNclick(x, y)
    enable_calib_button()


def click_defect_solid_tomo_calib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = defectSolidTomo()
    moveNclick(x, y)
    enable_calib_button()


def click_uniformity_stereo_calib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = offset()
    moveNclick(x, y)
    enable_calib_button()


def click_uniformity_bpy_calib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = uniformityBpy()
    moveNclick(x, y)
    enable_calib_button()


def click_uniformity_tomo_calib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = uniformityTomo()
    moveNclick(x, y)
    enable_calib_button()


def click_uniformity_es_calib():
    openMUTLMCU()
    openCalibrationMenu()
    x, y = uniformityES()
    moveNclick(x, y)
    enable_calib_button()
