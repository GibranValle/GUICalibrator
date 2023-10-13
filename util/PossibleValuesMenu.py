from typing import Literal

VALID_CALIBRATION_NAMES = Literal[
    "offset",
    "defect",
    "defect solid",
    "pixel defect",
    "shading",
    "x-ray uniformity",
    "defect solid stereo",
    "defect solid biopsy",
    "defect solid tomo",
    "x-ray uniformity stereo",
    "x-ray uniformity biopsy",
    "x-ray uniformity tomo",
    "x-ray uniformity ES",
]
