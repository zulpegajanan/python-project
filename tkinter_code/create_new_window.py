from tkinter import *
root=Tk()

def open():
    top = Toplevel()  # create newnwindow
    lbl = Label(top, text="this is secound window").pack()  # print hello in new window
    #btn2=Button(top,text="destroy secound window",command=top.destroy()).pack()

btn=Button(root,text="open secound window",command=open,bg="blue",fg="white").pack()



root.mainloop()