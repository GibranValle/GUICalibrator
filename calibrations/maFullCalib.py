import customtkinter as ck

from util.serialCOM import communicate


def mAFullCalibration(gui_object: ck.CTk = None):
    gui = gui_object
    edit_output = gui.generic.edit_output
    not_responding = gui.generic.not_responding
    gui.delay.startStatus()
    total = 0
    gui.generic.clear_output()
    # VERIFY CONNECTION BEFORE COUNTDOWN
    if not communicate("T"):
        return not_responding()

    text = 'Requesting exposure in'
    time = gui.delay.countdown(0, text, 10)
    total += time
    if time < 10:
        text1 = 'App failure detected'
        text2 = 'Please verify'
        edit_output(text1, text2)
        gui.delay.stopStatus()
        return gui.generic.abort_requested()

    # REQUEST FOR LONG EXPOSURE
    if not communicate("L"):
        return not_responding()
    gui.generic.accepted('LONG')

    time = gui.delay.wait_for_exposure_signal(0, 10)
    total += time
    if time >= 9:
        text1 = 'Exposure request failure'
        text2 = 'Verify CN2 Connector'
        edit_output(text1, text2)
        gui.delay.stopStatus()
        return

    gui.generic.under_exposure()
    time = gui.delay.wait_for_long_end(5 * 60, 0)
    if time == -1:
        return gui.generic.abnormal()
    elif time < 30:
        return gui.generic.aborted()
    total += time

    # REQUEST FOR EXPOSURE END
    if not communicate("X"):
        return not_responding()

    gui.generic.request_end()
    if not communicate("X"):
        return gui.generic.end_manually()

    gui.generic.exposure_done(total)
