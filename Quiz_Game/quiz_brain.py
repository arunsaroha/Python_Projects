class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        final_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False) ")
        self.check_answer(final_answer, current_question.answer)

    def check_answer(self, ans1, ans2):
        if ans1.lower() == ans2.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")

        print(f"The correct answer was: {ans2}")
        print(f"Your current score is: {self.score} / {self.question_number}")
        print("\n")
