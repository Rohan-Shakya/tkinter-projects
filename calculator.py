# Importing dependencies
import tkinter
from tkinter import *
from tkinter import messagebox

# Global Variables
initial_value = ''
value = 0
initial_operator = ''


# GUI for calculator
calc = tkinter.Tk()
calc.geometry("350x460+300+300")
calc.resizable(0, 0)
calc.title("Calculator")
calc.config(background = 'light grey')

# functionality
def clickedOperandBtn(operand):
    global initial_value
    initial_value = initial_value + operand
    data.set(initial_value)

def clickedOperatorBtn(operator):
    global value
    global initial_operator
    global initial_value
    value = int(initial_value)
    initial_operator = operator
    initial_value = initial_value + operator
    data.set(initial_value)

def clear():
    global value
    global initial_operator
    global initial_value
    initial_value = ''
    value = 0
    initial_operator = ''
    data.set(initial_value)

def result():
    global value
    global initial_operator
    global initial_value
    initial_value2 = initial_value
    if initial_operator == '+':
        x = int(initial_value2.split('+')[1])
        c = value + x
        data.set(c)
        initial_value = str(c)
    elif initial_operator == '-':
        x = int(initial_value2.split('-')[1])
        c = value - x
        data.set(c)
        initial_value = str(c)
    elif initial_operator == '*':
        x = int(initial_value2.split('*')[1])
        c = value * x
        data.set(c)
        initial_value = str(c)
    elif initial_operator == '/':
        x = int(initial_value2.split('/')[1])
        if x == 0:
            messagebox.showerror("Error", "Division by 0 not allowed")
            value = ''
            initial_value = ''
            data.set(initial_value)
        else:
            c = int(value / x)
            data.set(c)
            initial_value = str(c)

data = StringVar()

# Display screen
display = Label(
    calc, 
    text = 'Label',
    anchor = SE,
    font = ("Courier New", 20),
    textvariable = data,
    background = 'dark grey',
    fg = '#000000'
)
display.pack(expand = True, fill = 'both')

# Frame Section
row1 = Frame(calc)
row1.pack(expand = True, fill = "both")

row2 = Frame(calc)
row2.pack(expand = True, fill = "both")

row3 = Frame(calc)
row3.pack(expand = True, fill = "both")

row4 = Frame(calc)
row4.pack(expand = True, fill = "both")


# Buttons Section
btn1 = Button(
    row1,
    text = "1",
    font = ("Courier New", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: clickedOperandBtn("1"),
)
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    row1,
    text = "2",
    font = ("Courier New", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: clickedOperandBtn("2"),
)

btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3 = Button(
    row1,
    text = "3",
    font = ("Courier New", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: clickedOperandBtn("3"),
)
btn3.pack(side = LEFT, expand = True, fill = "both",)

btnPlus = Button(
    row1,
    text = "+",
    font = ("Courier New", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: clickedOperatorBtn("+")
)
btnPlus.pack(side = LEFT, expand = True, fill = "both",)

# Buttons for frame 2

btn4 = Button(
    row2,
    text = "4",
    font = ("Courier New", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: clickedOperandBtn("4"),
)
btn4.pack(side = LEFT, expand = True, fill = "both",)

btn5 = Button(
    row2,
    text = "5",
    font = ("Courier New", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: clickedOperandBtn("5"),

)
btn5.pack(side = LEFT, expand = True, fill = "both",)

btn6 = Button(
    row2,
    text = "6",
    font = ("Courier New", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: clickedOperandBtn("6"),

)
btn6.pack(side = LEFT, expand = True, fill = "both",)

btnMinus = Button(
    row2,
    text = "-",
    font = ("Courier New", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: clickedOperatorBtn("-")
    
)
btnMinus.pack(side = LEFT, expand = True, fill = "both",)

# Buttons for frame 3

btn7 = Button(
    row3,
    text = "7",
    font = ("Courier New", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: clickedOperandBtn("7"),
)
btn7.pack(side = LEFT, expand = True, fill = "both",)

btn8 = Button(
    row3,
    text = "8",
    font = ("Courier New", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: clickedOperandBtn("8"),
)
btn8.pack(side = LEFT, expand = True, fill = "both",)

btn9 = Button(
    row3,
    text = "9",
    font = ("Courier New", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: clickedOperandBtn("9"),
)
btn9.pack(side = LEFT, expand = True, fill = "both",)

btnMultiply = Button(
    row3,
    text = "*",
    font = ("Courier New", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: clickedOperatorBtn("*")
)
btnMultiply.pack(side = LEFT, expand = True, fill = "both",)

# Buttons for frame 4


btnClear = Button(
    row4,
    text = "C",
    font = ("Courier New", 22),
    fg="white",
    background="crimson",
    relief = GROOVE,
    border = 0,
    command = clear
)
btnClear.pack(side = LEFT, expand = True, fill = "both",)

btnZero = Button(
    row4,
    text = "0",
    font = ("Courier New", 22),
    relief = GROOVE,
    border = 0,
   command = lambda: clickedOperandBtn("0"),
)
btnZero.pack(side = LEFT, expand = True, fill = "both",)

btnEqual = Button(
    row4,
    text = "=",
    font = ("Courier New", 22),
    relief = GROOVE,
    border = 0,
    command = result
)
btnEqual.pack(side = LEFT, expand = True, fill = "both",)

btnDivide = Button(
    row4,
    text = "/",
    font = ("Courier New", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: clickedOperatorBtn("/")
)
btnDivide.pack(side = LEFT, expand = True, fill = "both",)


# For continuos looping
calc.mainloop()