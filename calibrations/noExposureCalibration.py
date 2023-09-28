from util.misc import printSuccess
import customtkinter as ck


def noExposureCalibration(name, gui_object: ck.CTk = None, duration=600):
    total = 0
    gui = gui_object
    print('NO EXPOSURE CALIB')
    gui.generic.clear_output()

    text1 = f'{name} calib starting...'
    text2 = f'Wait for calib signal'
    gui.generic.edit_output(text1, text2)
    time = gui.delay.wait_for_calib_signal(1, duration)
    if time < 0:
        print('aborted')
        text1 = f'{name} calib aborting...'
        text2 = f'Please retry'
        gui.generic.edit_output(text1, text2)
        return
    total += time
    printSuccess('CALIBRATION SIGNAL FOUND!')

    text1 = f'{name} calib running...'
    text2 = f'Wait for pass signal'
    gui.generic.edit_output(text1, text2)
    time = gui.delay.wait_for_calib_pass(1, duration)
    if time < 0:
        print('aborted')
        text1 = f'{name} calib aborting...'
        text2 = f'Please retry'
        gui.generic.edit_output(text1, text2)
        return
    total += time
    printSuccess('CALIBRATION PASS FOUND!')
    gui.generic.exposure_done_counter(total, 0)
    printSuccess('CALIBRATION FINISHED!')
    return total
