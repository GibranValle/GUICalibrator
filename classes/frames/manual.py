from customtkinter import CTkFrame, CTkButton, CTkLabel, CTk, CTkOptionMenu, CTkTextbox
from util import menu_list as m
from classes.constants import *
from classes.generic import *


def pushed(self, button):
    self.status = button

    if button == 'pause':
        print('paused')
        self.start_button_m.configure(state='normal')
        self.pause_button_m.configure(state='disabled')
        self.stop_button_m.configure(state='normal')
        return


    elif button == 'start':
        print('RUNNING')
        option = self.menu_manual.get()
        if option == 'Single Shot':
            self.start_button_m.configure(state='disabled')
            self.pause_button_m.configure(state='disabled')
            self.stop_button_m.configure(state='normal')
            return

        self.start_button_m.configure(state='disabled')
        self.pause_button_m.configure(state='normal')
        self.stop_button_m.configure(state='normal')
        return

    elif button == 'stop':
        print('NOT RUNNING')
        self.start_button_m.configure(state='normal')
        self.pause_button_m.configure(state='disabled')
        self.stop_button_m.configure(state='disabled')


def create_manual_frame(self):
    self.frame_manual = CTkFrame(self, fg_color=BG_COLOR_1)
    self.label_manual = CTkLabel(self.frame_manual, text='Manual Mode', font=self.font_title)
    self.label_manual.pack(pady=10, padx=20)

    self.menu_manual = CTkOptionMenu(self.frame_manual, values=m.manual_menu, font=self.font_text)
    self.menu_manual.pack(pady=5, padx=30, fill='x')

    self.frame_buttons = CTkFrame(self.frame_manual, fg_color=BG_COLOR_1)
    self.frame_buttons.pack(pady=5, padx=20)

    self.start_button_m = CTkButton(self.frame_buttons, command=lambda: pushed(self, 'start'), font=self.font_text, width=WIDTH_3,
                                    text=PLAY, text_color_disabled=DISABLED_COLOR)
    self.start_button_m.grid(row=0, column=1)

    self.pause_button_m = CTkButton(self.frame_buttons, command=lambda: pushed(self, 'pause'), font=self.font_text, width=WIDTH_3,
                                    text=PAUSE, state='disabled', text_color_disabled=DISABLED_COLOR, fg_color=OK_COLOR, hover_color=OK_COLOR_HOVER)
    self.pause_button_m.grid(row=0, column=2, padx=10)

    self.stop_button_m = CTkButton(self.frame_buttons, command=lambda: pushed(self, 'stop'), font=self.font_text, width=WIDTH_3,
                                   text=STOP, state='disabled', text_color_disabled=DISABLED_COLOR, fg_color=ERR_COLOR, hover_color=ERR_COLOR_HOVER)
    self.stop_button_m.grid(row=0, column=3)

    self.label_output1 = CTkLabel(self.frame_manual, text='M1:', font=self.font_text, anchor='w')
    self.label_output1.pack(pady=(5, 0), padx=30, fill='x')

    self.label_output2 = CTkLabel(self.frame_manual, text='M2:', font=self.font_text, anchor='w')
    self.label_output2.pack(pady=(0, 5), padx=30, fill='x')

    self.main_menu = CTkButton(self.frame_manual, command=lambda: back2main(self), font=self.font_text, text='Main menu',
                               fg_color=ERR_COLOR, hover_color=ERR_COLOR_HOVER)
    self.main_menu.pack(pady=10, padx=10)
