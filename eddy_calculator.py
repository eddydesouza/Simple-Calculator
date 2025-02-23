# Import the tkinter module
import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")

# Allow window resizing
root.geometry("300x400") # Initial window size

# Configure grid to be resizable
root.rowconfigure(0, weight=1)  # Entry row expands
for i in range(4):  # Make button rows expandable
    root.rowconfigure(i+1, weight=1)
    root.columnconfigure(i, weight=1)  # All columns expand

# Create the StringVar to store input results
input_var = tk.StringVar()
input_var.set("0") # Default display text
entry = tk.Entry(root, textvariable=input_var, font=('Arial', 14), bd=10, insertwidth=4, width=14, justify='right')
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")  # Expand in all directions

# Reset display to "0"
def clear_display():
    input_var.set("0")

# Define functions of the calculator
def button_click(value):
    current_input = input_var.get()
    if current_input == "0":
        input_var.set(str(value))  # Replace initial "0"
    else:
        input_var.set(current_input + str(value))

def calculate_result():
    try:
        result = eval(input_var.get())
        input_var.set(result)
    except Exception as e:
        input_var.set("Error")

# Create buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/',1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),  
]

# Running the main loop
for (text, row, col) in buttons:
    if text == 'C':
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=clear_display)
    elif text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=calculate_result)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=lambda t=text: button_click(t))

    button.grid(row=row, column=col, sticky="nsew")  # Allow button expansion
    root.rowconfigure(row, weight=1)  # Ensure rows expand
    root.columnconfigure(col, weight=1)  # Ensure columns expand

    button.grid(row=row, column=col)
root.mainloop()







