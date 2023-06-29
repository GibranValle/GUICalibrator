#      0             1                  2         3         4                       5                      6            7          8           9
menu = 'Basic FPD', 'Stereo Bpy FPD', 'Tomo FPD', 'ES FPD', 'mA full Calibration', 'IconLocation[Test]', 'Save MACs', 'Window', 'Single Shot', 'Create WOL file'

basic = 'Defect-solid', 'Pixel-defect', 'Shading', 'X-ray uniformity'

stereo = 'Defect-solid (Stereo)', 'Defect-solid (Bpy)', 'X-ray uniformity (Stereo)', 'X-ray uniformity (Bpy)'

tomo = 'Defect-solid (Tomo)', 'X-ray uniformity (Tomo)'

es = ['X-ray uniformity (ES)']

icons_menu = 'AWS status icons', 'RUPCTools icons', 'MUTL icons', 'FPD Calib icons', 'FPD Calib Opt icons'
icons_aws = 'Stand by', 'Blocked', 'Ok red', 'Calib button', 'Field calib button'
icons_RU = 'MU0', 'MCU0', 'New', 'Install'
icons_mutl = 'calibration', 'calibration (opt)', 'left', 'right',
icons_calib = 'offset', 'defect', 'defect solid', 'pixel defect', 'shading', 'uniformity', 'sensitivity'
icons_calib_opt = 'defect solid stereo', 'defect solid biopsy', 'defect solid tomo', 'x-ray uniformity stereo', \
    'x-ray uniformity biopsy', 'x-ray uniformity tomo', 'x-ray uniformity ES'

window = 'RUPCTools', 'MUTL MU', 'Calibration', 'Calibration Optional'
w_ru = 'Open RU', 'Close RU', 'Open MUTL MU', 'Open MUTL MCU', 'Close MUTL'
w_mu = 'Enable HVL', 'Enable MAG', 'Enable Ment Mode'
w_calibration = [f'Start {icon} Calib' for icon in icons_calib]
w_calibration_opt = [f'Start {icon} Calib' for icon in icons_calib_opt]

