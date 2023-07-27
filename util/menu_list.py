only_menu = 'mA Full', 'Single shot', '10 Shots'
with_output = 'Save MAC', 'Create WOL file'
with_submenu = 'Basic', 'Stereo', 'Tomo', 'ES',
with_submenu_lastmenu = ['Window']
mode = []
mode.extend(only_menu)
mode.extend(with_output)
mode.extend(with_submenu)
mode.extend(with_submenu_lastmenu)

# submodes
basic = 'Defect-solid', 'Pixel-defect', 'Shading', 'X-ray uniformity'
stereo = 'Defect-solid (Stereo)', 'Defect-solid (Bpy)', 'X-ray uniformity (Stereo)', 'X-ray uniformity (Bpy)'
tomo = 'Defect-solid (Tomo)', 'X-ray uniformity (Tomo)'
es = ['X-ray uniformity (ES)']

icons_calib = 'offset', 'defect', 'defect solid', 'pixel defect', 'shading', 'uniformity'  # 'sensitivity'
icons_calib_opt = 'defect solid stereo', 'defect solid biopsy', 'defect solid tomo', 'x-ray uniformity stereo', \
    'x-ray uniformity biopsy', 'x-ray uniformity tomo', 'x-ray uniformity ES'

window = 'AWS', 'RUPCTools', 'MUTL MU', 'MUTL MCU'
w_aws = 'Ok red', 'Calib button', 'Field calib button'
w_ru = 'Open RU', 'Close RU', 'Open MUTL MU', 'Open MUTL MCU', 'Close MUTL'
w_mutl = 'Toggle HVL', 'Toggle MAG', 'Enable Ment Mode'
w_calibration = [f'Start {icon} Calib' for icon in icons_calib]
w_calibration_opt = [f'Start {icon} Calib' for icon in icons_calib_opt]
w_mutl_mcu = []
w_mutl_mcu.extend(w_calibration)
w_mutl_mcu.extend(w_calibration_opt)


# NEW ITERATION
manual_menu = 'Single Shot', 'mA full calib shot', '10 shots', 'All requested (FPD)'
auto_menu = 'Calibration', 'Opt Calibrations'
utils_menu = 'Save MAC', 'Create WOL file'
calib_menu = 'offset', 'defect', 'defect solid', 'pixel defect', 'shading', 'uniformity'  # 'sensitivity'
calib_opt_menu = 'defect solid stereo', 'defect solid biopsy', 'defect solid tomo', 'x-ray uniformity stereo', \
    'x-ray uniformity biopsy', 'x-ray uniformity tomo', 'x-ray uniformity ES'
