# def add(a, *args):
#     sum = a
#     for n in args:
#         sum = sum + n
#
#     return sum
#
# print(add(3, 5, 6, 13, 1))
from tkinter import *
window = Tk()
window.minsize(500, 300)

my_label = Label(text="Beautiful", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

button1 = Button(text="Click Me")
button1.grid(column=1, row=1)

button2 = Button(text="Click Me")
button2.grid(column=2, row=0)

entry = Entry()
entry.insert(END, "You Man")
entry.grid(column=3, row=1)






window.mainloop()
