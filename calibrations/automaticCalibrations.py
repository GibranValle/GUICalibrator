from shell.MCU import *
from time import sleep
from shell.AWS import enable_FPD_calib
from calibrations.noExposure import noExposureCalibration
from calibrations.smartFPD import smart_FPD_calibration


def autoCalibLoop(gui_object=None):
    grand_total = 0
    options = gui_object.selected
    gui_object.generic.stabilizing()

    for option in options:
        if gui_object.delay.status == 'stop':
            break
        try:
            if option == 'offset':
                grand_total += offsetCalib(gui_object)
            elif option == 'defect':
                grand_total += defectCalib(gui_object)
            elif option == 'defect solid':
                grand_total += defectSolidCalib(gui_object)
            elif option == 'pixel defect':
                grand_total += pixedDefectCalib(gui_object)
            elif option == 'shading':
                grand_total += shadingCalib(gui_object)
            elif option == 'uniformity':
                grand_total += uniformityCalib(gui_object)
            elif option == 'defect solid stereo':
                grand_total += defectSolidStereoCalib(gui_object)
            elif option == 'defect solid biopsy':
                grand_total += defectSolidBpyCalib(gui_object)
            elif option == 'defect solid tomo':
                grand_total += defectSolidTomoCalib(gui_object)
            elif option == 'x-ray uniformity stereo':
                grand_total += uniformityCalibStereo(gui_object)
            elif option == 'x-ray uniformity biopsy':
                grand_total += uniformityCalibBpy(gui_object)
            elif option == 'x-ray uniformity tomo':
                grand_total += uniformityCalibTomo(gui_object)
            elif option == 'x-ray uniformity ES':
                grand_total += uniformityCalibES(gui_object)
        except TypeError:
            printError('CALIBRATION NOT INITIATED')
    if grand_total < 0:
        gui_object.generic.abnormal()
        gui_object.auto.pushed('stop')
        return
    gui_object.generic.end_exp_msg(grand_total, 'selection')
    gui_object.auto.pushed('stop')


def offsetCalib(gui_object=None):
    gui_object.generic.edit_output('Offset calib', 'Please wait')
    click_offset_calib()
    enable_FPD_calib()
    return noExposureCalibration('offset', gui_object, duration=600)


def defectCalib(gui_object=None):
    gui_object.generic.edit_output('Defect calib', 'Please wait')
    click_defect_calib()
    enable_FPD_calib()
    return noExposureCalibration('defect', gui_object, duration=600)


def defectSolidCalib(gui_object=None):
    gui_object.generic.edit_output('Defect Solid calib', 'Please wait')
    click_defect_solid_calib()
    enable_FPD_calib()
    return smart_FPD_calibration('defect solid', gui_object)


def pixedDefectCalib(gui_object=None):
    gui_object.generic.edit_output('Pixel Defect calib', 'Please wait')
    click_pixel_defect_calib()
    enable_FPD_calib()
    return smart_FPD_calibration('pixel defect', gui_object)


def shadingCalib(gui_object=None):
    gui_object.generic.edit_output('Shading calib', 'Please wait')
    click_shading_calib()
    enable_FPD_calib()
    return smart_FPD_calibration('shading', gui_object)


def uniformityCalib(gui_object=None):
    gui_object.generic.edit_output('Uniformity calib', 'Please wait')
    click_uniformity_calib()
    enable_FPD_calib()
    return smart_FPD_calibration('uniformity', gui_object)


def defectSolidStereoCalib(gui_object=None):
    gui_object.generic.edit_output('Defect Solid Stereo calib', 'Please wait')
    click_defect_solid_stereo_calib()
    enable_FPD_calib()
    return smart_FPD_calibration('defect solid stereo', gui_object)


def defectSolidBpyCalib(gui_object=None):
    gui_object.generic.edit_output('Defect Solid Bpy calib', 'Please wait')
    click_defect_solid_bpy_calib()
    enable_FPD_calib()
    return smart_FPD_calibration('defect solid bpy', gui_object)


def defectSolidTomoCalib(gui_object=None):
    gui_object.generic.edit_output('Defect Solid Tomo calib', 'Please wait')
    click_defect_solid_tomo_calib()
    enable_FPD_calib()
    return smart_FPD_calibration('defect solid tomo', gui_object)


def uniformityCalibStereo(gui_object=None):
    gui_object.generic.edit_output('Uniformity stereo calib', 'Please wait')
    click_uniformity_stereo_calib()
    enable_FPD_calib()
    return smart_FPD_calibration('x-ray uniformity stereo', gui_object)


def uniformityCalibBpy(gui_object=None):
    gui_object.generic.edit_output('Uniformity Bpy calib', 'Please wait')
    click_uniformity_bpy_calib()
    enable_FPD_calib()
    return smart_FPD_calibration('x-ray uniformity bpy', gui_object)


def uniformityCalibTomo(gui_object=None):
    gui_object.generic.edit_output('Uniformity Tomo calib', 'Please wait')
    click_uniformity_tomo_calib()
    enable_FPD_calib()
    return smart_FPD_calibration('x-ray uniformity tomo', gui_object)


def uniformityCalibES(gui_object=None):
    gui_object.generic.edit_output('Uniformity ES calib', 'Please wait')
    click_uniformity_es_calib()
    enable_FPD_calib()
    return smart_FPD_calibration('x-ray uniformity ES', gui_object)
