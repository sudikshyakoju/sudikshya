from tkinter import *
root=Tk()

e1=Entry(root, width=50, fg="blue", bg="white", borderwidth=5)
e1.pack()

def myclick():
    textoutput="Hello" + e1.get()
    mylabel=Label(root, text=textoutput)
    mylabel.pack()

mybutton=Button(root, text="click me", command=myclick)
mybutton.pack()

root.mainloop()