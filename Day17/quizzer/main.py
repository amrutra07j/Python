from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for dic in question_data:
    question_bank.append(Question(dic["text"], dic["answer"]))

quiz = QuizBrain(question_bank)
quiz.next_question()
print(quiz.has_question())
while quiz.has_question():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score is: {quiz.score} ")
