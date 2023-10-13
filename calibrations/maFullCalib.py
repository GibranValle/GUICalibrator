from exposures.smart_exposure import smart_exposure_loop
from typing import Any


def mAFullCalibration(gui_object: Any) -> None:
    smart_exposure_loop(gui_object, calib_type="ma_calib")
