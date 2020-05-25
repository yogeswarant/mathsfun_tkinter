from tkinter import *
from datetime import timedelta

SCREEN_GEOMETRY = "1200x800"
RESULT_BASE_X = 20
RESULT_BASE_Y = 60 + 30
MAX_ROW_COUNT = 25


class ResultsScreen(object):
    def __init__(self, parent, results, duration):
        self.screen = parent
        self.screen.geometry(SCREEN_GEOMETRY)
        self.frame = Frame(parent, width=1200, height=800)
        self.frame.place(x=0, y=0)
        self.results = results
        self.duration = duration
        self.header_label = Label(self.frame, text="Speed Test Result", font="Verdana 30 bold")
        self.header_label.place(x=5, y=5)
        self.summaryvar = StringVar()
        self.summary_label = Label(self.frame, textvar=self.summaryvar, font="Verdana 15 bold")
        self.summary_label.place(x=20, y=60)
        self.show_results()

    def show_results(self):
        correct = 0
        wrong = 0
        for index, result in enumerate(self.results):
            x = RESULT_BASE_X + (int(index / MAX_ROW_COUNT) * 350)
            y = RESULT_BASE_Y + ((index % MAX_ROW_COUNT) * 25)
            index_bg = "green"
            question_bg = "white"
            your_answer_bg = "white"
            status_bg = "green"
            if result['status'] != 'Correct':
                index_bg = "red"
                question_bg = "yellow"
                your_answer_bg = "yellow"
                status_bg = "red"
                wrong += 1
            else:
                correct += 1

            print("index={} x={} y={}".format(index, x, y))
            iw = 3
            index_label = Label(self.frame, text="{}.".format(index + 1), width=iw, height=1, bg=index_bg)
            index_label.place(x=x, y=y)

            qw = 10
            qtext = result['question'].replace('_', str(result['answer']))
            question_label = Label(self.frame, text=qtext, width=qw, height=1, bg=question_bg)
            question_label.place(x=x + (iw * 10), y=y)

            yw = 12
            your_answer_text = "Your answer: {}".format(result['your_answer'])
            your_answer_label = Label(self.frame, text=your_answer_text, width=yw, height=1, bg=your_answer_bg)
            your_answer_label.place(x=x + ((iw + qw) * 10), y=y)

            sw = 6
            status_label = Label(self.frame, text=result['status'], width=sw, height=1, bg=status_bg)
            status_label.place(x=x + ((iw + qw + yw) * 10), y=y)
            print("{}. {}".format(index, result))

        self.summaryvar.set("Duration: {} Total: {}  Correct: {} Wrong: {}".format(
            str(timedelta(seconds=self.duration)), correct+wrong, correct, wrong))


if __name__ == '__main__':
    r = [{'question': '9 x 2 = _', 'answer': 18, 'your_answer': '18', 'status': 'Correct'},
     {'question': '1 x _= 1', 'answer': 1, 'your_answer': '1', 'status': 'Correct'},
     {'question': '_ x 1 = 5', 'answer': 5, 'your_answer': '', 'status': 'Wrong'},
     {'question': '_ x 1 = 3', 'answer': 3, 'your_answer': '3', 'status': 'Correct'},
     {'question': '3 x 1 = _', 'answer': 3, 'your_answer': '3', 'status': 'Correct'},
     {'question': '_ x 1 = 11', 'answer': 11, 'your_answer': '', 'status': 'Wrong'},
     {'question': '_ x 1 = 2', 'answer': 2, 'your_answer': '2', 'status': 'Correct'},
     {'question': '8 x _= 16', 'answer': 2, 'your_answer': '2', 'status': 'Correct'}] * 8

    screen = Tk()
    rs = ResultsScreen(screen, r, duration=120)
    screen.mainloop()
