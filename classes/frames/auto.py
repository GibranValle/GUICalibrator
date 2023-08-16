from customtkinter import CTkFrame, CTkButton, CTkLabel, CTkOptionMenu
from util import menu_list as m
from classes.constants import *
from calibrations.exposureCalibration import *
from calibrations.allExposureNeeded import allRequired
from shell.MCU import *
from threading import Thread


class Auto:

    def __init__(self, gui_object: ck):
        self.gui = gui_object

    def only_start(self):
        gui = self.gui
        gui.start_button_m.configure(state='normal')
        gui.pause_button_m.configure(state='disabled')
        gui.stop_button_m.configure(state='disabled')

    def not_only_start(self):
        gui = self.gui
        gui.start_button_m.configure(state='disabled')
        gui.pause_button_m.configure(state='normal')
        gui.stop_button_m.configure(state='normal')

    def only_stop(self):
        gui = self.gui
        gui.start_button_m.configure(state='disabled')
        gui.pause_button_m.configure(state='disabled')
        gui.stop_button_m.configure(state='normal')

    def not_only_pause(self):
        gui = self.gui
        gui.start_button_m.configure(state='normal')
        gui.pause_button_m.configure(state='disabled')
        gui.stop_button_m.configure(state='normal')

    def menu_change(self, option):
        print(option)
        if option == 'Calibration':
            self.gui.menu_calib.configure(values=m.calib_menu)
            self.gui.menu_calib.set(m.calib_menu[0])
        elif option == 'Opt Calibrations':
            self.gui.menu_calib.configure(values=m.calib_opt_menu)
            self.gui.menu_calib.set(m.calib_opt_menu[0])

    def pushed(self, button):
        gui = self.gui
        self.status = button

        if button == 'pause':
            gui.delay.pauseStatus()
            self.not_only_pause()
            return

        elif button == 'stop':
            gui.delay.stopStatus()
            self.only_start()

        elif button == 'start':
            option = self.gui.menu_calib.get()
            if option in m.exp_calib_menu or option in m.calib_opt_menu:
                if gui.delay.status == 'pause':
                    gui.delay.startStatus()
                    return
                Thread(target=allRequired, args=[gui], daemon=True).start()

            else:
                return
            gui.delay.startStatus()

    def enableCalib(self):
        gui = self.gui
        option = self.gui.menu_calib.get()
        if option == 'offset':
            startOffsetCalib()
        elif option == 'defect':
            startDefectCalib()
        elif option == 'defect solid':
            startDefectSolidCalib()

    def create_auto_frame(self):
        gui = self.gui

        gui.frame_auto = CTkFrame(gui, fg_color=BG_COLOR_1)
        gui.label_auto = CTkLabel(gui.frame_auto, text='Auto Mode', font=gui.font_title)
        gui.label_auto.pack(pady=5, padx=20)

        gui.menu_auto = CTkOptionMenu(gui.frame_auto, values=m.auto_menu, font=gui.font_text,
                                      command=lambda option: self.menu_change(option))
        gui.menu_auto.pack(pady=5, padx=20, fill='x')

        gui.menu_calib = CTkOptionMenu(gui.frame_auto, values=m.calib_menu, font=gui.font_text)
        gui.menu_calib.set(m.calib_menu[0])
        gui.menu_calib.pack(pady=5, padx=20, fill='x')

        gui.enable_calib = CTkButton(gui.frame_auto, command=self.enableCalib, font=gui.font_text,
                                     text='Enable calib', text_color_disabled=DISABLED_COLOR)
        gui.enable_calib.pack(pady=5, padx=20, fill='x')

        gui.frame_buttons = CTkFrame(gui.frame_auto, fg_color=BG_COLOR_1)
        gui.frame_buttons.pack(pady=5, padx=20, fill='x')

        gui.start_button = CTkButton(gui.frame_buttons, command=lambda: self.pushed('start'), font=gui.font_text,
                                     width=WIDTH_3,
                                     text=PLAY, text_color_disabled=DISABLED_COLOR)
        gui.start_button.grid(row=0, column=1)

        gui.pause_button = CTkButton(gui.frame_buttons, command=lambda: self.pushed('pause'), font=gui.font_text,
                                     width=WIDTH_3,
                                     text=PAUSE, state='disabled', text_color_disabled=DISABLED_COLOR,
                                     fg_color=OK_COLOR, hover_color=OK_COLOR_HOVER)
        gui.pause_button.grid(row=0, column=2, padx=20)

        gui.stop_button = CTkButton(gui.frame_buttons, command=lambda: self.pushed('stop'), font=gui.font_text,
                                    width=WIDTH_3,
                                    text=STOP, state='disabled', text_color_disabled=DISABLED_COLOR,
                                    fg_color=ERR_COLOR, hover_color=ERR_COLOR_HOVER)
        gui.stop_button.grid(row=0, column=3)

        gui.label_output1 = CTkLabel(gui.frame_auto, text='M1:', font=gui.font_output, anchor='w')
        gui.label_output1.pack(pady=(3, 0), padx=20, fill='x')

        gui.label_output2 = CTkLabel(gui.frame_auto, text='M2:', font=gui.font_output, anchor='w')
        gui.label_output2.pack(pady=(3, 5), padx=20, fill='x')

        gui.main_menu = CTkButton(gui.frame_auto, command=gui.generic.back2main, font=gui.font_text,
                                  text='Main menu',
                                  fg_color=ERR_COLOR, hover_color=ERR_COLOR_HOVER)
        gui.main_menu.pack(pady=(5, 3), padx=10)
