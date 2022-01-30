from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", "20", "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.title("Quizzler")

        self.quiz_brain = quiz_brain
        self.score = self.quiz_brain.score

        self.score_text = StringVar()
        self.score_text.set(f"Score: {self.score}")
        self.score_label = Label(textvariable=self.score_text)
        self.score_label.config(bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas_text = self.canvas.create_text(150, 125, text="test", font=FONT, fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.next()

        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")

        self.true_button = Button(command=self.true_button, image=true_img, borderwidth=0, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(command=self.false_button, image=false_img, borderwidth=0, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()

    def next(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            next_question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.canvas_text, text=next_question)
            self.score_text.set(f"Score: {self.quiz_brain.score}")
        else:
            self.canvas.itemconfig(self.canvas_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button(self):
        self.give_feedback(self.quiz_brain.check_answer("True"))

    def false_button(self):
        self.give_feedback(self.quiz_brain.check_answer("False"))

    def give_feedback(self, correct: bool):

        if correct:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.next)
