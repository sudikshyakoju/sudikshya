from tkinter import *
root =Tk()
MODES=[
    ("pepperoni","pepperoni"),
    ("cheese","cheese"),
    ("mushroom","mushroom")
]

pizza= StringVar()
pizza.set("pepperoni")
for text, mode in MODES:
    Radiobutton(root, text=text,variable=pizza,value=mode).pack(anchor=W)

def clicked(value):
    myLabel=Label(root,text=value)
    myLabel.pack()

mybutton= Button(root,text="click",command=lambda :clicked(pizza.get())).pack()
root.mainloop()
