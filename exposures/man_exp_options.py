from exposures.smart_exposure import smart_exposure_loop
from classes.constants import CALIB_TYPE
from typing import Any


def singleShot(gui_object: Any):
    exposures: int = 1
    start_smart_exposure(gui_object, exposures, "manual")


def TenShots(gui_object: Any):
    exposures = 10
    start_smart_exposure(gui_object, exposures, "manual")


def start_smart_exposure(
    gui_object: Any, exposures: int = 100, calib_type: CALIB_TYPE = "auto"
):
    return smart_exposure_loop(gui_object, exposures, calib_type=calib_type)
