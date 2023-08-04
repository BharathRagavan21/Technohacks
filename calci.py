import tkinter as tk

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = dropdown.get()

    if operation == 'Addition':
        result = num1 + num2
    elif operation == 'Subtraction':
        result = num1 - num2
    elif operation == 'Multiplication':
        result = num1 * num2
    elif operation == 'Division':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero is not allowed."
    else:
        result = "Invalid operation"

    label_result.config(text="Result: " + str(result))

window = tk.Tk()
window.title("Calculator")

label_num1 = tk.Label(window, text="Number 1:")
label_num1.pack()

entry_num1 = tk.Entry(window)
entry_num1.pack()

label_num2 = tk.Label(window, text="Number 2:")
label_num2.pack()

entry_num2 = tk.Entry(window)
entry_num2.pack()

label_operation = tk.Label(window, text="Operation:")
label_operation.pack()

dropdown = tk.StringVar(window)
dropdown.set('Addition')
dropdown_menu = tk.OptionMenu(window, dropdown, 'Addition', 'Subtraction', 'Multiplication', 'Division')
dropdown_menu.pack()

button_calculate = tk.Button(window, text="Calculate", command=calculate)
button_calculate.pack()

label_result = tk.Label(window, text="Result:")
label_result.pack()

window.mainloop()