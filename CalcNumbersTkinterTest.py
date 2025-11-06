import tkinter as tk
from tkinter import messagebox

# Function to calculate and display the result
def calculate():
    try:
        # Get the values from the entry fields
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        # Calculate the sum
        result = num1 + num2
        
        # Display the result in the result label
        result_label.config(text=f"Result: {num1} + {num2} = {result}")
        
    except ValueError:
        # Show error if inputs aren't valid numbers
        messagebox.showerror("Invalid Input", "Please enter valid numbers!")

# Function to clear all fields
def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result: ")

# Create the main window
window = tk.Tk()
window.title("Addition Calculator")
window.geometry("400x300")
window.resizable(False, False)

# Create a title label
title_label = tk.Label(window, text="Simple Addition Calculator", 
                       font=("Arial", 16, "bold"))
title_label.pack(pady=20)

# Create frame for input fields
input_frame = tk.Frame(window)
input_frame.pack(pady=10)

# First number label and entry
label1 = tk.Label(input_frame, text="First Number:", font=("Arial", 12))
label1.grid(row=0, column=0, padx=10, pady=10, sticky="e")

entry1 = tk.Entry(input_frame, font=("Arial", 12), width=15)
entry1.grid(row=0, column=1, padx=10, pady=10)

# Second number label and entry
label2 = tk.Label(input_frame, text="Second Number:", font=("Arial", 12))
label2.grid(row=1, column=0, padx=10, pady=10, sticky="e")

entry2 = tk.Entry(input_frame, font=("Arial", 12), width=15)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Create frame for buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# Calculate button
calculate_button = tk.Button(button_frame, text="Calculate", 
                             font=("Arial", 12, "bold"), 
                             bg="#4CAF50", fg="white",
                             command=calculate, width=10)
calculate_button.grid(row=0, column=0, padx=5)

# Clear button
clear_button = tk.Button(button_frame, text="Clear", 
                         font=("Arial", 12, "bold"),
                         bg="#f44336", fg="white",
                         command=clear, width=10)
clear_button.grid(row=0, column=1, padx=5)

# Result label
result_label = tk.Label(window, text="Result: ", 
                       font=("Arial", 14), fg="#2196F3")
result_label.pack(pady=20)

# Start the GUI event loop
window.mainloop()