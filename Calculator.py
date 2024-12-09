from tkinter import *

# Create the main application window
root = Tk()
root.title("Calculator")

# Set the size of the GUI
root.geometry("600x700")  # Larger dimensions

# Configure the grid to expand dynamically
for i in range(6):  # Rows
    root.grid_rowconfigure(i, weight=1)
for j in range(6):  # Columns
    root.grid_columnconfigure(j, weight=1)

# Adding the input field with larger font
display = Entry(root, font=("Arial", 28), justify='right', bd=10, relief=SUNKEN)
display.grid(row=0, columnspan=6, sticky=N+E+W+S, padx=10, pady=10)

# Function placeholders
def get_variables(num):
    display.insert(END, num)

def clear_all():
    display.delete(0, END)

def get_operation(op):
    display.insert(END, op)

def undo():
    current_text = display.get()
    display.delete(0, END)
    display.insert(0, current_text[:-1])

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, END)
        display.insert(END, result)
    except:
        display.delete(0, END)
        display.insert(END, "Error")

def fact():
    try:
        n = int(display.get())
        result = 1
        for i in range(1, n + 1):
            result *= i
        display.delete(0, END)
        display.insert(END, result)
    except:
        display.delete(0, END)
        display.insert(END, "Error")

# Adding buttons to the calculator with larger font
button_font = ("Arial", 20)  # Common font for all buttons

Button(root, text="1", command=lambda: get_variables(1), font=button_font).grid(row=1, column=0, sticky=N+S+E+W, padx=10, pady=10)
Button(root, text="2", command=lambda: get_variables(2), font=button_font).grid(row=1, column=1, sticky=N+S+E+W, padx=10, pady=10)
Button(root, text="3", command=lambda: get_variables(3), font=button_font).grid(row=1, column=2, sticky=N+S+E+W, padx=10, pady=10)

Button(root, text="4", command=lambda: get_variables(4), font=button_font).grid(row=2, column=0, sticky=N+S+E+W, padx=10, pady=10)
Button(root, text="5", command=lambda: get_variables(5), font=button_font).grid(row=2, column=1, sticky=N+S+E+W, padx=10, pady=10)
Button(root, text="6", command=lambda: get_variables(6), font=button_font).grid(row=2, column=2, sticky=N+S+E+W, padx=10, pady=10)

Button(root, text="7", command=lambda: get_variables(7), font=button_font).grid(row=3, column=0, sticky=N+S+E+W, padx=10, pady=10)
Button(root, text="8", command=lambda: get_variables(8), font=button_font).grid(row=3, column=1, sticky=N+S+E+W, padx=10, pady=10)
Button(root, text="9", command=lambda: get_variables(9), font=button_font).grid(row=3, column=2, sticky=N+S+E+W, padx=10, pady=10)

Button(root, text="AC", command=lambda: clear_all(), font=button_font, fg="red").grid(row=4, column=0, sticky=N+S+E+W, padx=10, pady=10)
Button(root, text="0", command=lambda: get_variables(0), font=button_font).grid(row=4, column=1, sticky=N+S+E+W, padx=10, pady=10)
Button(root, text=".", command=lambda: get_variables("."), font=button_font).grid(row=4, column=2, sticky=N+S+E+W, padx=10, pady=10)

Button(root, text="+", command=lambda: get_operation("+"), font=button_font).grid(row=1, column=3, sticky=N+S+E+W, padx=10, pady=10)
Button(root, text="-", command=lambda: get_operation("-"), font=button_font).grid(row=2, column=3, sticky=N+S+E+W, padx=10, pady=10)
Button(root, text="*", command=lambda: get_operation("*"), font=button_font).grid(row=3, column=3, sticky=N+S+E+W, padx=10, pady=10)
Button(root, text="/", command=lambda: get_operation("/"), font=button_font).grid(row=4, column=3, sticky=N+S+E+W, padx=10, pady=10)

Button(root, text="pi", command=lambda: get_operation("*3.14"), font=button_font).grid(row=1, column=4, sticky=N+S+E+W, padx=10, pady=10)
Button(root, text="%", command=lambda: get_operation("%"), font=button_font).grid(row=2, column=4, sticky=N+S+E+W, padx=10, pady=10)
Button(root, text="(", command=lambda: get_operation("("), font=button_font).grid(row=3, column=4, sticky=N+S+E+W, padx=10, pady=10)
Button(root, text="exp", command=lambda: get_operation("**"), font=button_font).grid(row=4, column=4, sticky=N+S+E+W, padx=10, pady=10)

Button(root, text="<-", command=lambda: undo(), font=button_font).grid(row=1, column=5, sticky=N+S+E+W, padx=10, pady=10)
Button(root, text="x!", command=lambda: fact(), font=button_font).grid(row=2, column=5, sticky=N+S+E+W, padx=10, pady=10)
Button(root, text=")", command=lambda: get_operation(")"), font=button_font).grid(row=3, column=5, sticky=N+S+E+W, padx=10, pady=10)
Button(root, text="^2", command=lambda: get_operation("**2"), font=button_font).grid(row=4, column=5, sticky=N+S+E+W, padx=10, pady=10)

Button(root, text="=", command=lambda: calculate(), font=("Arial", 24), bg="green", fg="white").grid(row=5, columnspan=6, sticky=N+S+E+W, padx=10, pady=10)

# Start the main application loop
root.mainloop()
