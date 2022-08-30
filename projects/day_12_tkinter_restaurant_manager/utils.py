from tkinter import *
from typing import List, Tuple, Callable


def validate_check_list(check_list: List[IntVar], entry_list: List[Entry], entry_value_list: List[StringVar]):
    for index, check in enumerate(check_list):
        entry = entry_list[index]
        entry_value = entry_value_list[index]

        if check.get() == 1:
            entry.config(state=NORMAL)
            entry_value.get() == '0' and entry.delete(0, END)

            entry.focus()
        else:
            entry.config(state=DISABLED)
            entry_value.set('0')


def generate_list_actions(item_list: List[str],
                          panel: LabelFrame,
                          command: Callable) -> Tuple[List[IntVar], List[Entry], List[StringVar]]:
    check_list: List[IntVar] = []
    entry_list: List[Entry] = []
    entry_value_list: List[StringVar] = []
    for index, item in enumerate(item_list):
        check_list.append(IntVar())
        # check_list[index] = IntVar()
        item_checkbutton = Checkbutton(panel, text=item, font=('Dosis', 19, 'bold'),
                                       onvalue=1, offvalue=0, variable=check_list[index],
                                       command=command
                                       )
        item_checkbutton.grid(row=index, column=0, sticky=W)
        entry_value_list.append(StringVar(value='0'))
        # entry_value_list.append(StringVar())
        # entry_value_list[index].set('0')
        entry_list.append(Entry(panel, font=('Dosis', 18, 'bold'), bd=1,
                                width=6, state=DISABLED, textvariable=entry_value_list[index])
                          )
        entry_list[index].grid(row=index, column=1)

    return check_list, entry_list, entry_value_list


def get_total_by_lists(entry_value_list: List[StringVar], price_list: List[float]) -> float:
    total = 0
    for index, entry_value in enumerate(entry_value_list):
        total += float(entry_value.get()) * price_list[index]
    return round(total, 2)


def get_receipt_data_by_list(item_list: List[str],
                             entry_value_list: List[StringVar],
                             price_list: List[float],
                             ) -> str:
    text = ''
    for index, entry_value in enumerate(entry_value_list):
        value = entry_value.get()
        price = price_list[index]
        if value != '0':
            text += f'{item_list[index]}\t\t{value}\t${round(int(value)*price, 2)}\n'
    return text


def reset_entry_value_list(entry_value_list: List[StringVar]):
    for entry_value in entry_value_list:
        entry_value.set('0')


def reset_entry_list(entry_list: List[Entry]):
    for entry in entry_list:
        entry.config(state=DISABLED)


def reset_check_list(check_list: List[IntVar]):
    for check in check_list:
        check.set(0)
