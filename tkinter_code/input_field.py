from tkinter import *
root = Tk()

e = Entry(root,width=50,fg="red")
e.pack()

def myclick():
    mylabel=Label(root, text=e.get()+" you clicked the button", bg="orange", fg="green")
    mylabel.pack()

mybutton=Button(root,text="click me",command=myclick) #don't use myclick()
mybutton.pack()

root.mainloop()
