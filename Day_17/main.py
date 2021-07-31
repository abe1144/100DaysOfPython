from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question_dict in question_data:
    question_bank.append(
        Question(question_dict["text"], question_dict["answer"]))


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print("Your final score was: {}/{}".format(quiz.score, len(quiz.question_list)))
