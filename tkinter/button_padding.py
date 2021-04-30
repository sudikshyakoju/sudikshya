from tkinter import *
root=Tk()

mybutton=Botton(root,text="Click me")
mybutton.pack()

mybutton1=Botton(root,text="Click",state="DISABLE")
mybutton1.pack()

mybutton2=Botton(root,text="Click",padx=50)
mybutton2.pack()

mybutton3=Botton(root,text="Click",padx=50,pady=50)
mybutton3.pack()

root.mainloop()