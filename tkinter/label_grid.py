from tkinter import *
root=Tk()
mylabel1=Label(root,text="Tkinter program")
mylabel2=Label(root,text="I am Sudikshya")
mylabel3=Label(root,text="This is my program")

mylabel1.grid(row=0,column=0)
mylabel2.grid(row=1,column=5)
mylabel3.grid(row=2,column=7)

root.mainloop()