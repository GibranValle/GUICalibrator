from customtkinter import CTkFrame, CTkButton, CTkLabel, CTk, CTkOptionMenu, CTkTextbox
from util import menu_list as m
from classes.constants import *


def menu_change(self, option):
    if option == 'Calibration':
        self.menu_calib.configure(values=m.calib_menu)
        self.menu_calib.set(m.calib_menu[0])
    elif option == 'Opt Calibrations':
        self.menu_calib.configure(values=m.calib_opt_menu)
        self.menu_calib.set(m.calib_opt_menu[0])


def pushed(self, button):
    self.status = button
    if button == 'pause':
        print('paused')
        self.start_button.configure(state='normal')
        self.pause_button.configure(state='disabled')
        self.stop_button.configure(state='normal')
        return


    elif button == 'start':
        self.start_button.configure(state='disabled')
        self.pause_button.configure(state='normal')
        self.stop_button.configure(state='normal')
        print('RUNNING')
        return

    elif button == 'stop':
        print('NOT RUNNING')
        self.start_button.configure(state='normal')
        self.pause_button.configure(state='disabled')
        self.stop_button.configure(state='disabled')


def create_auto_frame(self):
    self.frame_auto = CTkFrame(self, fg_color=BG_COLOR_1)
    self.label_auto = CTkLabel(self.frame_auto, text='Auto Mode', font=self.font_title)
    self.label_auto.pack(pady=5, padx=20)

    self.menu_auto = CTkOptionMenu(self.frame_auto, values=m.auto_menu, font=self.font_text, command=lambda option: menu_change(self, option))
    self.menu_auto.pack(pady=5, padx=20, fill='x')

    self.menu_calib = CTkOptionMenu(self.frame_auto, values=m.calib_menu, font=self.font_text)
    self.menu_calib.set(m.calib_menu[0])
    self.menu_calib.pack(pady=5, padx=20, fill='x')

    self.enable_calib = CTkButton(self.frame_auto, command=self.generic.open_serial_config, font=self.font_text,
                                  text='Enable calib', text_color_disabled=DISABLED_COLOR)
    self.enable_calib.pack(pady=5, padx=20, fill='x')

    self.frame_buttons = CTkFrame(self.frame_auto, fg_color=BG_COLOR_1)
    self.frame_buttons.pack(pady=5, padx=20, fill='x')

    self.start_button = CTkButton(self.frame_buttons, command=lambda: pushed(self, 'start'), font=self.font_text, width=WIDTH_3,
                                  text=PLAY, text_color_disabled=DISABLED_COLOR)
    self.start_button.grid(row=0, column=1)

    self.pause_button = CTkButton(self.frame_buttons, command=lambda: pushed(self, 'pause'), font=self.font_text, width=WIDTH_3,
                                  text=PAUSE, state='disabled', text_color_disabled=DISABLED_COLOR, fg_color=OK_COLOR, hover_color=OK_COLOR_HOVER)
    self.pause_button.grid(row=0, column=2, padx=20)

    self.stop_button = CTkButton(self.frame_buttons, command=lambda: pushed(self, 'stop'), font=self.font_text, width=WIDTH_3,
                                 text=STOP, state='disabled', text_color_disabled=DISABLED_COLOR, fg_color=ERR_COLOR, hover_color=ERR_COLOR_HOVER)
    self.stop_button.grid(row=0, column=3)

    self.label_output1 = CTkLabel(self.frame_auto, text='M1:', font=self.font_output, anchor='w')
    self.label_output1.pack(pady=(3, 0), padx=20, fill='x')

    self.label_output2 = CTkLabel(self.frame_auto, text='M2:', font=self.font_output, anchor='w')
    self.label_output2.pack(pady=(3, 5), padx=20, fill='x')

    self.main_menu = CTkButton(self.frame_auto, command=self.generic.back2main, font=self.font_text, text='Main menu',
                               fg_color=ERR_COLOR, hover_color=ERR_COLOR_HOVER)
    self.main_menu.pack(pady=(5, 3), padx=10)
