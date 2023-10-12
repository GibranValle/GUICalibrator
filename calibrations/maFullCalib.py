from exposures.smart_exposure import smart_exposure_loop


def mAFullCalibration(gui_object):
    smart_exposure_loop(gui_object, calib_type='ma_calib')
