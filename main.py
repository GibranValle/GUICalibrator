import time
import threading
import customtkinter

from util import menu_list as m
import util.serialCOM as com
import shell.process as pro
import calibrations.exposureCalibration as exp

index = subindex = -1


def connectButton():
    if com.isListening:
        com.endListening()
        button_serial.configure(text='Open serial port')
        title.configure(text_color='red', text='Offline')

    else:
        serialThread = threading.Thread(target=com.startListening)
        serialThread.start()
        time.sleep(1.5)
        title.configure(text_color='green', text='Online')
        button_serial.configure(text='Close serial port')


def menuCallback(v):
    global index, subindex
    index = m.menu.index(v)
    label_submenu.place_forget()
    submenu.place_forget()
    subButton.place_forget()
    iconsmenu.place_forget()
    label_icons.place_forget()
    rightButton.place_forget()
    leftButton.place_forget()
    label_output1.place_forget()
    label_output2.place_forget()

    if index == 0:
        subButton.configure(text='Run calibration')
        submenu.configure(values=m.basic)
    elif index == 1:
        subButton.configure(text='Run calibration')
        submenu.configure(values=m.stereo)
    elif index == 2:
        subButton.configure(text='Run calibration')
        submenu.configure(values=m.tomo)
    elif index == 3:
        subButton.configure(text='Run calibration')
        submenu.configure(values=m.es)
    elif index == 4:
        subButton.configure(text='Run calibration')
        subButton.place(relx=0.09, rely=0.3)
    elif index == 5:
        submenu.configure(values=m.icons_menu)
    elif index == 6:
        subButton.configure(text='Create file')
        subButton.place(relx=0.09, rely=0.3)

    if index >= 0 and index <= 3:
        label_submenu.configure(text='Available calibrations')
        submenu.set("Select:")
        label_submenu.place(relx=0.1, rely=0.3)
        submenu.place(relx=0.1, rely=0.36)

    elif index == 5:
        label_submenu.configure(text='Available menus')
        submenu.set("Select:")
        label_submenu.place(relx=0.1, rely=0.3)
        submenu.place(relx=0.1, rely=0.36)

    elif index == 7:
        0
        # TODO WINDOW menu

    elif index == 8:
        subButton.configure(text='Perform exposure')
        subButton.place(relx=0.09, rely=0.3)


def submenuCallback(v):
    global index, subindex
    subButton.place_forget()
    iconsmenu.place_forget()
    label_icons.place_forget()
    rightButton.place_forget()
    leftButton.place_forget()
    label_output1.place_forget()
    label_output2.place_forget()

    if index == 0: subindex = m.basic.index(v)
    elif index == 1: subindex = m.stereo.index(v)
    elif index == 2: subindex = m.tomo.indx(v)
    elif index == 3: subindex = m.es.index(v)
    elif index == 5:
        subindex = m.icons_menu.index(v)
        if subindex == 0: iconsmenu.configure(values=m.icons_aws)
        elif subindex == 1: iconsmenu.configure(values=m.icons_RU)
        elif subindex == 2: iconsmenu.configure(values=m.icons_mutl)
        elif subindex == 3: iconsmenu.configure(values=m.icons_calib)
        elif subindex == 4: iconsmenu.configure(values=m.icons_calib_opt)

    if index >= 0 and index < 5 and subindex >= 0:
        subButton.place(relx=0.09, rely=0.45)

    elif subindex >= 0 and index == 5:
            iconsmenu.place(relx=0.1, rely=0.51)
            label_icons.place(relx=0.1, rely=0.45)


def lastmenuCallback(v):
    global index, subindex
    leftButton.place_forget()
    rightButton.place_forget()
    label_output1.place_forget()
    label_output2.place_forget()
    global subindex
    if subindex >= 0:
        leftButton.configure(text='Move cursor')
        rightButton.configure(text='Move & click')
        leftButton.place(relx=0.1, rely=0.65)
        rightButton.place(relx=0.5, rely=0.65)


def thread_fun(target, label_output1, label_output2):
    threading.Thread(target=target, args=[label_output1, label_output2], daemon=True).start()


def Run():
    textOutput.place_forget()
    label_icons.place_forget()
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
        textOutput.insert(0.0, text)
        textOutput.place(relx=0.1, rely=0.44)

    elif index == 7:
        0
        # TODO WINDOW

    elif index == 8:
        print('single shot')
        thread_fun(exp.singleShot, label_output1, label_output2)


def close():
    com.endListening()
    app.destroy()


if __name__ == '__main__':
    try:
        customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

        app = customtkinter.CTk()
        font_title = ("Consolas", 25, 'bold')
        font_text = ("Consolas", 20)
        app.geometry("400x500")
        app.title("FPD Calibration bot")
        app.resizable(False, False)

        frame_1 = customtkinter.CTkFrame(master=app, corner_radius=10)
        frame_1.pack(fill="both", expand=True)

        label_close = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.CENTER,
                                             font=font_text, text='*Use this button to close app*')
        label_close.place(relx=0.1, rely=0)

        button_close = customtkinter.CTkButton(master=frame_1, command=close, font=font_text, text='CLOSE APP',
                                               fg_color='#610000', hover_color='#460000', height=35)
        button_close.place(relx=0.3, rely=0.06)

        title = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, font=font_title, text='Offline',
                                       text_color='red')
        title.place(relx=0.1, rely=0.9)

        if com.offline:
            button_serial = customtkinter.CTkButton(master=frame_1, command=connectButton, font=font_text, height=40,
                                                    width=180, text='Open serial port')
        else:
            button_serial = customtkinter.CTkButton(master=frame_1, command=connectButton, font=font_text, height=40,
                                                    width=180, text='Open serial port')
        button_serial.place(relx=0.4, rely=0.89)

        label_menu = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, font=font_text,
                                            text='Select Mode')
        label_menu.place(relx=0.1, rely=0.15)

        menu = customtkinter.CTkOptionMenu(frame_1, values=m.menu, font=font_text, command=menuCallback, height=35)
        menu.place(relx=0.1, rely=0.21)
        menu.set("Select:")

        label_submenu = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, font=font_text)
        submenu = customtkinter.CTkOptionMenu(frame_1, font=font_text, command=submenuCallback, height=35)
        subButton = customtkinter.CTkButton(master=frame_1, command=Run, font=font_text, text='Run calibration',
                                            fg_color='#003366', hover_color='#004477', height=50, width=200)

        textOutput = customtkinter.CTkTextbox(app, width=250, font=font_text, height=132, state='normal')

        label_icons = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, font=font_text,
                                             text='Look for icon:')
        iconsmenu = customtkinter.CTkOptionMenu(frame_1, font=font_text, command=lastmenuCallback, height=35)
        iconsmenu.set('Select:')

        leftButton = customtkinter.CTkButton(master=frame_1, command=Run, font=font_text, hover_color='#004477',
                                             height=50,
                                             width=150)
        rightButton = customtkinter.CTkButton(master=frame_1, command=Run, font=font_text, hover_color='#004477',
                                              height=50,
                                              width=150)

        label_output1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, font=font_text, text='', bg_color='#555555', height=30, width=330, corner_radius=20)
        label_output2 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, font=font_text, text='', bg_color='#555555', height=30, width=330, corner_radius=20)

        app.mainloop()

    except KeyboardInterrupt:
        print('CLOSING')
