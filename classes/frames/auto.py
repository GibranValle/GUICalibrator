from customtkinter import CTkFrame, CTkButton, CTkLabel
from classes.constants import *
from shell.MCU import *
from threading import Thread
from calibrations.automaticCalibrations import startAutomaticCalib


class Auto:

    def __init__(self, gui_object: ck):
        self.gui = gui_object

    def only_start(self):
        gui = self.gui
        gui.start_button_auto.configure(state='normal')
        gui.pause_button_auto.configure(state='disabled')
        gui.stop_button_auto.configure(state='disabled')

    def not_only_start(self):
        gui = self.gui
        gui.start_button_auto.configure(state='disabled')
        gui.pause_button_auto.configure(state='normal')
        gui.stop_button_auto.configure(state='normal')

    def only_stop(self):
        gui = self.gui
        gui.start_button_auto.configure(state='disabled')
        gui.pause_button_auto.configure(state='disabled')
        gui.stop_button_auto.configure(state='normal')

    def not_only_pause(self):
        gui = self.gui
        gui.start_button_auto.configure(state='normal')
        gui.pause_button_auto.configure(state='disabled')
        gui.stop_button_auto.configure(state='normal')

    def pushed(self, button):
        gui = self.gui
        self.status = button

        if button == 'pause':
            print('push pause')
            gui.delay.pauseStatus()
            self.not_only_pause()
            return

        elif button == 'stop':
            print('push stoped')
            gui.delay.stopStatus()
            self.only_start()

        elif button == 'start':
            print('push start')
            size = len(gui.selected)
            if size > 0:
                gui.delay.startStatus()
                print('start')
                self.not_only_start()
                Thread(target=startAutomaticCalib, args=[self.gui], daemon=True).start()
            else:
                gui.generic.edit_output('No calib selected!', 'Please select options')

    def select_calib(self):
        gui = self.gui
        option = self.gui.menu_calib.get()
        if option == 'offset':
            click_offset_calib()
        elif option == 'defect':
            click_defect_calib()
        elif option == 'defect solid':
            click_defect_solid_calib()
        elif option == 'pixel defect':
            click_pixel_defect_calib()
        elif option == 'shading':
            click_shading_calib()
        elif option == 'uniformity':
            click_uniformity_calib()

    def create_auto_frame(self):
        gui = self.gui
        gui.toplevel_window = None
        gui.frame_auto = CTkFrame(gui, fg_color=BG_COLOR_1)
        gui.label_auto = CTkLabel(gui.frame_auto, text='Auto Mode', font=gui.font_title)
        gui.label_auto.pack(pady=(5, 0), padx=20)

        gui.selection = CTkButton(gui.frame_auto, command=self.gui.open_toplevel, font=gui.font_text,
                                  text='Select calibs', text_color_disabled=DISABLED_COLOR)
        gui.selection.pack(pady=5, padx=20, fill='x')

        gui.frame_buttons = CTkFrame(gui.frame_auto, fg_color=BG_COLOR_1)
        gui.frame_buttons.pack(pady=5, padx=20, fill='x')

        gui.start_button_auto = CTkButton(gui.frame_buttons, command=lambda: self.pushed('start'), font=gui.font_text,
                                          width=WIDTH_3,
                                          text=PLAY, text_color_disabled=DISABLED_COLOR)
        gui.start_button_auto.grid(row=0, column=1)

        gui.pause_button_auto = CTkButton(gui.frame_buttons, command=lambda: self.pushed('pause'), font=gui.font_text,
                                          width=WIDTH_3,
                                          text=PAUSE, state='disabled', text_color_disabled=DISABLED_COLOR,
                                          fg_color=OK_COLOR, hover_color=OK_COLOR_HOVER)
        gui.pause_button_auto.grid(row=0, column=2, padx=20)

        gui.stop_button_auto = CTkButton(gui.frame_buttons, command=lambda: self.pushed('stop'), font=gui.font_text,
                                         width=WIDTH_3,
                                         text=STOP, state='disabled', text_color_disabled=DISABLED_COLOR,
                                         fg_color=ERR_COLOR, hover_color=ERR_COLOR_HOVER)
        gui.stop_button_auto.grid(row=0, column=3)

        gui.label_output1_auto = CTkLabel(gui.frame_auto, text='M1:', font=gui.font_output, anchor='w', height=20)
        gui.label_output1_auto.pack(padx=20, fill='x')

        gui.label_output2_auto = CTkLabel(gui.frame_auto, text='M2:', font=gui.font_output, anchor='w', height=20)
        gui.label_output2_auto.pack(padx=20, fill='x')

        gui.main_menu = CTkButton(gui.frame_auto, command=gui.generic.back2main, font=gui.font_text,
                                  text='Main menu',
                                  fg_color=ERR_COLOR, hover_color=ERR_COLOR_HOVER)
        gui.main_menu.pack(pady=(5, 10), padx=10)
