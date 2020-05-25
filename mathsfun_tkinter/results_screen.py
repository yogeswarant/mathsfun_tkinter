from tkinter import *

SCREEN_GEOMETRY = "1200x800"
RESULT_BASE_X = 20
RESULT_BASE_Y = 60
MAX_ROW_COUNT = 25


class ResultsScreen(object):
    def __init__(self, results):
        self.screen = Tk()
        self.screen.geometry(SCREEN_GEOMETRY)
        self.results = results
        self.header_label = Label(text="Speed Test Result", font="Verdana 30 bold")
        self.header_label.place(x=5, y=5)
        self.show_results()

    def show_results(self):
        for index, result in enumerate(self.results):
            x = RESULT_BASE_X + (int(index / MAX_ROW_COUNT) * 350)
            y = RESULT_BASE_Y + ((index % MAX_ROW_COUNT) * 25)
            print("index={} x={} y={}".format(index, x, y))
            iw = 3
            index_label = Label(text="{}.".format(index + 1), width=iw, height=1, bg="red")
            index_label.place(x=x, y=y)

            qw = 10
            qtext = result['question'].replace('_', str(result['answer']))
            question_label = Label(text=qtext, width=qw, height=1, bg="green")
            question_label.place(x=x + (iw * 10), y=y)

            yw = 12
            your_answer_text = "Your answer: {}".format(result['your_answer'])
            your_answer_label = Label(text=your_answer_text, width=yw, height=1, bg="yellow")
            your_answer_label.place(x=x + ((iw + qw) * 10), y=y)

            sw = 6
            status_label = Label(text=result['status'], width=sw, height=1, bg="cyan")
            status_label.place(x=x + ((iw + qw + yw) * 10), y=y)
            print("{}. {}".format(index, result))

    def show(self):
        self.screen.mainloop()


if __name__ == '__main__':
    r = [{'question': '9 x 2 = _', 'answer': 18, 'your_answer': '18', 'status': 'Correct'},
     {'question': '1 x _= 1', 'answer': 1, 'your_answer': '1', 'status': 'Correct'},
     {'question': '_ x 1 = 5', 'answer': 5, 'your_answer': '5', 'status': 'Correct'},
     {'question': '_ x 1 = 3', 'answer': 3, 'your_answer': '3', 'status': 'Correct'},
     {'question': '3 x 1 = _', 'answer': 3, 'your_answer': '3', 'status': 'Correct'},
     {'question': '_ x 1 = 11', 'answer': 11, 'your_answer': '11', 'status': 'Correct'},
     {'question': '_ x 1 = 2', 'answer': 2, 'your_answer': '2', 'status': 'Correct'},
     {'question': '8 x _= 16', 'answer': 2, 'your_answer': '2', 'status': 'Correct'}] * 8

    # r = [{'question': '6 x 2 = _', 'answer': 12, 'your_answer': '12', 'status': 'Correct'}] * 20
    rs = ResultsScreen(r)
    rs.show()
