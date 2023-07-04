import time
from util.delayManager import waitTillEndYellow, waitTillStartYellow
import customtkinter as ck
from util.serialCOM import communicate

def mAFullCalibration(label1: ck.CTkLabel, label2: ck.CTkLabel):
    totaltime = 0
    label1.configure(text='')
    if not communicate("T"):  # VERIFY CONNECTION BEFORE COUNTDOWN
        return
    for i in range(1, -1, -1):
        label2.configure(text=f'Requesting exposure in: {i}')
        time.sleep(1)

    if not communicate("L"):  # REQUEST FOR LONG EXPOSURE
        return
    label1.configure(text='Accepted LONG exposure')
    label2.configure(text='')

    totaltime += waitTillStartYellow(10, label2)
    print('duration: ', duration)
    if duration < 0:
        label1.configure(text='Exposure request failure')
        label2.configure(text='Please verify bot')
        return
    totaltime += waitTillEndYellow(5 * 60, 0, label2)
    label1.configure(text='Requesting End of exposure')
    if not communicate("X"):
        return
    label1.configure(text='Exposure done')
    for i in range(0, 15 * 60, -1):
        label2.configure(text=f'Calculating: {i}')
        time.sleep(1)

    label1.configure(text='Calculation done!')
    label1.configure(text=f'This calib took: {totaltime}s')
