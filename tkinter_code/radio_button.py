from tkinter import *
root=Tk()

r=IntVar()
r.set("2")
#deafult position

Radiobutton(root,text="option 1",variable=r,value=1).pack()
Radiobutton(root,text="option 2",variable=r,value=2).pack()
mylabel=Label(root,text=r.get())
mylabel.pack()


root.mainloop()