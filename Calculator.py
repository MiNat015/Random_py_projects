import tkinter as tk
from tkinter import ttk


class Model:
    """
    class Docs
    """

    def __init__(self):
        self.previous_value = ''
        self.value = ''
        self.operator = ''

    def calculate(self, caption) -> str:
        if caption == 'C':
            self.previous_value = ''
            self.value = ''
            self.operator = ''
        elif isinstance(caption, int):
            self.value += str(caption)
        elif caption == '+/-':
            self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value
        elif caption == '%':
            self.value = str(self.percent(self.value))
        elif caption == '.':
            if caption not in self.value:
                self.value += caption
        elif caption == '=':
            if self.operator == '+':
                self.value = str(self.add(self.previous_value, self.value))
            elif self.operator == '-':
                self.value = str(self.subtract(self.previous_value, self.value))
            elif self.operator == '*':
                self.value = str(self.multiply(self.previous_value, self.value))
            elif self.operator == '/':
                self.value = str(self.divide(self.previous_value, self.value))
        else:
            if self.value:
                self.operator = caption
                self.previous_value = self.value
                self.value = ''

        return self.value

    def percent(self, value):
        value = float(value)
        return value/100

    def add(self, value1, value2):
        value1 = float(value1)
        value2 = float(value2)
        return value1 + value2

    def subtract(self, value1, value2):
        value1 = float(value1)
        value2 = float(value2)
        return value1 - value2

    def multiply(self, value1, value2):
        value1 = float(value1)
        value2 = float(value2)
        return value1 * value2

    def divide(self, value1, value2):
        value1 = float(value1)
        value2 = float(value2)
        return value1 / value2


class View(tk.Tk):
    """
    class Docs
    """

    PAD = 10

    MAX_BUTTONS_PER_ROW = 4

    button_captions = [
        'C', '+/-', '%', '/',
        7, 8, 9, '*',
        4, 5, 6, '-',
        1, 2, 3, '+',
        0, '.', '='
    ]

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.value_var = tk.StringVar()

        self.title("Calculator App")

        self._make_main_frame()
        self._make_entry()
        self._make_buttons()

    def main(self):
        self.mainloop()

    def _make_main_frame(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=self.PAD, pady=self.PAD)

    def _make_entry(self):
        ent = ttk.Entry(self.main_frame, justify='right', textvariable=self.value_var, state=tk.DISABLED)
        ent.pack(fill=tk.BOTH)

    def _make_buttons(self):
        outer_frame = ttk.Frame(self.main_frame)
        outer_frame.pack()

        frame = ttk.Frame(outer_frame)
        frame.pack()

        btn_in_row = 0

        for text in self.button_captions:
            if btn_in_row == self.MAX_BUTTONS_PER_ROW:
                frame = ttk.Frame(outer_frame)
                frame.pack()
                btn_in_row = 0
            btn = ttk.Button(frame, text=text, command=(lambda button=text: self.controller.on_button_click(button)))
            btn.pack(side=tk.LEFT)

            btn_in_row += 1


class Controller:
    """
    class Docs
    """

    def __init__(self):
        self.model = Model()
        self.view = View(self)
        pass

    def main(self):
        self.view.main()

    def on_button_click(self, caption):
        result = self.model.calculate(caption)

        self.view.value_var.set(result)


if __name__ == "__main__":
    calculator = Controller()
    calculator.main()
