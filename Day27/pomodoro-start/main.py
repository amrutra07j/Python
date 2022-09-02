from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
mark = "✔"
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps, mark
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    mark_label.config(text="")
    mark = ""
    reps = 1
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def time_starter():
    global reps, mark
    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps in [1, 3, 5, 7]:
        count_down(work)
        timer_label.config(text="Work")
        if reps == 1:
            mark_label.config(text="")
            mark = "✔"
        reps += 1
    elif reps in [2, 4, 6]:
        count_down(short_break)
        timer_label.config(text="Break", fg=PINK)
        reps += 1
    else:
        count_down(long_break)
        timer_label.config(text="Long Break", fg=RED)
        mark_label.config(text="")
        reps = 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global mark
    min = count//60
    sec = count%60
    if sec < 10:
        sec = "0" + str(sec)
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        time_starter()
        if reps%2 !=0 :
            mark_label.config(text=mark)
            mark += "✔"
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
canvas.grid(column=1, row=1)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=tomato_pic)
timer_text = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))


timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)
mark_label = Label(text="", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
mark_label.grid(column=1, row=3)


button_start = Button(text="Start", width=8, highlightthickness=0, command=time_starter)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", width=8, highlightthickness=0, command=reset)
button_reset.grid(column=2, row=2)




window.mainloop()