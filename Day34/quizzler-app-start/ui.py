from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.score = Label(text="score: 0", bg=THEME_COLOR, font=("Arial", 15, "normal"))
        self.score.grid(column=1, row=0)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question = self.canvas.create_text(150, 125, text="Question", font=("Arial", 20, "italic"), width=280)
        IMG_RIGHT = PhotoImage(file="images/true.png")
        IMG_WRONG = PhotoImage(file="images/false.png")
        self.right_button = Button(image=IMG_RIGHT, highlightthickness=0, command=self.right_mark)
        self.right_button.grid(column=0, row=2)
        self.wrong_button = Button(image=IMG_WRONG, highlightthickness=0, command=self.wrong_mark)
        self.wrong_button.grid(column=1, row=2)
        self.question_interface()
        self.window.mainloop()

    def question_interface(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text=f"Quiz Complete\n\nFinal score = {self.quiz.score}")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right_mark(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_mark(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, func=self.question_interface)
