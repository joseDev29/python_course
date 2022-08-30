from tkinter import *
from typing import List, Callable


class Calculator:
    def __init__(self, entry: Entry, panel: Frame):
        self.operator: str = ''
        self.buttons: List[Button] = []
        self.entry = entry
        self.panel = panel

    def init(self):
        self.generate_buttons()
        self.render_buttons()

    def reset(self):
        self.entry.delete(0, END)

    def result(self):
        result = str(eval(self.operator))
        self.reset()
        self.entry.insert(END, result)
        self.operator = result

    def set_number_or_operation(self, value: str):
        self.operator += value
        self.reset()
        self.entry.insert(END, self.operator)

    def add_number_or_operation_button(self, value: str):
        new_button = Button(self.panel, text=value,
                            font=('Dosis', 16, 'bold'), bg='azure4',
                            bd=1, width=8
                            )
        new_button.config(command=lambda: self.set_number_or_operation(value))
        self.buttons.append(new_button)

    def add_action_button(self, value: str, action: Callable):
        new_button = Button(self.panel, text=value,
                            font=('Dosis', 16, 'bold'), bg='azure4',
                            bd=1, width=8
                            )
        new_button.config(command=action)
        self.buttons.append(new_button)

    def generate_buttons(self):
        text_list = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', 'x', '0', 'CE', 'Delete', '/']
        for text in text_list:

            if text in '0123456789+-x/':
                self.add_number_or_operation_button(text)
            elif text == 'Delete':
                self.add_action_button('Delete', self.reset)
            elif text == 'CE':
                self.add_action_button('CE', self.result)

    def render_buttons(self):
        curr_row = 1
        curr_column = 0
        for calc_button in self.buttons:
            calc_button.grid(row=curr_row, column=curr_column)

            if curr_column == 3:
                curr_row += 1
                curr_column = 0
            else:
                curr_column += 1
