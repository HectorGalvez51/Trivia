from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, q_brain: QuizBrain):
        self.quiz = q_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_text = Label(text=f'Score: {self.quiz.score}', fg='white', font=("Arial", 14, 'bold'), background=THEME_COLOR, padx=20, pady=20)
        self.score_text.grid(column=1, row=0)

        self.canvas = Canvas(width=600, height=500, bg='white')
        self.canvas_text = self.canvas.create_text(300, 250, text="Preguntas" , fill=THEME_COLOR, font=("Arial", 25, 'bold'), width=550)
        self.canvas.grid(column=0, row=1, columnspan=2)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, borderwidth=0, highlightthickness=0, pady=20, padx=20, command= self.true_answer)
        self.true_button.grid(column=0, row=2)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, borderwidth=0, highlightthickness=0, command= self.false_answer)
        self.false_button.grid(column=1, row=2, pady=50)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_text.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text=f"Your final score is {self.quiz.score}/20")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def false_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.next_question)

