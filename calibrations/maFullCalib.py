from exposures.smart_exposure import smart_exposure_loop


def mAFullCalibration(gui_object):
    exposures = 1
    countdown = 10
    smart_exposure_loop(gui_object, exposures, countdown)
