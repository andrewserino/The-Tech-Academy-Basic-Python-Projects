# Author:   Andrew Serino
#
# Purpose:  Drill from Tech Academy in creating a GUI, using Tkinter GUI Module,
#           using Tkinter Parent and Child relationships.


from tkinter import *
import tkinter as tk


# Importing other modules so we can have access to them

import drill_checkfiles_gui
import drill_checkfiles_func


# Frame is the Tkinter frame class that our own class will inherit from


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define our master frame configuration
        self.master = master
        self.master.minsize(600,200) #(Height, Width)
        self.master.maxsize(600,200)
        # This CenterWindow method will center our app on the user's screen
        drill_checkfiles_func.center_window(self,600,200)
        self.master.title("Check files")
        self.master.configure(bg="#F0F0F0")
        # This protocal method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: drill_checkfiles_func.ask_quit(self))
        arg = self.master

        # Load in the GUI widgets from a separate module,
        # Keeping your code comparmentalized and clutter free
        drill_checkfiles_gui(self)




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
        
