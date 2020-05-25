from tkinter import *
from mathsfunlib.qgenerator import generate_questions
from mathsfunlib.qgenerator import QType

SCREEN_GEOMETRY = "500x500"


class QuizScreen(object):

    def __init__(self, parent, question_generator, total_questions, timeout_seconds, on_close):
        print("{} {}".format(question_generator, timeout_seconds))
        self.screen = parent
        self.screen.geometry(SCREEN_GEOMETRY)
        self.screen.title("Maths speed test")
        self.frame = Frame(parent, width=500, height=500)
        self.frame.place(x=0, y=0)
        self.question_generator = question_generator
        self.total_questions = total_questions
        self.qlabel = None
        self.timervar = StringVar()
        self.questionvar = StringVar()
        self.answervar = StringVar()
        self.timer_label = Label(self.frame, textvar=self.timervar, width=20)
        self.question_label = Label(self.frame, textvar=self.questionvar, font="Verdana 36 bold", width=10)
        self.timer_label.place(x=320, y=50)
        self.question_label.place(x=100, y=100)
        self.aentry = Entry(self.frame, textvar=self.answervar, validate='all',
                            validatecommand=(self.frame.register(self.numinput), '%P'),
                            font="Verdana 36 bold", width=6)
        self.aentry.bind('<Return>', self.answer)
        self.aentry.place(x=100, y=200)
        self.aentry.focus_set()
        self.abutton = Button(self.frame, text="Answer", width=8, height=3, command=lambda: self.answer(None))
        self.abutton.place(x=300, y=200)
        self.end_button = Button(self.frame, text="End", width=8, height=3, command=self.end)
        self.end_button.place(x=20, y=400)
        self.timeout_seconds = timeout_seconds
        self.remaining_seconds = self.timeout_seconds
        self.results = []
        self.ended = False
        self.on_close = on_close
        self.statusvar = StringVar()
        self.status_label = Label(self.frame, textvar=self.statusvar)
        self.status_label.place(x=150, y=400)
        self.correct = 0
        self.wrong = 0
        self.update_status()
        self.update_timer()
        self.question = self.next_question()
        self.frame.after(1000, self.tick_timer)

    def end(self):
        self.ended = True
        print("RESULT:")
        print(self.results)
        self.on_close(self)

    def update_status(self):
        so_far = self.correct + self.wrong
        remaining = self.total_questions - so_far
        self.statusvar.set("So far: {} Remaining: {} Correct: {} Wrong: {}".format(so_far,
                                                                                   remaining,
                                                                                   self.correct,
                                                                                   self.wrong))

    def answer(self, event):
        print("ANS")
        answer = self.answervar.get()
        status = "Wrong"
        if answer and int(answer) == self.question.get_answer():
            status = "Correct"
            self.correct += 1
        else:
            self.wrong += 1
        self.results.append({'question': self.question.get_question(),
                             'answer': self.question.get_answer(),
                             'your_answer': answer,
                             'status': status})
        self.answervar.set('')
        self.aentry.focus_set()

    def numinput(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False

    def next_question(self):
        try:
            print("NQ")
            self.question = next(self.question_generator)
            self.questionvar.set(self.question.get_question())
            self.remaining_seconds = self.timeout_seconds
            return self.question
        except StopIteration:
            self.end()

    def update_timer(self):
        timer = "{} second remaining".format(self.remaining_seconds)
        timer = timer.rjust(20)
        self.timervar.set('')
        self.timervar.set(timer)

    def tick_timer(self):
        if self.ended:
            return

        print("Tick")
        if self.remaining_seconds == 1:
            self.answer(None)
            self.update_status()
            self.next_question()
        else:
            self.remaining_seconds -= 1

        self.update_timer()
        self.frame.after(1000, self.tick_timer)

    def get_results(self):
        return self.results


if __name__ == '__main__':
    screen = Tk()
    qgen = generate_questions([1, 2], [QType.MULTIPLICATION, QType.XMULTIPLICATION], total_questions=5)
    qs = QuizScreen(screen, qgen, total_questions=5, timeout_seconds=5, on_close=lambda x: screen.destroy())
    screen.mainloop()
