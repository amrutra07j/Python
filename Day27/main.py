from tkinter import *

window = Tk()
window.title("Dare Here")
window.minsize(500, 300)

my_label = Label(text="First Time", font=("Arial", 24, "bold"))
my_label.pack()

def button_clicked():
    my_label.config(text = input.get())

button = Button(text="Click Me", command=button_clicked)
button.pack()

input = Entry()
input.insert(END, string="Something")
input.pack()

text = Text(height = 5, width = 30)
text.focus()
text.insert(END, "Example of multi-line text entry.")
print(text.get("1.0", END))
text.pack()

def spinbox_used():
    #gets the current value in spinbox.
    button.config(text=spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

def scale_used(value):
    text.insert(END, value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    my_label.config(text=checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    print(fruits.index(item))
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()







window.mainloop()
