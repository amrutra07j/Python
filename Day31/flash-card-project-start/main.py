import random
from tkinter import *
import pandas

i = 0
changer = None
BACKGROUND_COLOR = "#B1DDC6"
FONT_LANG = ("Arial", 40, "italic")
FONT_LANG_TEXT = ("Arial", 60, "bold")
#--------------------------------------------------------capture_data--------------------------------------

lang_data = pandas.read_csv("data/English_to_Kannada - Sheet1.csv")
english_data = lang_data.English.to_list()
kannada_data = lang_data.Kannada.to_list()
yet_to_learn_data = []
# -----------------------------------------------------------------------------func-----------------------------

def card_change_to_back():
    global i
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_text, text="Kannada", fill="white")
    canvas.itemconfig(lang_text, text=kannada_data[i], fill="white")
    # window.after_cancel(changer)


def card_change_to_front():
    global i, changer
    window.after_cancel(changer)
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(card_text, text="English", fill="black")
    i = random.randint(0, len(english_data)-1)
    canvas.itemconfig(lang_text, text=english_data[i], fill="black")
    changer = window.after(3000, func=card_change_to_back)


def update_learn():
    english_data.remove(english_data[i])
    kannada_data.remove(kannada_data[i])
    print(len(english_data))
    card_change_to_front()


# -------------------------------------------------UI-----------------------------------------------------------------
window = Tk()
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

changer = window.after(3000, func=card_change_to_back)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 280, image=card_front)
card_text = canvas.create_text(400, 150, text="English", font=FONT_LANG)
canvas.grid(column=0, row=0, columnspan=2)
lang_text = canvas.create_text(400, 263, text="", font=FONT_LANG_TEXT)




wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")
button_wrong = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=card_change_to_back)
button_wrong.grid(column=0, row=1)
button_right = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=update_learn)
button_wrong.grid(column=0, row=1)
button_right.grid(column=1, row=1)

card_change_to_front()

window.mainloop()
