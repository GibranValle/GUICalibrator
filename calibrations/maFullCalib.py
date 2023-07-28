import customtkinter as ck
from util.serialCOM import communicate
from classes.generic import Generic


def mAFullCalibration(gui_object: ck.CTk = None):
    gui = gui_object
    gui.delay.resetFlags()
    print('ma class')
    total = 0
    gui.generic.edit_output(' ', ' ')
    if not communicate("T"):  # VERIFY CONNECTION BEFORE COUNTDOWN
        text1 = 'BOT NOT RESPONDING!'
        text2 = 'Please verify'
        gui.generic.edit_output(text1, text2)
        return
    text = 'Requesting exposure in'
    time = gui.delay.countdown(0, text, 10)
    total += time
    if time < 10:
        text1 = 'Exposure aborted'
        text2 = '----------------'
        gui.generic.edit_output(text1, text2)
        return
    if not communicate("L"):  # REQUEST FOR LONG EXPOSURE
        gui_object.isRunning = False
        text1 = 'BOT NOT RESPONDING!'
        text2 = 'Please verify'
        gui.generic.edit_output(text1, text2)
        return
    text1 = 'Accepted LONG exposure'
    text2 = 'Please verify'
    gui.generic.edit_output(text1, text2)
    time = gui.delay.waitTillStartYellow(10)
    total += time
    if time >= 9:
        text1 = 'Exposure request failure'
        text2 = 'Verify CN2 Connector'
        gui.generic.edit_output(text1, text2)
        gui_object.isRunning = False
        return
    text1 = 'UNDER EXPOSURE...'
    text2 = '----------------'
    gui.generic.edit_output(text1, text2)
    time = gui.delay.waitTillEndYellow(5 * 60, 0)
    if time == -1:
        text1 = 'Aborted exposure'
        text2 = 'Please verify end on exposure'
        gui.generic.edit_output(text1, text2)
        gui_object.isRunning = False
        if not communicate("X"):  # REQUEST FOR LONG EXPOSURE
            edit_output(gui_object, '', 'Please end exposure manually')
        return
    elif time < 30:
        text1 = 'Premature end of exposure'
        text2 = 'Please verify system'
        gui.generic.edit_output(text1, text2)
        gui_object.isRunning = False
        if not communicate("X"):  # REQUEST FOR LONG EXPOSURE
            edit_output(gui_object, '', 'Please end exposure manually')
        return
    total += time
    text1 = 'Requesting End of exposure'
    text2 = ''
    gui.generic.edit_output(text1, text2)
    if not communicate("X"):
        text1 = ''
        text2 = 'Please end exposure manually'
        gui.generic.edit_output(text1, text2)
        gui_object.isRunning = False
        return
    text1 = 'Exposure done'
    text2 = createMessage('This calib took', total)
    gui.generic.edit_output(text1, text2)
