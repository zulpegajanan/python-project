from tkinter import *
from tkinter import filedialog
from PIL import  ImageTk,Image
root =Tk()
root.title("gajanan")
root.iconbitmap('pics.jpg')
root.geometry("400x400")#there multiplication denotes x alphabets not *


vertical=Scale(root,from_=0, to=100,bg="green",fg="white").pack()

Scale(root,from_=0, to=100,orient=HORIZONTAL).pack()




root.mainloop()