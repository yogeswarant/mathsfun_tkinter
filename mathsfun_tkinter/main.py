from mathsfun_tkinter.config_screen import ConfigScreen
from mathsfun_tkinter.quiz_screen import QuizScreen
from mathsfun_tkinter.results_screen import ResultsScreen
from mathsfunlib.qgenerator import generate_questions
from tkinter import Tk


screen = Tk()


def on_quiz_close(qs):
    results = qs.get_results()
    duration = qs.get_duration()
    ResultsScreen(screen, results, duration)


def on_config_close(cs):
    print("On config close")
    question_generator = generate_questions(cs.get_select_tables(), cs.get_selected_operations(), cs.get_total_questions())
    timeout_seconds = cs.get_timer()
    total_questions = cs.get_total_questions()
    QuizScreen(screen, question_generator, total_questions, timeout_seconds, on_quiz_close)


def main():
    ConfigScreen(screen, on_config_close)
    screen.mainloop()


if __name__ == '__main__':
    main()
