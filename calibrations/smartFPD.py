from exposures.exposure_options import start_smart_exposure


def smart_FPD_calibration(name: str, gui_object=None, duration=600):
    gui = gui_object
    total = 0
    gui.generic.edit_title(f'{name} calib starting...')

    time = gui.delay.wait_for_calib_signal(1, duration)
    if time < 0:
        return gui.generic.abort_requested()
    total += time

    time = start_smart_exposure(gui_object)
    if time < 0:
        return gui.generic.abort_requested()
    total += time
    return total

