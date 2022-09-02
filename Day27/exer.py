from tkinter import *

window = Tk()
window.title("Miles to Kilometer")
window.minsize(300, 100)

label1 = Label(text="is equal to")
label1.grid(column=0, row=1)
label2 = Label(text="Miles")
label2.grid(column=2, row=0)
label3 = Label(text="KM")
label3.grid(column=2, row=1)
label4 = Label(text="00")
label4.grid(column=1, row=1)

def button_clicked():
    label4.config(text = float(entry.get())*1.609)

entry = Entry()
entry.grid(column=1, row=0)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)







window.mainloop()