
from tkinter import *

root =Tk()
root.title("gajanan")
root.iconbitmap('pics.jpg')
root.geometry("400x400")#there multiplication denotes x alphabets not *

var=StringVar
c=Checkbutton(root, text="this is check box", variable=var)
c.select() #by default value is checked
#c.select()
c.pack()



root.mainloop()