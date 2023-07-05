from util.delayManager import waitTillEndYellow, waitTillStartYellow, countdown, createMessage, resetStopFlag
import customtkinter as ck
from util.serialCOM import communicate

def mAFullCalibration(label1: ck.CTkLabel, label2: ck.CTkLabel):
    resetStopFlag()
    total = 0
    label1.configure(text='')
    if not communicate("T"):  # VERIFY CONNECTION BEFORE COUNTDOWN
        return 
    text = 'Requesting exposure in'
    time = countdown(label2, 0, text, 10)
    total += time
    if time < 10:
        label1.configure(text='Exposure aborted')
        label2.configure(text='----------------')
        return 
    if not communicate("L"):  # REQUEST FOR LONG EXPOSURE
        return 
    label1.configure(text='Accepted LONG exposure')
    label2.configure(text='')
    time = waitTillStartYellow(10, label2)
    total += time
    if time >= 9:
        label1.configure(text='Exposure request failure')
        label2.configure(text='Please stop calibration')
        return 
    label1.configure(text='UNDER EXPOSURE...')
    time = waitTillEndYellow(5 * 60, 0, label2)
    total += time
    if time < 0:
        label1.configure(text='Exposure request failure')
        label2.configure(text='Please stop calibration')
        return 
    label1.configure(text='Requesting End of exposure')
    if not communicate("X"):
        return 
    label1.configure(text='Exposure done')
    text = 'Calculating'
    total += countdown(label2, 15*60, text, 0)
    label1.configure(text='Calculation done!')
    text = createMessage('This calib took', total)
    label1.configure(text=text)
