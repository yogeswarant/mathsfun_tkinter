from tkinter import *
from mathsfunlib.qgenerator import generate_questions
from mathsfunlib.qgenerator import QType

SCREEN_GEOMETRY = "500x500"


class QuizScreen(object):

    def __init__(self, question_generator, timeout_seconds):
        self.screen = Tk()
        self.screen.geometry(SCREEN_GEOMETRY)
        self.screen.title("Maths speed test")
        self.question_generator = question_generator
        self.qlabel = None
        self.timervar = StringVar()
        self.questionvar = StringVar()
        self.answervar = StringVar()
        self.timer_label = Label(textvar=self.timervar, width=20)
        self.question_label = Label(textvar=self.questionvar, font="Verdana 36 bold", width=10)
        self.timer_label.place(x=320, y=50)
        self.question_label.place(x=100, y=100)
        self.aentry = Entry(textvar=self.answervar, validate='all',
                            validatecommand=(self.screen.register(self.numinput), '%P'),
                            font="Verdana 36 bold", width=6)
        self.aentry.bind('<Return>', self.answer)
        self.aentry.place(x=100, y=200)
        self.aentry.focus_set()
        self.abutton = Button(text="Answer", width=8, height=3, command=lambda: self.answer(None))
        self.abutton.place(x=300, y=200)
        self.end_button = Button(text="End", width=8, height=3, command=self.end)
        self.end_button.place(x=20, y=400)
        self.timeout_seconds = timeout_seconds
        self.remaining_seconds = self.timeout_seconds
        self.screen.after(1000, self.tick_timer)
        self.question = self.next_question()
        self.results = []
        self.ended = False

    def end(self):
        self.ended = True
        print("RESULT:")
        print(self.results)

    def answer(self, event):
        print("ANS")
        answer = self.answervar.get()
        status = "Wrong"
        if answer and int(answer) == self.question.get_answer():
            status = "Correct"
        self.results.append({'question': self.question.get_question(),
                             'answer': self.question.get_answer(),
                             'your_answer': answer,
                             'status': status})
        self.answervar.set('')
        self.next_question()
        self.aentry.focus_set()

    def numinput(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False

    def next_question(self):
        print("NQ")
        self.question = next(self.question_generator)
        self.questionvar.set(self.question.get_question())
        self.remaining_seconds = self.timeout_seconds
        return self.question

    def tick_timer(self):
        if self.ended:
            return

        print("Tick")
        timer = "{} second remaining".format(self.remaining_seconds)
        timer = timer.rjust(20)
        if self.remaining_seconds == 1:
            self.next_question()
        else:
            self.remaining_seconds -= 1
        self.timervar.set('')
        self.timervar.set(timer)
        self.screen.after(1000, self.tick_timer)

    def get_results(self):
        return self.results

    def show(self):
        self.screen.mainloop()


if __name__ == '__main__':
    qgen = generate_questions([1, 2], [QType.MULTIPLICATION, QType.XMULTIPLICATION])
    qs = QuizScreen(qgen, 10)
    qs.show()
