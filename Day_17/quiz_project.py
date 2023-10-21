from question_model import Question
from trivia_data import question_data
from quiz_brain import QuizBrain
import html

question_bank = []
for question_dict in question_data:
    question_text = html.unescape(question_dict["question"])
    question_answer = question_dict["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
