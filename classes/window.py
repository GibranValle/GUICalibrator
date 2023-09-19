from util.location.AWS import *
from shell.RU_MUTL import *
from shell.MCU import *
from shell.MU import *
from util.misc import moveNclick, moveN2Click


def windowOptions(option):
    print(option)
    if option == 'Ok red':
        x, y = okExposure()
        moveNclick(x, y)

    elif option == 'Calib button':
        x, y = calib_button()
        moveN2Click(x, y)

    elif option == 'Field calib button':
        enable_calib_button()

    elif option == 'Open RU':
        openRU()

    elif option == 'Close RU':
        closeRU()

    elif option == 'Open MUTL MU':
        openMUTLMU()

    elif option == 'Open MUTL MCU':
        openMUTLMCU()

    elif option == 'Close MUTL':
        closeMUTL()

    elif option == 'Toggle HVL':
        toggle_HVL()

    elif option == 'Toggle MAG':
        toggle_MAG()

    elif option == 'Enable Ment Mode':
        enable_ment()

    elif 'offset' in option:
        click_offset_calib()

    elif 'defect' in option:
        click_defect_calib()

    elif 'defect solid' in option:
        click_defect_calib()

    elif 'pixel defect' in option:
        click_pixel_defect_calib()

    elif 'shading' in option:
        click_shading_calib()

    elif 'uniformity' in option:
        click_uniformity_calib()

    elif 'defect solid stereo' in option:
        click_defect_solid_calib()

    elif 'defect solid biopsy' in option:
        click_defect_solid_bpy_calib()

    elif 'defect solid tomo' in option:
        click_defect_solid_tomo_calib()

    elif 'x-ray uniformity stereo' in option:
        click_uniformity_stereo_calib()

    elif 'x-ray uniformity biopsy' in option:
        click_uniformity_bpy_calib()

    elif 'x-ray uniformity tomo' in option:
        click_uniformity_tomo_calib()

    elif 'x-ray uniformity ES' in option:
        click_uniformity_es_calib()
