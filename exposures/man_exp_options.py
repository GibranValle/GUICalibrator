from exposures.smart_exposure import smart_exposure_loop


def singleShot(gui_object=None):
    exposures = 1
    start_smart_exposure(gui_object, exposures, 'manual')


def TenShots(gui_object=None):
    exposures = 10
    start_smart_exposure(gui_object, exposures, 'manual')


def start_smart_exposure(gui_object=None, exposures=100, calib_type='auto'):
    return smart_exposure_loop(gui_object, exposures, calib_type=calib_type)
