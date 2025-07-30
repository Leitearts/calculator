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

# Create the window
window = tk.Tk()
window.title("Python GUI Calculator")
window.geometry("300x250")

# First number
tk.Label(window, text="Enter First Number").pack(pady=5)
entry1 = tk.Entry(window)
entry1.pack()

# Second number
tk.Label(window, text="Enter Second Number").pack(pady=5)
entry2 = tk.Entry(window)
entry2.pack()

# Operator dropdown
tk.Label(window, text="Choose Operation").pack(pady=5)
operator_var = tk.StringVar(window)
operator_var.set('+')
tk.OptionMenu(window, operator_var, '+', '-', '*', '/').pack()

# Calculate button
tk.Button(window, text="Calculate", command=calculate).pack(pady=10)

# Result display
result_label = tk.Label(window, text="Result: ")
result_label.pack()

# Start the GUI loop
window.mainloop()
