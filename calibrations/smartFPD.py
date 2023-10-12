from exposures.man_exp_options import start_smart_exposure


def smart_FPD_calibration(name: str, gui_object=None, duration=600):
    print('SMART FPD CALIB')
    gui = gui_object
    total = 0
    gui.generic.edit_title(f'{name} calib starting...')

    try:
        total += gui.delay.wait_for_calib_signal(1, duration)
        total += start_smart_exposure(gui_object)
    except ValueError:
        return gui.generic.abnormal()
    except TypeError:
        return gui.generic.abnormal()
    return total
