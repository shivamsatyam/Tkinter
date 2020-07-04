from tkinter import *

window = Tk()

def kgConverter():
    kgToGram = float(entry1Value.get()) * 1000
    kgToPounds = float(entry1Value.get()) * 2.20462
    kgToOunces = float(entry1Value.get()) * 35.274

    txt1.delete("1.0", END)
    txt1.insert(END, kgToGram)

    txt2.delete("1.0", END)
    txt2.insert(END, kgToPounds)

    txt2.delete("1.0", END)
    txt3.insert(END, kgToOunces)

lbl1 = Label(window, text="Enter kg")
lbl1.grid(row = 0, column = 0)

entry1Value = StringVar()
entry1 = Entry(window, textvariable = entry1Value)
entry1.grid(row = 0, column = 1)

btn1 = Button(window, text="Convert", command = kgConverter)
btn1.grid(row = 0, column = 2)

txt1 = Text(window, height = 1, width = 20)
txt1.grid(row = 1, column = 0)

txt2 = Text(window, height = 1, width = 20)
txt2.grid(row = 1, column = 1)

txt3 = Text(window, height = 1, width = 20)
txt3.grid(row = 1, column = 2)





window.mainloop()