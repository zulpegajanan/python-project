from tkinter import *
from tkinter import filedialog
from PIL import  ImageTk,Image
root =Tk()

def open():
    global my_image
    root.filename=filedialog.askopenfilename(title="select a file",filetype=(("png file","*.png"),("all file","*.*")))
    my_label=Label(root,text="root.filename").pack()
    my_image=ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label=Label(image=my_image).pack()


my_btn=Button(root,text="open file",padx=30,pady=15,command=open).pack()

root.mainloop()