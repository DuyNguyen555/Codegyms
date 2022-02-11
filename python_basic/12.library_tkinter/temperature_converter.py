from tkinter import *

def fahrenheit_to_celsius():
    fahrenheit = entry_f.get()
    celsius = 5/9 * (float(fahrenheit) - 32)
    label_result_c["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

def celsius_to_fahrenheit ():
    celsius = entry_c.get()
    fahrenheit = 9/5 * float(celsius) + 32
    label_result_f["text"] = f"{round(fahrenheit, 2)} \N{DEGREE FAHRENHEIT}"

if __name__ == '__main__':
    # Create screen
    screen = Tk()
    screen.title("TEMPERATURE CONVERTER")
    screen.resizable(width=False, height=False)

    """F to C(START)"""
    # create frame of F
    frame_f = Frame(screen)
    
    # Create entry F
    entry_f = Entry(frame_f, width = 10)
    
    # Create an F-mark
    label_f = Label(frame_f, text = "\N{DEGREE FAHRENHEIT}")
    
    # position entry F and label F in grid
    entry_f.grid(row=0, column=0, sticky="E")
    label_f.grid(row=0, column=1, sticky="W")
    
    # Button to converter
    button_f = Button(screen, text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheit_to_celsius)
    
    # Create a C-mark
    label_result_c = Label(screen, text="\N{DEGREE CELSIUS}")
    
    # Display result
    frame_f.grid(row=0, column=0, padx=10)
    button_f.grid(row=0, column=1, pady=10)
    label_result_c.grid(row=0, column=2, padx=10)
    """F to C(END)"""

    """C to F(START)"""
    # Create frame of C
    frame_c = Frame(screen)
    
    # Create entry C
    entry_c = Entry(frame_c, width = 10)

    # Create a C-mark
    label_c = Label(frame_c, text="\N{DEGREE CELSIUS}")
    
    # Position entry C and label C in grid
    entry_c.grid(row=0, column=0, sticky="E")
    label_c.grid(row=0, column=1, sticky="W")
    
    # Button to converter
    button_c = Button(
        screen,
        text="\N{RIGHTWARDS BLACK ARROW}", command=celsius_to_fahrenheit
        )
    
    # Create an F-mark
    label_result_f = Label(screen, text="\N{DEGREE FAHRENHEIT}")
    
    # Display result
    frame_c.grid(row=1, column=0, padx=10)
    button_c.grid(row=1, column=1, padx=10)
    label_result_f.grid(row=1, column=2, padx=10)
    
    # mainloop
    screen.mainloop()