from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
CHECK_MARK_IMAGE_PATH = "images/true.png"
CROSS_IMAGE_PATH = "images/false.png"
TEXT_FONT = ('Arial', 20, 'italic')
timer = None

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(bg=THEME_COLOR, font=('Arial', 15, 'normal'), fg='white')
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(bg='white', width=300, height=250)
        self.text = self.canvas.create_text(
            150,
            125,
            font=TEXT_FONT,
            fill=THEME_COLOR,
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        check_mark_img = PhotoImage(file=CHECK_MARK_IMAGE_PATH)
        self.true_button = Button(
            image=check_mark_img,
            highlightthickness=0,
            command=lambda: self.trigger_answer_checker('True')
        )
        self.true_button.grid(row=2, column=0)

        cross_img = PhotoImage(file=CROSS_IMAGE_PATH)
        self.false_button = Button(
            image=cross_img,
            highlightthickness=0,
            command=lambda: self.trigger_answer_checker('False')
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.update_score()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.print_end()

    def update_score(self):
        new_score = self.quiz.score
        self.score_label.config(text=f'Score: {new_score}')

    def trigger_answer_checker(self, code: str):

        global timer

        if timer is not None:
            self.window.after_cancel(timer)

        if self.quiz.check_answer(code):
            self.canvas.config(bg='green')
            self.update_score()
            timer = self.window.after(2000, self.get_next_question)
        else:
            self.canvas.config(bg='red')
            self.update_score()
            timer = self.window.after(2000, self.get_next_question)

    def print_end(self):
        self.true_button.config(state='disabled')
        self.false_button.config(state='disabled')
        self.canvas.itemconfig(self.text, text='Congratulations!\nYou completed the quiz!')
