from tkinter import *
win = Tk()

win.geometry("400x515+20+20")
win.title("Calculator")

# title widgets
title = Label(win, text="≡", fg="Black", font=("Arial", 14))
title.place(x=0, y=10)
title = Label(win, text="Standard mode", fg="Black", font=("Times New Roman", 15))
title.place(x=20, y=10)
zero = Label(win, text="0", fg="Black", font=("Times New Roman", 35))
zero.place(x=350,y=30)

# First function widgets
MC = Button(win, text="MC", fg="Black", bd=3, height= 1, font=("Times New Roman", 12),relief=FLAT)
MC.place(x=30,y=100)
MR = Button(win, text="MR", fg="Black", bd=3, height= 1, font= ("Times New Roman", 12), relief=FLAT)
MR.place(x=90,y=100)
M = Button(win, text="M+", fg="Black", bd=3, height= 1, font= ("Times New Roman", 12), relief=FLAT)
M.place(x=150,y=100)
M = Button(win, text="M-", fg="Black", bd=3, height= 1, font= ("Times New Roman", 12), relief=FLAT)
M.place(x=210,y=100)
MS = Button(win, text="MS", fg="Black", bd=3, height= 1, font= ("Times New Roman", 12), relief=FLAT)
MS.place(x=270,y=100)
M = Button(win, text="M↓", fg="Black", bd=3, height= 1, font= ("Times New Roman", 12), relief=FLAT)
M.place(x=330,y=100)

# First Function numbers
percent = Button(win, text="%", fg="Black", bd=3, height= 2, width= 8 ,font=("Times New Roman", 15))
percent.place(x=1,y=140)
CE = Button(win, text="CE", fg="Black", bd=3, height= 2, width= 8 ,font=("Times New Roman", 15))
CE.place(x=100,y=140)
C = Button(win, text="C", fg="Black", bd=3, height= 2, width= 8 ,font=("Times New Roman", 15))
C.place(x=200,y=140)
Arrowside= Button(win, text="⌫", fg="Black", bd=3, height= 3, width= 13 ,font=("Times New Roman", 9))
Arrowside.place(x=300,y=144)

# Second Row numbers
X = Button(win, text="1/x", fg="Black", bd=3, height= 2, width= 8 ,font=("Times New Roman", 15))
X.place(x=1,y=202)
X = Button(win, text="x^2", fg="Black", bd=3, height= 2, width= 8 ,font=("Times New Roman", 15))
X.place(x=100,y=202)
C = Button(win, text="√x", fg="Black", bd=3, height= 2, width= 8 ,font=("Times New Roman", 15))
C.place(x=200,y=202)
Devide= Button(win, text="÷", fg="Black", bd=3, height= 2, width= 8 ,font=("Times New Roman", 15))
Devide.place(x=300,y=202)

# Third Row numbers
Seven = Button(win, text="7", fg="Black", bd=3, height= 2, width= 8 ,font=("Times New Roman", 15))
Seven.place(x=1,y=264)
Eight = Button(win, text="8", fg="Black", bd=3, height= 2, width= 8 ,font=("Times New Roman", 15))
Eight.place(x=100,y=264)
Nine = Button(win, text="9", fg="Black", bd=3, height= 2, width= 8 ,font=("Times New Roman", 15))
Nine.place(x=200,y=264)
Multiply= Button(win, text="x", fg="Black", bd=3, height= 2, width= 8 ,font=("Times New Roman", 15))
Multiply.place(x=300,y=264)

# Fourth Row numbers
Four = Button(win, text="4", fg="Black", bd=3, height= 2, width= 8 ,font=("Times New Roman", 15))
Four.place(x=1,y=326)
Five = Button(win, text="5", fg="Black", bd=3, height= 2, width= 8 ,font=("Times New Roman", 15))
Five.place(x=100,y=326)
Six = Button(win, text="6", fg="Black", bd=3, height= 2, width= 8 ,font=("Times New Roman", 15))
Six.place(x=200,y=326)
Subtract= Button(win, text="-", fg="Black", bd=3, height= 2, width= 8 ,font=("Times New Roman", 15))
Subtract.place(x=300,y=326)

# Fifth Row numbers
One = Button(win, text="1", fg="Black", bd=3, height= 2, width= 8 ,font=("Times New Roman", 15))
One.place(x=1,y=388)
Two = Button(win, text="2", fg="Black", bd=3, height= 2, width= 8 ,font=("Times New Roman", 15))
Two.place(x=100,y=388)
Three = Button(win, text="3", fg="Black", bd=3, height= 2, width= 8 ,font=("Times New Roman", 15))
Three.place(x=200,y=388)
Addition= Button(win, text="+", fg="Black", bd=3, height= 2, width= 8 ,font=("Times New Roman", 15))
Addition.place(x=300,y=388)

# Sixth Row numbers
AddandMinus = Button(win, text="+/-", fg="Black", bd=3, height= 2, width= 8 ,font=("Times New Roman", 15))
AddandMinus.place(x=1,y=450)
Zero = Button(win, text="0", fg="Black", bd=3, height= 2, width= 8 ,font=("Times New Roman", 15))
Zero.place(x=100,y=450)
Dot = Button(win, text=".", fg="Black", bd=3, height= 2, width= 8 ,font=("Times New Roman", 15))
Dot.place(x=200,y=450)
Equal= Button(win, text="=", fg="Black", bd=3, height= 2, width= 8 ,font=("Times New Roman", 15))
Equal.place(x=300,y=450)
win.mainloop()
