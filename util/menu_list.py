#      0             1                  2         3         4                       5                      6            7          8           9
# mode = 'ma Full', 'Single shot', 'Save MAC', 'Create WOL file', 'Basic', 'Stereo', 'TOMO', 'ES', 'IconFinder', 'Window'
with_menu = 'ma Full', 'Single shot'
with_menu_output = 'Save MAC', 'Create WOL file'
with_submenu =  'Basic', 'Stereo', 'Tomo', 'ES',
with_lastmenu = 'IconFinder', 'Window'
mode = []
mode.extend(with_menu)
mode.extend(with_menu_output)
mode.extend(with_submenu)
mode.extend(with_lastmenu)


basic = 'Defect-solid', 'Pixel-defect', 'Shading', 'X-ray uniformity'

stereo = 'Defect-solid (Stereo)', 'Defect-solid (Bpy)', 'X-ray uniformity (Stereo)', 'X-ray uniformity (Bpy)'

tomo = 'Defect-solid (Tomo)', 'X-ray uniformity (Tomo)'

es = ['X-ray uniformity (ES)']

icons = 'AWS', 'RUPCTools', 'MUTL MU', 'Calibration', 'Calibration Opt'
icons_aws = 'Stand by', 'Blocked', 'Ok red', 'Calib button', 'Field calib button'
icons_RU = 'MU0', 'MCU0', 'New', 'Install'
icons_mutl = 'calibration', 'calibration (opt)', 'left', 'right',
icons_calib = 'offset', 'defect', 'defect solid', 'pixel defect', 'shading', 'uniformity', 'sensitivity'
icons_calib_opt = 'defect solid stereo', 'defect solid biopsy', 'defect solid tomo', 'x-ray uniformity stereo', \
    'x-ray uniformity biopsy', 'x-ray uniformity tomo', 'x-ray uniformity ES'

window = icons
w_aws = 'Ok red', 'Calib button', 'Field calib button'
w_ru = 'Open RU', 'Close RU', 'Open MUTL MU', 'Open MUTL MCU', 'Close MUTL'
w_mutl = 'Enable HVL', 'Enable MAG', 'Enable Ment Mode'
w_calibration = [f'Start {icon} Calib' for icon in icons_calib]
w_calibration_opt = [f'Start {icon} Calib' for icon in icons_calib_opt]

