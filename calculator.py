from tkinter import *

class MyWindow:
    def __init__(self,win):

    # Widgets
    # Label
        self.lbl1 = Label(win, text="Premise 1:")
        self.lbl1.place(x=85, y=50)
        self.lbl2 = Label(win, text="Premise 2:")
        self.lbl2.place(x=85, y=100)
        self.lbl3 = Label(win, text="Results")
        self.lbl3.place(x=100, y=150)
    # Entry
        self.txt1 = Entry(win, bd="3")
        self.txt1.place(x=150, y=50)
        self.txt2 = Entry(win, bd="3")
        self.txt2.place(x=150, y=100)
        self.txt3 = Entry(win, bd="3")
        self.txt3.place(x=150, y=150)
    # Buttons
        self.btn1 = Button(win, text="Add", bd="3", command=self.add)
        self.btn1.place(x=100, y=200)
        self.btn2 = Button(win, text="Subtract", bd="3", command=self.subtract)
        self.btn2.place(x=150, y=200)
        self.btn3 = Button(win, text="Multiply", bd="3", command=self.multiply)
        self.btn3.place(x=220, y=200)
        self.btn4 = Button(win, text="Divide", bd="3", command=self.divide)
        self.btn4.place(x=290, y=200)

    # Functions
    def add(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 + num2
        self.txt3.insert(END, str(result))

    def subtract(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 - num2
        self.txt3.insert(END, str(result))

    def multiply(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 * num2
        self.txt3.insert(END, str(result))

    def divide(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 / num2
        self.txt3.insert(END, str(result))

window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Simple Calculator")
window.mainloop()
