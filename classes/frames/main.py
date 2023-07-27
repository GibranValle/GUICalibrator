from customtkinter import CTkFrame, CTkButton, CTkLabel, CTk, CTkOptionMenu, CTkTextbox
from util import menu_list as m
from classes.constants import *
from classes.generic import *


def create_main_frame(self):
    self.frame_main = CTkFrame(self, fg_color=BG_COLOR_1)
    self.Label = CTkLabel(self.frame_main, text='Main Menu', font=self.font_title)
    self.Label.pack(pady=(10, 5), padx=20)

    self.serial_config = CTkButton(self.frame_main, command=lambda: display_serial_frame(self), font=self.font_text, text='Serial config')
    self.serial_config.pack(pady=5, padx=10)

    self.manual_menu = CTkButton(self.frame_main, command=lambda: display_manual_frame(self), font=self.font_text, text='Manual Mode')
    self.manual_menu.pack(pady=5, padx=10)

    self.auto_menu = CTkButton(self.frame_main, command=lambda: display_auto_frame(self), font=self.font_text, text='Auto')
    self.auto_menu.pack(pady=5, padx=10)

    self.utils_menu = CTkButton(self.frame_main, command=lambda: display_utils_frame(self), font=self.font_text, text='Utils')
    self.utils_menu.pack(pady=(5, 20), padx=10)
