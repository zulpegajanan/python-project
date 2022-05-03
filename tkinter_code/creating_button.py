from tkinter import *
root = Tk()
def myclick():
    mylabel=Label(root, text="you clicked the button", bg="orange", fg="green")
    mylabel.pack()
mybutton=Button(root,text="click here",padx=50,pady=20,command=myclick,fg="blue",bg="red")
mybutton.pack()
root.mainloop()