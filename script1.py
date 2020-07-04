from tkinter import *

window = Tk()

def kmToMiles():
    miles = float(entry1Value.get()) * 1.6
    txt1.insert(END, miles)

btn1 = Button(window, text="Execute", command = kmToMiles)
btn1.grid(row = 0, column = 0)


entry1Value = StringVar()
entry1 = Entry(window, textvariable = entry1Value)
entry1.grid(row = 0, column = 1)

txt1 = Text(window, height = 1, width = 20)
txt1.grid(row = 0, column = 2)



window.mainloop()