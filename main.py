from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface
import requests
import random

question_data = requests.get('https://opentdb.com/api.php?amount=20&type=boolean').json()['results']

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    options = question['incorrect_answers']
    options.append(question['correct_answer'])
    random.shuffle(options)
    new_question = Question(question_text, question_answer, options)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

#while quiz.still_has_questions():
    #quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
