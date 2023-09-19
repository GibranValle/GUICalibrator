from customtkinter import CTkFrame, CTkButton, CTkLabel, CTk, CTkOptionMenu, CTkTextbox
from util import menu_list as m
from classes.constants import *
from classes.generic import *
import util.serialCOM as com
from threading import Thread
from time import sleep

def create_serial_frame(self):
    self.frame_serial = CTkFrame(self, fg_color=BG_COLOR_1)

    self.button_serial = CTkButton(self.frame_serial, command=lambda: toggle_serial(self), font=self.font_text, text='Connect')
    self.button_serial.pack(pady=20, padx=10)

    self.main_menu = CTkButton(self.frame_serial, command=self.generic.back2main, font=self.font_text, text='Main menu',
                               fg_color=ERR_COLOR, hover_color=ERR_COLOR_HOVER)
    self.main_menu.pack(pady=(0, 20), padx=10)


def toggle_serial(self):
    if com.isListening:
        com.endListening()
        self.button_serial.configure(text='Open serial port')
        self.serial_label.configure(text_color='red', text='Offline')
        return

    serialThread = Thread(target=com.startListening)
    serialThread.start()
    sleep(1.5)
    if com.isListening:
        self.serial_label.configure(text_color='green', text='Online')
        self.button_serial.configure(text='Close serial port')
