from tkinter import  *
from tkinter import  messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def checker():
    website = entry_web.get()
    email = entry_email.get()
    password = entry_password.get()
    if len(website) == 0 :
        messagebox.showerror(title="Website Error", message="Please enter Website name")
    elif len(password) < 3:
        messagebox.showerror(title="Password Error", message="Please enter Password with length more than 4")
    else:
        save_file()

def save_file():
    website = entry_web.get()
    email = entry_email.get()
    password = entry_password.get()
    is_ok = messagebox.askokcancel(title=website, message=f"Your details: \nemail: {email}\npassword: {password}")
    if is_ok:
        with open("data.txt", "a") as file:
            data = f"{website} | {email} | {password}\n"
            file.write(data)
        entry_web.delete(0, END)
        entry_password.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window =Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(140, 100, image=lock_img)
canvas.grid(column=1, row=0)

label_web = Label(text="Website: ")
label_web.grid(column=0, row=1)
label_email = Label(text="Email/Username: ")
label_email.grid(column=0, row=2)
label_password = Label(text="Password: ")
label_password.grid(column=0, row=3)

entry_web = Entry(width=35)
entry_web.focus()
entry_web.grid(column=1, row=1, columnspan=2)
entry_email = Entry(width=35)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(END, "amrutrajhalageri@gmail.com")
entry_password = Entry(width=21)
entry_password.grid(column=1, row=3)

button_password = Button(text="Generate Password", highlightthickness=0, command=generate_password)
button_password.grid(column=2, row=3)
button_add = Button(text="Add", width=36, command=checker)
button_add.grid(column=1, row=4, columnspan=2)














window.mainloop()