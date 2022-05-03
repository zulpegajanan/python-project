from tkinter import *
from tkinter import messagebox
root=Tk()
def popup():
    #showinfo,showwarning,showerror,askquestion,askyesno,askokcancel
    messagebox.askquestion("this is popup","hii gajanan")

Button(root,text="popup",command=popup).pack()












root.mainloop()