class MenuList:
    manual_menu = "Single Shot", "mA full calib shot", "10 shots", "All needed (FPD)"
    auto_menu = "Calibration", "Opt Calibrations"
    no_exp_menu = ["offset", "defect"]
    exp_calib_menu = [
        "defect solid",
        "pixel defect",
        "shading",
        "uniformity",
    ]  # 'sensitivity'

    basic_menu: list[str] = []
    basic_menu.extend(no_exp_menu)
    basic_menu.extend(exp_calib_menu)

    only_full_menu = [
        "defect solid stereo",
        "defect solid biopsy",
        "defect solid tomo",
        "x-ray uniformity stereo",
        "x-ray uniformity biopsy",
        "x-ray uniformity tomo",
    ]
    ES_menu = ["x-ray uniformity ES"]

    calib_menu: list[str] = []
    calib_menu.extend(no_exp_menu)
    calib_menu.extend(exp_calib_menu)

    calib_opt_menu: list[str] = []
    calib_opt_menu.extend(only_full_menu)
    calib_opt_menu.extend(ES_menu)

    only_tomo_menu = ["defect solid tomo", "x-ray uniformity tomo"]
    tomo_menu: list[str] = []
    tomo_menu.extend(basic_menu)
    tomo_menu.extend(only_tomo_menu)

    full_menu: list[str] = []
    full_menu.extend(basic_menu)
    full_menu.extend(only_full_menu)

    CALIB_MENU = basic_menu
    OPT_CALIB_MENU = calib_opt_menu
