def clearScreen(self):
    self.frame_serial.pack_forget()
    self.frame_auto.pack_forget()
    self.frame_manual.pack_forget()
    self.frame_utils.pack_forget()
    self.frame_main.pack_forget()


def back2main(self):
    clearScreen(self)
    self.frame_main.pack(pady=20, padx=20, fill='x')


def open_serial_config(self):
    clearScreen(self)
    self.frame_serial.pack(pady=20, padx=20, fill='x')


def display_main_frame(self):
    clearScreen(self)
    self.frame_main.pack(pady=(3, 20), padx=20, fill='x')


def display_serial_frame(self):
    clearScreen(self)
    self.frame_serial.pack(pady=(5, 15), padx=20, fill='x')


def display_manual_frame(self):
    clearScreen(self)
    self.frame_manual.pack(pady=(5, 15), padx=20, fill='x')


def display_auto_frame(self):
    clearScreen(self)
    self.frame_auto.pack(pady=(5, 15), padx=20, fill='x')


def display_utils_frame(self):
    clearScreen(self)
    self.frame_utils.pack(pady=(5, 15), padx=20, fill='x')
