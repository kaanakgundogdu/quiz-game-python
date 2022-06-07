from cgitb import text
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        true_image = PhotoImage(file="game/images/true.png")
        false_image = PhotoImage(file="game/images/false.png")

        self.score_label = Label(
            text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", "14", "bold"))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg="white", highlightthickness=0)

        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="Question", fill=THEME_COLOR, font=("Arial", 20, "italic"))

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_button = Button(
            image=true_image, highlightthickness=0, command=self.pressed_true_button)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(
            image=false_image, highlightthickness=0, command=self.pressed_false_button)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(
                self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You've reached end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def pressed_true_button(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def pressed_false_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
