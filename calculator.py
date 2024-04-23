import tkinter as tk
import sympy as sp

def evaluate_expression():
    expression = entry_expression.get()
    try:
        result = sp.sympify(expression)
        result_label.config(text="Result: {}".format(result))
    except (sp.SympifyError, ValueError):
        result_label.config(text="Invalid Expression")

def clear():
    entry_expression.delete(0, tk.END)
    result_label.config(text="Result:")

# Create the GUI
root = tk.Tk()
root.title("Algebraic Calculator")

entry_expression = tk.Entry(root, width=50)
entry_expression.pack()

evaluate_button = tk.Button(root, text="Evaluate", command=evaluate_expression)
evaluate_button.pack()

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.pack()

result_label = tk.Label(root, text="Result:")
result_label.pack()

root.mainloop()
