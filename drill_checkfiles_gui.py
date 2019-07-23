from tkinter import *
import tkinter as tk

# Be sure to import our other modules
# So we can have access to them
import drill_checkfiles_main
import drill_checkfiles_func



def load_gui(self):

    self.lbl_user1 = tk.Label(self.master)
    self.lbl_user1.grid(row=0,column=2,padx=(0,0),pady=(10,0),sticky=N+W)
    self.lbl_user2 = tk.Label(self.master)
    self.lbl_user2.grid(row=0,column=4,padx=(0,0),pady=(10,0),sticky=N+W)

    self.btn_browse1 = tk.Button(self.master,width=12,height=2,text='Browse...',command=lambda: drill_checkfiles_func.addToList(self))
    self.btn_browse1.grid(row=8,column=0,padx(25,0),pady=(45,10),sticky=W)
    self.btn_browse2 = tk.Button(self.master,width=12,height=2,text='Browse...',command=lambda: drill_checkfiles_func.onUpdate(self))
    self.btn_browse2.grid(row=8,column=1,padx(15,0),pady=(45,10),sticky=W)
    self.btn_checkforfiles = tk.Button(self.master,width=12,height=2,text='Check for files...',command=lambda: drill_checkfiles_func.onDelete(self))
    self.btn_checkforfiles.grid(row=8,column=2,padx(35,0),pady=(45,10),sticky=W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program',command=lambda: drill_checkfiles_func.ask_quit(self))
    self.btn_close.grid(row=8,column=4,padx(15,0),pady=(45,10),sticky=E)

    drill_checkfiles_func.create_db(self)
    drill_checkfiles_func.onrefresh(self)





if __name__ == "__main__":
    pass
