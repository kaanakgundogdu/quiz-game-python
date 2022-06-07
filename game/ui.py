from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
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
            150, 125, text="Question", fill=THEME_COLOR, font=("Arial", 20, "italic"))

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_button = Button(
            image=true_image, highlightthickness=0)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(
            image=false_image, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.window.mainloop()
