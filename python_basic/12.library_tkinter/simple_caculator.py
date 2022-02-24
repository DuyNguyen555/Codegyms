from tkinter import *

def press(text):
    global equation
    equation = equation + str(text)
    var_input.set(equation)

def clear():
    global equation
    equation = ""
    var_input.set(equation)

def equal():
    global equation
    try:
        result = str(eval(equation))
        equation = result
        var_input.set(equation)
    except:
        equation = "Error"
        var_input.set(equation)

if __name__ == '__main__':
    # Create display
    display = Tk()
    display.title("CALCULATOR")
    
    # Calculate
    # Entry number
    var_input = StringVar()
    equation = ""
    expression = Entry(display, textvariable = var_input, width=25, 
                       font = 'arial 20 bold', justify = "right", 
                       insertwidth=2, bd=10).grid(columnspan = 4, pady =10)

    # Create button
    # number
    button_9 = Button(display, text="9", font = 'arial 15 bold', bd=5, width=5, command = lambda: press(9) ).grid(row=1, column=2)
    button_8 = Button(display, text="8", font = 'arial 15 bold', bd=5, width=5, command = lambda: press(8) ).grid(row=1, column=1)
    button_7 = Button(display, text="7", font = 'arial 15 bold', bd=5, width=5, command = lambda: press(7) ).grid(row=1, column=0)
    button_6 = Button(display, text="6", font = 'arial 15 bold', bd=5, width=5, command = lambda: press(6) ).grid(row=2, column=2)
    button_5 = Button(display, text="5", font = 'arial 15 bold', bd=5, width=5, command = lambda: press(5) ).grid(row=2, column=1)
    button_4 = Button(display, text="4", font = 'arial 15 bold', bd=5, width=5, command = lambda: press(4) ).grid(row=2, column=0)
    button_3 = Button(display, text="3", font = 'arial 15 bold', bd=5, width=5, command = lambda: press(3) ).grid(row=3, column=2)
    button_2 = Button(display, text="2", font = 'arial 15 bold', bd=5, width=5, command = lambda: press(2) ).grid(row=3, column=1)
    button_1 = Button(display, text="1", font = 'arial 15 bold', bd=5, width=5, command = lambda: press(1) ).grid(row=3, column=0)
    button_0 = Button(display, text="0", font = 'arial 15 bold', bd=5, width=5, command = lambda: press(0) ).grid(row=4, column=1)

    # Calculation
    button_divide   = Button(display, text="/", font = 'arial 15 bold', bd=5, width=5, command = lambda: press("/")).grid(row=1, column=3)
    button_multiply = Button(display, text="*", font = 'arial 15 bold', bd=5, width=5, command = lambda: press("*")).grid(row=2, column=3)
    button_minus    = Button(display, text="-", font = 'arial 15 bold', bd=5, width=5, command = lambda: press("-")).grid(row=3, column=3)
    button_plus     = Button(display, text="+", font = 'arial 15 bold', bd=5, width=5, command = lambda: press("+")).grid(row=4, column=3)
    button_dot      = Button(display, text=".", font = 'arial 15 bold', bd=5, width=5, command = lambda: press(".")).grid(row=4, column=2)

    # Clear
    button_clear = Button(display, text="C", font = 'arial 15 bold', bd=5, width=5, command = clear).grid(row=4, column=0)
    
    # Equal
    button_equal = Button(display, text="=", font = 'arial 15 bold', bd=5, width=25, command = equal).grid(row=5, columnspan=4, pady = 5)
    
    display.mainloop()
