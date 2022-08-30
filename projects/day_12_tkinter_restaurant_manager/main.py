import datetime
import random
from tkinter import filedialog, messagebox

from calculator import Calculator
from utils import *

# Init
application = Tk()

# view size
# geometry('WidthxHeight+posX+posY')
application.geometry('1200x630+0+0')

# Configure not resize
# resizable(x, y)
application.resizable(False, False)

# App title
application.title('Restaurant Manager')

# Background color
# bg = 'name' | 'rgb'
application.config(bg='burlywood')

# Top panel
# bd = border , relief = FLAT | RAISED | SUNKEN' | GROOVE | RIDGE
top_panel = Frame(application, bd=1, relief=FLAT)
top_panel.pack(side=TOP)

# Title label
title_label = Label(top_panel, text="Restaurant Manager", fg='azure4',
                    font=('Dosis', 58), bg='burlywood', width=27
                    )
title_label.grid(row=0, column=0)

# Left panel
left_panel = Frame(application, bd=1, relief=FLAT)
left_panel.pack(side=LEFT)

# Costs panel
costs_panel = Frame(left_panel, bd=1, relief=FLAT, bg='azure4')
costs_panel.pack(side=BOTTOM)

# Meals panel
meals_panel = LabelFrame(left_panel, text='Meals', font=('Dosis', 19, 'bold'),
                         bd=1, relief=FLAT, foreground='azure4'
                         )
meals_panel.pack(side=LEFT)

# Drinks panel
drinks_panel = LabelFrame(left_panel, text='Drinks', font=('Dosis', 19, 'bold'),
                          bd=1, relief=FLAT, foreground='azure4'
                          )
drinks_panel.pack(side=LEFT)

# Desserts panel
desserts_panel = LabelFrame(left_panel, text='Drinks', font=('Dosis', 19, 'bold'),
                            bd=1, relief=FLAT, foreground='azure4'
                            )
desserts_panel.pack(side=LEFT)

# Right panel
right_panel = Frame(application, bd=1, relief=FLAT)
right_panel.pack(side=RIGHT)

# Calculator panel
calculator_panel = Frame(right_panel, bd=1, relief=FLAT, bg='burlywood')
calculator_panel.pack()

# Calculator panel
calculator_panel = Frame(right_panel, bd=1, relief=FLAT, bg='burlywood')
calculator_panel.pack()

# Receipt panel
receipt_panel = Frame(right_panel, bd=1, relief=FLAT, bg='burlywood')
receipt_panel.pack()

# Receipt panel
receipt_panel = Frame(right_panel, bd=1, relief=FLAT, bg='burlywood')
receipt_panel.pack()

# Actions panel
actions_panel = Frame(right_panel, bd=1, relief=FLAT, bg='burlywood')
actions_panel.pack()

# Products lists
meals_list = ['Chicken', 'Lamb', 'Salmon', 'Kebab', 'Pizza', 'Ravioli', 'Spaghetti', 'Ajiaco']
meals_prices = [1.12, 2.34, 3.56, 2.34, 5.67, 3.45, 2.56, 6.55]
drinks_list = ['Water', 'Soda', 'Beer', 'Juice', 'Cola Cola', 'Wine', 'Vodka', 'Tequila']
drinks_prices = [1.12, 2.34, 3.56, 2.34, 5.67, 3.45, 2.56, 6.55]
desserts_list = ['Ice Cream', 'Fruit', 'Brownie', 'Custard', 'Cake', 'Cookies', 'Banana Split', 'Cinnamon Rolls']
desserts_prices = [1.12, 2.34, 3.56, 2.34, 5.67, 3.45, 2.56, 6.55]


def on_change_check():
    validate_check_list(meals_check_list, meals_entry_list, meals_entry_value_list)
    validate_check_list(drinks_check_list, drinks_entry_list, drinks_entry_value_list)
    validate_check_list(desserts_check_list, desserts_entry_list, desserts_entry_value_list)


meals_check_list, meals_entry_list, meals_entry_value_list = generate_list_actions(
    meals_list, meals_panel, on_change_check)
drinks_check_list, drinks_entry_list, drinks_entry_value_list = generate_list_actions(
    drinks_list, drinks_panel, on_change_check)
desserts_check_list, desserts_entry_list, desserts_entry_value_list = generate_list_actions(
    desserts_list, desserts_panel, on_change_check)


def generate_label_entry_value(panel: Frame, label_text: str) -> Tuple[Label, Entry, StringVar]:
    label = Label(panel, text=label_text, font=('Dosis', 12, 'bold'),
                  bg='azure4',
                  fg='white'
                  )
    value = StringVar(value='0')
    entry = Entry(panel, font=('Dosis', 12, 'bold'), bd=1, width=10,
                  state='readonly', textvariable=value
                  )
    return label, entry, value


# Costs label, entry, value
meals_cost_label, meals_cost_entry, meals_cost_value = generate_label_entry_value(costs_panel, 'Meals cost')
meals_cost_label.grid(row=0, column=0)
meals_cost_entry.grid(row=0, column=1, padx=50)

# Costs label, entry, value
drinks_cost_label, drinks_cost_entry, drinks_cost_value = generate_label_entry_value(costs_panel, 'Drinks cost')
drinks_cost_label.grid(row=1, column=0)
drinks_cost_entry.grid(row=1, column=1, padx=50)

