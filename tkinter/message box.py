from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("message box")
def popup():
    messagebox.showinfo("This is my popup","Hello World")
Button(root,text="popup",command=popup).pack()
root.mainloop()