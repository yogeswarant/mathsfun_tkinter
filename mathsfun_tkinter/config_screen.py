from tkinter import *
from mathsfunlib.qgenerator import QType

FIRST_SECTION_Y = 30
SECOND_SECTION_Y = 80
THIRD_SECTION_Y = 110
SCREEN_GEOMETRY = "500x400"


class ConfigScreen(object):

    def __init__(self):
        self.screen = Tk()
        self.screen.geometry(SCREEN_GEOMETRY)
        self.screen.title("Maths speed test - Config")
        self.multiplication = IntVar()
        self.division = IntVar()
        self.addition = IntVar()
        self.subtraction = IntVar()
        self.all_operations = IntVar()
        self.tables = []
        self.all_tables = IntVar()
        self.table_options = False
        self.timer = StringVar()
        self.digits = IntVar()
        self.multiplication.set(1)

        mul = Checkbutton(self.screen, text='Multiplication', variable=self.multiplication,
                          onvalue=1, offvalue=0)
        mul.place(x=20, y=FIRST_SECTION_Y, height=25)
        div = Checkbutton(self.screen, text='Division', variable=self.division, onvalue=1,
                          offvalue=0)
        div.place(x=140, y=FIRST_SECTION_Y, height=25)
        add = Checkbutton(self.screen, text='Addition', variable=self.addition,
                          onvalue=1, offvalue=0)
        add.place(x=240, y=FIRST_SECTION_Y, height=25)
        sub = Checkbutton(self.screen, text='Subtraction', variable=self.subtraction,
                          onvalue=1, offvalue=0)
        sub.place(x=320, y=FIRST_SECTION_Y, height=25)

        all_ops = Checkbutton(self.screen, text='All', variable=self.all_operations,
                              onvalue=1, offvalue=0, command=self.select_all_operations)
        all_ops.place(x=430, y=FIRST_SECTION_Y, height=25)

        self.show_tables()

        digits_label = Label(text="Select digits:")
        digits_label.place(x=220, y=SECOND_SECTION_Y)
        self.digits.set(3)
        supported_digits = ["{}".format(x) for x in range(1, 6)]
        digits_option = OptionMenu(self.screen, self.digits, *supported_digits)
        digits_option.place(x=230, y=THIRD_SECTION_Y)

        qtime_label = Label(text="Select time:")
        qtime_label.place(x=330, y=SECOND_SECTION_Y)
        self.timer.set('10 Seconds')
        supported_timer = ["{} Seconds".format(x) for x in range(5, 16)]
        timer_option = OptionMenu(self.screen, self.timer, *supported_timer)
        timer_option.place(x=330, y=THIRD_SECTION_Y)

        start = Button(self.screen, text="Start", command=self.start)
        start.place(x=210, y=300)

    def start(self):
        print(self.get_select_tables())
        print(self.get_selected_operations())
        print(self.get_digits())
        print(self.get_timer())

    def select_all_operations(self):
        if self.all_operations.get():
            self.multiplication.set(1)
            self.division.set(1)
            self.addition.set(1)
            self.subtraction.set(1)
        else:
            self.multiplication.set(0)
            self.division.set(0)
            self.addition.set(0)
            self.subtraction.set(0)

    def get_digits(self):
        return self.digits.get()

    def get_timer(self):
        return int(self.timer.get().split()[0])

    def show_tables(self):
        basex = 30
        basey = SECOND_SECTION_Y
        Label(text="Select tables:").place(x=basey, y=SECOND_SECTION_Y)
        basex += 30
        basey = THIRD_SECTION_Y
        for i in range(12):
            table_selection = IntVar()
            self.tables.append(table_selection)
            if i < 5:
                table_selection.set(1)
            table_check = Checkbutton(self.screen, text='{}'.format(i + 1),
                                      variable=self.tables[i], onvalue=1, offvalue=0)

            x = basex + ((i % 3)*50)
            y = basey + (int(i / 3) * 30)
            table_check.place(x=x, y=y)

        table_check = Checkbutton(self.screen, text='All tables',
                                  variable=self.all_tables,
                                  command=self.select_all)
        all_y = y + 30
        table_check.place(x=basex, y=all_y)

    def select_all(self):
        for i in range(12):
            self.tables[i].set(self.all_tables.get())

    def get_select_tables(self):
        selected_tables = []
        for index, selected in enumerate(self.tables):
            if not selected.get():
                continue
            selected_tables.append(index + 1)
        return selected_tables

    def get_selected_operations(self):
        operations = []
        if self.multiplication.get():
            operations.extend([QType.MULTIPLICATION, QType.XMULTIPLICATION])
        if self.division.get():
            operations.extend([QType.DIVISION, QType.XDIVISION])
        return operations

    def show(self):
        self.screen.mainloop()


if __name__ == '__main__':
    cs = ConfigScreen()
    cs.show()
