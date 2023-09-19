import customtkinter as ck
from shell.MCU import *
from calibrations.allExposureNeeded import allRequired


def startAutomaticCalib(gui_object: ck.CTk = None):
    options = gui_object.selected
    for option in options:
        print(option)
        if option == 'offset':
            offsetCalib(gui_object)
        elif option == 'defect':
            defectCalib(gui_object)
        elif option == 'defect solid':
            defectSolidCalib(gui_object)
        elif option == 'pixel defect':
            pixedDefectCalib(gui_object)
        elif option == 'shading':
            shadingCalib(gui_object)
        elif option == 'uniformity':
            uniformityCalib(gui_object)
        elif option == 'defect solid stereo':
            defectSolidStereoCalib(gui_object)
        elif option == 'defect solid biopsy':
            defectSolidBpyCalib(gui_object)
        elif option == 'defect solid tomo':
            defectSolidTomoCalib(gui_object)
        elif option == 'x-ray uniformity stereo':
            uniformityCalibStereo(gui_object)
        elif option == 'x-ray uniformity biopsy':
            uniformityCalibBpy(gui_object)
        elif option == 'x-ray uniformity tomo':
            uniformityCalibTomo(gui_object)
        elif option == 'x-ray uniformity ES':
            uniformityCalibES(gui_object)


def noExposureCalibration(name, gui_object: ck.CTk = None, duration=600):
    gui = gui_object
    print('NO EXPOSURE CALIB')
    gui.delay.startStatus()
    gui.generic.clear_output()
    total = 0
    text1 = f'{name} calib running'
    text2 = f'Wait for pass signal'
    gui.generic.edit_output(text1, text2)
    total += gui.delay.waitTillPass(1, duration)
    gui.generic.exposure_done_exp(total, 0)


def offsetCalib(gui_object: ck.CTk = None):
    gui_object.generic.edit_output('Offset calib', 'Please wait')
    click_offset_calib()
    noExposureCalibration('offset', gui_object, duration=600)


def defectCalib(gui_object: ck.CTk = None):
    gui_object.generic.edit_output('Defect calib', 'Please wait')
    click_defect_calib()
    noExposureCalibration('defect', gui_object, duration=600)


def defectSolidCalib(gui_object: ck.CTk = None):
    gui_object.generic.edit_output('Defect Solid calib', 'Please wait')
    click_defect_solid_calib()
    allRequired(gui_object)


def pixedDefectCalib(gui_object: ck.CTk = None):
    gui_object.generic.edit_output('Pixel Defect calib', 'Please wait')
    click_pixel_defect_calib()
    allRequired(gui_object)


def shadingCalib(gui_object: ck.CTk = None):
    gui_object.generic.edit_output('Shading calib', 'Please wait')
    click_shading_calib()
    allRequired(gui_object)


def uniformityCalib(gui_object: ck.CTk = None):
    gui_object.generic.edit_output('Uniformity calib', 'Please wait')
    click_uniformity_calib()
    allRequired(gui_object)


def defectSolidStereoCalib(gui_object: ck.CTk = None):
    gui_object.generic.edit_output('Defect Solid Stereo calib', 'Please wait')
    click_defect_solid_stereo_calib()
    allRequired(gui_object)


def defectSolidBpyCalib(gui_object: ck.CTk = None):
    gui_object.generic.edit_output('Defect Solid Bpy calib', 'Please wait')
    click_defect_solid_bpy_calib()
    allRequired(gui_object)


def defectSolidTomoCalib(gui_object: ck.CTk = None):
    gui_object.generic.edit_output('Defect Solid Tomo calib', 'Please wait')
    click_defect_solid_tomo_calib()
    allRequired(gui_object)


def uniformityCalibStereo(gui_object: ck.CTk = None):
    gui_object.generic.edit_output('Uniformity stereo calib', 'Please wait')
    click_uniformity_stereo_calib()
    allRequired(gui_object)


def uniformityCalibBpy(gui_object: ck.CTk = None):
    gui_object.generic.edit_output('Uniformity Bpy calib', 'Please wait')
    click_uniformity_bpy_calib()
    allRequired(gui_object)


def uniformityCalibTomo(gui_object: ck.CTk = None):
    gui_object.generic.edit_output('Uniformity Tomo calib', 'Please wait')
    click_uniformity_tomo_calib()
    allRequired(gui_object)


def uniformityCalibES(gui_object: ck.CTk = None):
    gui_object.generic.edit_output('Uniformity ES calib', 'Please wait')
    click_uniformity_es_calib()
    allRequired(gui_object)
