from customtkinter import CTkFrame, CTkButton, CTkLabel, CTk, CTkOptionMenu, CTkTextbox, CTkSwitch
from util import menu_list as m
from classes.constants import *
from classes.generic import *
from calibrations.maFullCalib import mAFullCalibration
from calibrations.exposureCalibration import *
from threading import Thread
from calibrations.allExposureNeeded import allRequired


class Manual:
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

    def handleSwitch(self):
        print(self.gui.is_auto_ok)
        self.gui.is_auto_ok = not self.gui.is_auto_ok

    def pushed(self, button):
        gui = self.gui

        if button == 'pause':
            gui.delay.pauseStatus()
            self.not_only_pause()
            return

        elif button == 'start':

            option = self.gui.menu_manual.get()
            if option == 'Single Shot':
                print('single shot')
                self.only_stop()
                if gui.delay.status == 'pause':
                    gui.delay.startStatus()
                    return
                Thread(target=singleShot, args=[gui], daemon=True).start()

            elif option == 'mA full calib shot':
                print('ma full')
                self.not_only_start()
                if gui.delay.status == 'pause':
                    gui.delay.startStatus()
                    return
                Thread(target=mAFullCalibration, args=[gui], daemon=True).start()

            elif option == '10 shots':
                print('10 shots')
                self.not_only_start()
                if gui.delay.status == 'pause':
                    gui.delay.startStatus()
                    return
                Thread(target=TenShots, args=[gui], daemon=True).start()

            elif option == 'All needed (FPD)':
                print('smart exposure')
                self.not_only_start()
                if gui.delay.status == 'pause':
                    gui.delay.startStatus()
                    return
                Thread(target=allRequired, args=[gui], daemon=True).start()

            else:
                return

            gui.delay.startStatus()

        elif button == 'stop':
            gui.delay.stopStatus()
            self.only_start()

    def create_manual_frame(self):
        gui = self.gui
        gui.frame_manual = CTkFrame(gui, fg_color=BG_COLOR_1)
        gui.label_manual = CTkLabel(gui.frame_manual, text='Manual Mode', font=gui.font_title)
        gui.label_manual.pack(pady=10, padx=20)
        gui.menu_manual = CTkOptionMenu(gui.frame_manual, values=m.manual_menu, font=gui.font_text)
        gui.menu_manual.pack(pady=5, padx=30, fill='x')
        gui.frame_buttons = CTkFrame(gui.frame_manual, fg_color=BG_COLOR_1)
        gui.frame_buttons.pack(pady=5, padx=20)
        gui.start_button_m = CTkButton(gui.frame_buttons, command=lambda: self.pushed('start'), font=gui.font_text,
                                       width=WIDTH_3, text=PLAY, text_color_disabled=DISABLED_COLOR)
        gui.start_button_m.grid(row=0, column=1)
        gui.pause_button_m = CTkButton(gui.frame_buttons, command=lambda: self.pushed('pause'), font=gui.font_text,
                                       width=WIDTH_3,
                                       text=PAUSE, state='disabled', text_color_disabled=DISABLED_COLOR,
                                       fg_color=OK_COLOR, hover_color=OK_COLOR_HOVER)
        gui.pause_button_m.grid(row=0, column=2, padx=10)
        gui.stop_button_m = CTkButton(gui.frame_buttons, command=lambda: self.pushed('stop'), font=gui.font_text,
                                      width=WIDTH_3,
                                      text=STOP, state='disabled', text_color_disabled=DISABLED_COLOR,
                                      fg_color=ERR_COLOR, hover_color=ERR_COLOR_HOVER)
        gui.stop_button_m.grid(row=0, column=3)
        gui.label_output1_m = CTkLabel(gui.frame_manual, text='M1:', font=gui.font_output, anchor='w')
        gui.label_output1_m.pack(pady=(5, 0), padx=30, fill='x')
        gui.label_output2_m = CTkLabel(gui.frame_manual, text='M2:', font=gui.font_output, anchor='w')
        gui.label_output2_m.pack(pady=(0, 5), padx=30, fill='x')
        gui.main_menu = CTkButton(gui.frame_manual, command=gui.generic.back2main, font=gui.font_text, text='Main menu',
                                  fg_color=ERR_COLOR, hover_color=ERR_COLOR_HOVER)
        gui.main_menu.pack(pady=10, padx=10)
        gui.switch_auto = CTkSwitch(gui.frame_manual, text='Autoclick ok', font=gui.font_text, command=self.handleSwitch)
        gui.switch_auto.pack(pady=10, padx=10)
