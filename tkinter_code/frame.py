from tkinter import *

root=Tk()
root.title("gaju")

frame=LabelFrame(root,text="this is frame",padx=52,pady=52,bg="pink")
#this padding in side the frame
frame.pack(padx=120,pady=120)
#this padding out side the frame
b=Button(frame,text="click here")
b.pack()


root.mainloop()