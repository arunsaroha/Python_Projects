from tkinter import *

def convert():
    miles = float(inputs.get())
    kms = Label(text=miles*1.609)
    kms.grid(column=1, row=1)

window = Tk()
window.title("Mile to Km Converter")

label = Label(text="is equal to ")
label.grid(column=0, row=1)

mile = Label(text="Miles")
mile.grid(column=2, row=0)

km = Label(text="Km")
km.grid(column=2, row=1)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

inputs = Entry()
inputs.grid(column=1, row=0)


window.mainloop()