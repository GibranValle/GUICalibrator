from exposures.smart_exposure import smart_exposure_loop


def singleShot(gui_object=None):
    exposures = 1
    start_smart_exposure(gui_object, exposures)


def TenShots(gui_object=None):
    exposures = 10
    start_smart_exposure(gui_object, exposures)


def start_smart_exposure(gui_object=None, exposures=100):
    return smart_exposure_loop(gui_object, exposures)
