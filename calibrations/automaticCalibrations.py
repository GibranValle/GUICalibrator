from shell.MCU import *
from calibrations.allExposureNeeded import allRequired
from time import sleep


def startAutomaticCalib(gui_object: ck.CTk = None):
    grand_total = 0
    options = gui_object.selected
    text1 = f'Stabilizing...'
    text2 = f'Please wait...'
    gui_object.generic.edit_output(text1, text2)

    for option in options:
        if gui_object.delay.status == 'stop':
            break

        print(option)
        sleep(2)

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
    gui_object.generic.exposure_done(grand_total, 'selection')
    gui_object.auto.pushed('stop')


def noExposureCalibration(name, gui_object: ck.CTk = None, duration=600):
    total = 0
    gui = gui_object
    print('NO EXPOSURE CALIB')
    gui.generic.clear_output()

    text1 = f'{name} calib starting...'
    text2 = f'Wait for calib signal'
    gui.generic.edit_output(text1, text2)
    time = gui.delay.wait_for_calib_signal(1, duration)
    if time < 0:
        print('aborted')
        text1 = f'{name} calib aborting...'
        text2 = f'Please retry'
        gui.generic.edit_output(text1, text2)
        return
    total += time

    text1 = f'{name} calib running...'
    text2 = f'Wait for pass signal'
    gui.generic.edit_output(text1, text2)
    time = gui.delay.wait_for_calib_pass(1, duration)
    if time < 0:
        print('aborted')
        text1 = f'{name} calib aborting...'
        text2 = f'Please retry'
        gui.generic.edit_output(text1, text2)
        return
    total += time
    gui.generic.exposure_done_counter(total, 0)
    return total


def exposureCalibration(name, gui_object: ck.CTk = None, duration=600):
    gui = gui_object
    print('EXPOSURE CALIB')
    total = 0

    text1 = f'{name} calib starting...'
    text2 = f'Wait for calib signal'
    gui.generic.edit_output(text1, text2)
    time = gui.delay.wait_for_calib_signal(1, duration)
    if time < 0:
        print('aborted')
        text1 = f'{name} calib aborting...'
        text2 = f'Please retry'
        gui.generic.edit_output(text1, text2)
        return
    total += time
    time = allRequired(gui_object)
    if time < 0:
        print('aborted')
        text1 = f'{name} calib aborting...'
        text2 = f'Please retry'
        gui.generic.edit_output(text1, text2)
        return
    total += time
    return total


def offsetCalib(gui_object: ck.CTk = None):
    gui_object.generic.edit_output('Offset calib', 'Please wait')
    click_offset_calib()
    total = noExposureCalibration('offset', gui_object, duration=600)
    return total


def defectCalib(gui_object: ck.CTk = None):
    gui_object.generic.edit_output('Defect calib', 'Please wait')
    click_defect_calib()
    total = noExposureCalibration('defect', gui_object, duration=600)
    return total


def defectSolidCalib(gui_object: ck.CTk = None):
    gui_object.generic.edit_output('Defect Solid calib', 'Please wait')
    click_defect_solid_calib()
    total = exposureCalibration(gui_object)
    return total


def pixedDefectCalib(gui_object: ck.CTk = None):
    gui_object.generic.edit_output('Pixel Defect calib', 'Please wait')
    click_pixel_defect_calib()
    total = exposureCalibration(gui_object)
    return total


def shadingCalib(gui_object: ck.CTk = None):
    gui_object.generic.edit_output('Shading calib', 'Please wait')
    click_shading_calib()
    total = exposureCalibration(gui_object)
    return total


def uniformityCalib(gui_object: ck.CTk = None):
    gui_object.generic.edit_output('Uniformity calib', 'Please wait')
    click_uniformity_calib()
    total = exposureCalibration(gui_object)
    return total


def defectSolidStereoCalib(gui_object: ck.CTk = None):
    gui_object.generic.edit_output('Defect Solid Stereo calib', 'Please wait')
    click_defect_solid_stereo_calib()
    total = exposureCalibration(gui_object)
    return total


def defectSolidBpyCalib(gui_object: ck.CTk = None):
    gui_object.generic.edit_output('Defect Solid Bpy calib', 'Please wait')
    click_defect_solid_bpy_calib()
    total = exposureCalibration(gui_object)
    return total


def defectSolidTomoCalib(gui_object: ck.CTk = None):
    gui_object.generic.edit_output('Defect Solid Tomo calib', 'Please wait')
    click_defect_solid_tomo_calib()
    total = exposureCalibration(gui_object)
    return total


def uniformityCalibStereo(gui_object: ck.CTk = None):
    gui_object.generic.edit_output('Uniformity stereo calib', 'Please wait')
    click_uniformity_stereo_calib()
    total = exposureCalibration(gui_object)
    return total


def uniformityCalibBpy(gui_object: ck.CTk = None):
    gui_object.generic.edit_output('Uniformity Bpy calib', 'Please wait')
    click_uniformity_bpy_calib()
    total = exposureCalibration(gui_object)
    return total


def uniformityCalibTomo(gui_object: ck.CTk = None):
    gui_object.generic.edit_output('Uniformity Tomo calib', 'Please wait')
    click_uniformity_tomo_calib()
    total = exposureCalibration(gui_object)
    return total


def uniformityCalibES(gui_object: ck.CTk = None):
    gui_object.generic.edit_output('Uniformity ES calib', 'Please wait')
    click_uniformity_es_calib()
    total = exposureCalibration(gui_object)
    return total
