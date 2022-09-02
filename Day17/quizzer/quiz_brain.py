class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You are cute and it's correct!")
        else:
            print("You are such a useful piece of shit")
        print(f"The correct answer was: {correct_answer}")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        choice = input(f"Q.{self.question_number} : {current_question.text} (True/False): ")
        self.check_answer(choice, current_question.answer)
        print(f"Your score is: {self.score}/{self.question_number}")

    def has_question(self):
        return len(self.question_list) > self.question_number

