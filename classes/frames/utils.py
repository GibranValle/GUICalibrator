from customtkinter import CTkFrame, CTkButton, CTkLabel, CTk, CTkOptionMenu, CTkTextbox
from util import menu_list as m
from classes.constants import *
from classes.generic import *

def pushed(self):
    print(self.menu_utils.get())

def create_utils_frame(self):
    self.frame_utils = CTkFrame(self, fg_color=BG_COLOR_1)
    self.label_utils = CTkLabel(self.frame_utils, text='Utils Menu', font=self.font_title)
    self.label_utils.pack(pady=10, padx=20)

    self.menu_utils = CTkOptionMenu(self.frame_utils, values=m.utils_menu, font=self.font_text)
    self.menu_utils.pack(pady=5, padx=30, fill='x')

    self.run_button = CTkButton(self.frame_utils, command=lambda: pushed(self), font=self.font_text,
                                text='Run', text_color_disabled=DISABLED_COLOR)
    self.run_button.pack(pady=5, padx=30, fill='x')

    self.textBoxOutput = CTkTextbox(self.frame_utils, font=self.font_output, state='normal', height=100)
    self.textBoxOutput.pack(pady=5, padx=30, fill='x')

    self.main_menu = CTkButton(self.frame_utils, command=lambda: back2main(self), font=self.font_text, text='Main menu',
                               fg_color=ERR_COLOR, hover_color=ERR_COLOR_HOVER)
    self.main_menu.pack(pady=10, padx=10)
