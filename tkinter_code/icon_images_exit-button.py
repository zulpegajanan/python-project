from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("GAJANAN")
root.iconbitmap("https://www.google.com/search?q=image&rlz=1C1CHBF_enIN882IN882&tbm=isch&source=iu&ictx=1&vet=1&fir=nH5liarSz56duM%252C0JWe7yDOKrVFAM%252C_%253Bn5hAWsQ-sgKo_M%252C-UStXW0dQEx4SM%252C_%253BuD-WKhoPb7taoM%252CVjlu6XxRvRb4lM%252C_%253BqXynBYpZpHkhWM%252C4O2GvGuD-Cf09M%252C_%253Bz4_uU0QB2pe-SM%252C7SySw5zvOgPYAM%252C_%253BxE4uU8uoFN00aM%252CpEU77tdqT8sGCM%252C_%253BMOAYgJU89sFKnM%252CygIoihldBPn-LM%252C_%253BQOZymhPf48LDYM%252CibTdn4unYxO9nM%252C_%253B2DNOEjVi-CBaYM%252CAOz9-XMe1ixZJM%252C_%253B0DzWhtJoQ1KWgM%252CcIQ7wXCEtJiOWM%252C_%253BbDjlNH-20Ukm8M%252CG9GbNX6HcZ2O_M%252C_%253BgqzX1TfESdsqZM%252CH2EgTD7zoxSjyM%252C_&usg=AI4_-kQSCY6waZ_jHav07jSht6miIV3Mqg&sa=X&ved=2ahUKEwiA5Lf2wsD3AhUTCKYKHanFBXYQ9QF6BAgIEAE#imgrc=n5hAWsQ-sgKo_M")

my_img=ImageTk.PhotoImag(Image.open("pics.jpg"))
my_label=Label(image=my_img)
my_label.pack()

b1=Button(root,text="exit program ", command=root.quit())
b1.pack()





root.mainloop()