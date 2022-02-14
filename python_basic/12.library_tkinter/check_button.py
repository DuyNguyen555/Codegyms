from tkinter import *

def button_1_click():
    print("It's number: 1")
    
def button_2_click():
    print("It's number: 2")

if __name__ == '__main__':
    check = Tk()
    check.geometry("100x100")

    button_1 = Button(check, text="1", width=10, command=button_1_click).grid(padx= 10, pady=10)
    button_2 = Button(check, text="2", width=10, command=button_2_click).grid(padx=10, pady=10)
    
    # Execute
    check.mainloop()