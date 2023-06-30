import time
import threading
import customtkinter

import util.serialCOM as com
import shell.process as pro
from classes.GUI import App


def thread_fun(target, label_output1, label_output2):
    threading.Thread(target=target, args=[label_output1, label_output2], daemon=True).start()


def Run():
    global index, subindex, optionindex
    print(index, subindex, optionindex)

    textBoxOutput.place_forget()
    label_last.place_forget()
    label_output1.place_forget()
    label_output2.place_forget()

    if 0 <= index <= 4 or index == 8:
        label_output1.place(relx=0.08, rely=0.58)
        label_output2.place(relx=0.08, rely=0.66)
        label_output1.configure(text='')
        label_output2.configure(text='')

    if index == 0 and subindex == 0:
        thread_fun(exp.defectSolidCalib, label_output1, label_output2)
    elif index == 0 and subindex == 1:
        thread_fun(exp.pixedDefectCalib, label_output1, label_output2)
    elif index == 0 and subindex == 2:
        thread_fun(exp.shadingCalib, label_output1, label_output2)
    elif index == 0 and subindex == 3:
        thread_fun(exp.uniformityCalib, label_output1, label_output2)

    elif index == 1 and subindex == 0:
        thread_fun(exp.defectSolidStereoCalib, label_output1, label_output2)
    elif index == 1 and subindex == 1:
        thread_fun(exp.defectSolidBpyCalib, label_output1, label_output2)
    elif index == 1 and subindex == 2:
        thread_fun(exp.uniformityCalibStereo, label_output1, label_output2)
    elif index == 1 and subindex == 3:
        thread_fun(exp.uniformityCalibBpy, label_output1, label_output2)

    elif index == 2 and subindex == 0:
        thread_fun(exp.defectSolidTomoCalib, label_output1, label_output2)
    elif index == 2 and subindex == 1:
        thread_fun(exp.uniformityCalibTomo, label_output1, label_output2)

    elif index == 3:
        thread_fun(exp.uniformityCalibES, label_output1, label_output2)

    elif index == 4:
        thread_fun(exp.mAFullCalibration, label_output1, label_output2)

    elif index == 5:
        0
        # TODO ICON

    elif index == 6:
        text = pro.saveMACs()
        print(text)
        textBoxOutput.insert(0.0, text)
        textBoxOutput.place(relx=0.1, rely=0.44)

    elif index == 7:
        if optionindex == 0 and subindex == 0:
            print('EXECUTING')
            pro.openRU()
        elif optionindex == 1 and subindex == 0:
            pro.closeRU()
        elif optionindex == 2 and subindex == 0:
            pro.openMUTLMU()
        elif optionindex == 3 and subindex == 0:
            pro.openMUTLMCU()
        elif optionindex == 4 and subindex == 0:
            pro.closeMUTL()

        if optionindex == 0 and subindex == 1:
            print('ENABLE HLV')
        elif optionindex == 1 and subindex == 1:
            print('ENABLE MAG')
        elif optionindex == 2 and subindex == 1:
            print('ENABLE ment mode')

        if optionindex == 0 and subindex == 2:
            pro.startOffsetCalib()
        elif optionindex == 1 and subindex == 2:
            pro.startDefectCalib()
        elif optionindex == 2 and subindex == 2:
            pro.startDefectSolidCalib()
        elif optionindex == 3 and subindex == 2:
            pro.startPixelDefectCalib()
        elif optionindex == 4 and subindex == 2:
            pro.startShadingCalib()
        elif optionindex == 5 and subindex == 2:
            pro.startUniformityCalib()

        if optionindex == 0 and subindex == 3:
            pro.startDefectSolidStereoCalib()
        elif optionindex == 1 and subindex == 3:
            pro.startDefectSolidBpyCalib()
        elif optionindex == 2 and subindex == 3:
            pro.startDefectSolidTomo()
        elif optionindex == 3 and subindex == 3:
            pro.startUniformityStereoCalib()
        elif optionindex == 4 and subindex == 3:
            pro.startUniformityBpyCalib()
        elif optionindex == 5 and subindex == 3:
            pro.startUniformityTomoCalib()
        elif optionindex == 6 and subindex == 3:
            pro.startUniformityESCalib()

    elif index == 8:
        print('single shot')
        thread_fun(exp.singleShot, label_output1, label_output2)

    elif index == 9:
        pro.createWOLsetupFile('Ethernet')
        label_result.configure(text='Please copy mannually to:')
        label_result.place(relx=0.1, rely=0.44)
        text = 'C:\Program Files (x86)\Fujifilm\WOL'
        textBoxOutput.insert(0.0, text)
        textBoxOutput.place(relx=0.1, rely=0.5)


if __name__ == '__main__':
    app = App()
    app.create_main_menu()
    app.mainloop()


