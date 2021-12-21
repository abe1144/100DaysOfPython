from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(width=300, height=250)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="some text", font=("Arial", 20, 'italic'),
        width=280)
        self.canvas.grid(row=1,column=0, columnspan=2, pady=50)
        #self.canvas.config(padx=20, pady=20)
        true_img = PhotoImage(file='images/true.png')
        false_img = PhotoImage(file='images/false.png')

        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.answer_true)
        self.true_btn.grid(row=2, column=0)
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.answer_false)
        self.false_btn.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()

    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text="Score: {}".format(self.quiz.score))
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've Reached the end of the Quiz!")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def answer_true(self):
        self.user_answer = "true"
        is_right = self.quiz.check_answer(self.user_answer)
        self.give_feedback(is_right)

    def answer_false(self):
        self.user_answer = "false"
        is_right = self.quiz.check_answer(self.user_answer)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
