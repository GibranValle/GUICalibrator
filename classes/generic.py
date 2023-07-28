from customtkinter import CTk as ck

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
            self.gui.label_output1_m.configure(text=msg1)
        if msg2 != '':
            self.gui.label_output2_m.configure(text=msg2)
