import tkinter as tk
from customtkinter import CTkFrame, CTkButton, CTkLabel, CTk, CTkOptionMenu, CTkTextbox
from util import menu_list as m
from classes.constants import *
from classes.generic import *


def create_main_frame(self):
    self.frame_main = CTkFrame(self, fg_color=BG_COLOR_1)

    self.serial_frame = CTkFrame(self, fg_color=BG_COLOR_0)
    self.serial_label = CTkLabel(self.serial_frame, text='Offline', font=self.font_title, text_color='red')
    self.serial_label.pack(side=tk.LEFT, padx=10)
    self.serial_button = CTkButton(self.serial_frame, command=self.generic.display_serial_frame,
                                   font=self.font_text,text='Serial config')
    self.serial_button.pack(side=tk.LEFT, pady=5, padx=10)
    self.serial_frame.pack(padx=10, pady=(5, 0))

    self.manual_menu = CTkButton(self.frame_main, command=self.generic.display_manual_frame, font=self.font_text, text='Manual Mode')
    self.manual_menu.pack(pady=(10, 5), padx=10)

    self.auto_menu = CTkButton(self.frame_main, command=self.generic.display_auto_frame, font=self.font_text, text='Auto')
    self.auto_menu.pack(pady=(5, 10), padx=10)