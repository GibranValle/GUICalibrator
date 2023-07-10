from util.delayManager import waitTillEndYellow, waitTillStartYellow, countdown, createMessage, resetStopFlag, editButton
import customtkinter as ck
from util.serialCOM import communicate

def mAFullCalibration(gui_object:ck.CTk = None):
    label1 = gui_object.label_output1
    label2 = gui_object.label_output2
    button = gui_object.button_run

    resetStopFlag()
    total = 0
    label1.configure(text='')
    if not communicate("T"):  # VERIFY CONNECTION BEFORE COUNTDOWN
        label1.configure(text='BOT NOT RESPONDING!')
        label2.configure(text='Please verify')
        return 
    text = 'Requesting exposure in'
    time = countdown(label2, 0, text, 10)
    total += time
    if time < 10:
        label1.configure(text='Exposure aborted')
        label2.configure(text='----------------')
        return 
    if not communicate("L"):  # REQUEST FOR LONG EXPOSURE
        label1.configure(text='BOT NOT RESPONDING!')
        label2.configure(text='Please verify')
        gui_object.isRunning = False
        editButton('Start Exposure', button)
        return 
    label1.configure(text='Accepted LONG exposure')
    label2.configure(text='')
    time = waitTillStartYellow(10, label2)
    total += time
    if time >= 9:
        label1.configure(text='Exposure request failure')
        label2.configure(text='Verify CN2 Connector')
        gui_object.isRunning = False
        editButton('Start Exposure', button)
        return
    label1.configure(text='UNDER EXPOSURE...')
    time = waitTillEndYellow(5 * 60, 0, label2)
    if time == -1:
        label1.configure(text='Aborted exposure')
        label2.configure(text='Please verify end on exposure')
        gui_object.isRunning = False
        editButton('Start Exposure', button)
        if not communicate("X"):  # REQUEST FOR LONG EXPOSURE
            label2.configure(text='Please end exposure manually')
        return
    elif time < 30 :
        label1.configure(text='Premature end of exposure')
        label2.configure(text='Please verify system')
        gui_object.isRunning = False
        editButton('Start Exposure', button)
        if not communicate("X"):  # REQUEST FOR LONG EXPOSURE
            label2.configure(text='Please end exposure manually')
        return
    total += time
    label1.configure(text='Requesting End of exposure')
    if not communicate("X"):
        label2.configure(text='Please end exposure manually')
        gui_object.isRunning = False
        editButton('Start Exposure', button)
        return 
    label1.configure(text='Exposure done')
    text = createMessage('This calib took', total)
    label1.configure(text=text)
    editButton('Start Exposure', button)