# Costs label, entry, value
desserts_cost_label, desserts_cost_entry, desserts_cost_value = generate_label_entry_value(costs_panel, 'Desserts cost')
desserts_cost_label.grid(row=2, column=0)
desserts_cost_entry.grid(row=2, column=1, padx=50)

# Costs label, entry, value
subtotal_label, subtotal_entry, subtotal_value = generate_label_entry_value(costs_panel, 'Subtotal')
subtotal_label.grid(row=0, column=2)
subtotal_entry.grid(row=0, column=3, padx=50)

# Costs label, entry, value
tax_label, tax_entry, tax_value = generate_label_entry_value(costs_panel, 'Tax')
tax_label.grid(row=1, column=2)
tax_entry.grid(row=1, column=3, padx=50)

# Costs label, entry, value
total_label, total_entry, total_value = generate_label_entry_value(costs_panel, 'Total')
total_label.grid(row=2, column=2)
total_entry.grid(row=2, column=3, padx=50)

# Buttons
buttons_text_list = ['Total', 'Receipt', 'Save', 'Reset']
buttons_list: List[Button] = []

for index, button_text in enumerate(buttons_text_list):
    button = Button(actions_panel, text=button_text, font=('Dosis', 14, 'bold'),
                    bg='azure4', bd=1, width=9
                    )
    button.grid(row=0, column=index)
    buttons_list.append(button)


def get_cost_values() -> Tuple[float, float, float, float, float, float]:
    meals_total = get_total_by_lists(meals_entry_value_list, meals_prices)
    drinks_total = get_total_by_lists(drinks_entry_value_list, drinks_prices)
    desserts_total = get_total_by_lists(desserts_entry_value_list, desserts_prices)

    subtotal = round(meals_total + drinks_total + desserts_total, 2)
    tax = round(subtotal * 0.19, 2)
    total = round(subtotal + tax, 2)

    return total, subtotal, tax, meals_total, drinks_total, desserts_total


def calculate_total():
    total, subtotal, tax, meals_total, drinks_total, desserts_total = get_cost_values()
    meals_cost_value.set(str(meals_total))
    drinks_cost_value.set(str(drinks_total))
    desserts_cost_value.set(str(desserts_total))
    subtotal_value.set(str(subtotal))
    tax_value.set(str(tax))
    total_value.set(str(total))


def generate_receipt():
    receipt_text.delete(1.0, END)
    receipt_number = f"N# - {random.randint(1000, 9999)}"
    date_now = datetime.datetime.now()
    formatted_date = f'{date_now.day}/{date_now.month}/{date_now.year}'
    receipt_text.insert(END, f'Data:\t{receipt_number}\t\t{formatted_date}\n')
    receipt_text.insert(END, f'*' * 47 + '\n')
    receipt_text.insert(END, 'Items\t\tQuantity\tPrice\n')
    receipt_text.insert(END, f'-'*54 + '\n')
    receipt_text.insert(END, get_receipt_data_by_list(meals_list, meals_entry_value_list, meals_prices))
    receipt_text.insert(END, get_receipt_data_by_list(drinks_list, drinks_entry_value_list, drinks_prices))
    receipt_text.insert(END, get_receipt_data_by_list(desserts_list, desserts_entry_value_list, desserts_prices))
    costs = get_cost_values()
    receipt_text.insert(END, f'-' * 54 + '\n')
    receipt_text.insert(END, f"Subtotal: ${subtotal_value.get()}\n")
    receipt_text.insert(END, f"Tax: ${tax_value.get()}\n")
    receipt_text.insert(END, f"Total: ${total_value.get()}\n")


def save_receipt():
    receipt_info = receipt_text.get(1.0, END)
    file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    file.write(receipt_info)
    file.close()
    messagebox.showinfo('Info', 'Receipt saved')


def reset():
    receipt_text.delete(0.1, END)
    reset_check_list(meals_check_list)
    reset_check_list(drinks_check_list)
    reset_check_list(desserts_check_list)
    reset_entry_list(meals_entry_list)
    reset_entry_list(drinks_entry_list)
    reset_entry_list(desserts_entry_list)
    reset_entry_value_list(meals_entry_value_list)
    reset_entry_value_list(drinks_entry_value_list)
    reset_entry_value_list(desserts_entry_value_list)
    reset_entry_value_list([meals_cost_value, drinks_cost_value, desserts_cost_value,
                            subtotal_value, tax_value, total_value
                            ])


buttons_list[0].config(command=calculate_total)
buttons_list[1].config(command=generate_receipt)
buttons_list[2].config(command=save_receipt)
buttons_list[3].config(command=reset)

# Receipt area
receipt_text = Text(receipt_panel, font=('Dosis', 12, 'bold'),
                    bd=1, width=42, height=10
                    )
receipt_text.grid(row=0, column=0)

# Calculator
calculator_entry = Entry(calculator_panel, font=('Dosis', 16, 'bold'), width=32, bd=1)
calculator_entry.grid(row=0, column=0, columnspan=4)
calculator = Calculator(entry=calculator_entry, panel=calculator_panel)
calculator.init()

# App loop
application.mainloop()
