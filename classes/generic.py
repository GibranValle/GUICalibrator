from customtkinter import CTk as ck


def createMessage(msg, count):
    minutes = count // 60
    secs = count % 60
    text = f'{msg}: {secs}s' if minutes <= 0 else f'{msg}: {minutes}m {secs}s'
    return text


class Generic:
    def __init__(self, gui_object: ck):
        self.gui = gui_object

    def clearScreen(self):
        self.gui.frame_serial.pack_forget()
        self.gui.frame_auto.pack_forget()
        self.gui.frame_manual.pack_forget()
        self.gui.frame_utils.pack_forget()
        self.gui.frame_main.pack_forget()

    def updateGui(self, gui_object: ck):
        self.gui = gui_object

    def back2main(self):
        self.clearScreen()
        self.gui.frame_main.pack(pady=20, padx=20, fill='x')

    def open_serial_config(self):
        self.clearScreen()
        self.gui.frame_serial.pack(pady=20, padx=20, fill='x')

    def display_main_frame(self):
        self.clearScreen()
        self.gui.frame_main.pack(pady=(3, 20), padx=20, fill='x')

    def display_serial_frame(self):
        self.clearScreen()
        self.gui.frame_serial.pack(pady=(5, 15), padx=20, fill='x')

    def display_manual_frame(self):
        self.clearScreen()
        self.gui.frame_manual.pack(pady=(5, 15), padx=20, fill='x')

    def display_auto_frame(self):
        self.clearScreen()
        self.gui.frame_auto.pack(pady=(5, 15), padx=20, fill='x')

    def display_utils_frame(self):
        self.clearScreen()
        self.gui.frame_utils.pack(pady=(5, 15), padx=20, fill='x')

    def edit_output(self, msg1='', msg2=''):
        if msg1 != '':
            self.gui.label_output1_man.configure(text=msg1)
            self.gui.label_output1_auto.configure(text=msg1)

        if msg2 != '':
            self.gui.label_output2_man.configure(text=msg2)
            self.gui.label_output2_auto.configure(text=msg2)

    def clear_output(self):
        self.edit_output(' ', ' ')

    def not_responding(self):
        self.edit_output('BOT NOT RESPONDING!', 'Please verify')
        self.gui.isRunning = False

    def abort_requested(self):
        text1 = 'Exposure aborted'
        text2 = '----------------'
        self.edit_output(text1, text2)
        self.gui.isRunning = False

    def aborted(self):
        text1 = 'Premature end of exposure'
        text2 = 'Please verify system'
        self.edit_output(text1, text2)
        self.gui.isRunning = False

    def abnormal(self):
        text1 = 'Abnormal behavior'
        text2 = 'Please verify system'
        self.edit_output(text1, text2)
        self.gui.isRunning = False

    def under_exposure(self):
        text1 = 'UNDER EXPOSURE...'
        text2 = '----------------'
        self.edit_output(text1, text2)

    def request_end(self):
        text1 = 'Requesting End of exposure'
        self.edit_output(text1)

    def end_manually(self):
        text1 = ' '
        text2 = 'Please end exposure manually'
        self.edit_output(text1, text2)

    def exposure_done(self, total, kind='exposure'):
        text1 = 'Exposure done'
        text2 = createMessage(f'This {kind} took', total)
        self.edit_output(text1, text2)

    def accepted(self, kind='short'):
        text1 = f'Accepted {kind} exposure'
        self.edit_output(text1)

    def exposure_done_exp(self, total, exposures):
        text1 = 'Calibration passed!'
        text2 = createMessage('Time', total)
        self.edit_output(text1, text2 + f' exposures: {exposures}')

    def count(self, exposures):
        text1 = f'Exposures count: {exposures}'
        self.edit_output(text1)
