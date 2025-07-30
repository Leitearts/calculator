import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operator_var.get()

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                messagebox.showerror("Math Error", "Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Operator Error", "Select a valid operator.")
            return

        result_label.config(text=f"Result: {num1} {operator} {num2} = {round(result, 2)}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create window
window = tk.Tk()
window.title("Python Calculator")
window.geometry("300x300")

# Input fields
tk.Label(window, text="First Number").pack()
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="Second Number").pack()
entry2 = tk.Entry(window)
entry2.pack()

# Operator selection
tk.Label(window, text="Operation").pack()
operator_var = tk.StringVar(window)
operator_var.set('+')  # Default operator
tk.OptionMenu(window, operator_var, '+', '-', '*', '/').pack()

# Calculate button
tk.Button(window, text="Calculate", command=calculate).pack(pady=10)

# Result
result_label = tk.Label(window, text="Result: ")
result_label.pack()