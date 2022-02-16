from tkinter import *

def convert():
    kg = entry_kg.get()
    # 1 kg = 1000 gram
    label_result_gram["text"] = f"{round(float(kg)*1000, 4)}"

    # 1 kg = 2.20462262 pound
    label_result_pounds["text"] = f"{round(float(kg)*2.20462262, 4)}"

    # 1 kg = 35.2739619 ounce
    label_result_ounce["text"] = f"{round(float(kg)*35.2739619, 4)}"

if __name__ == '__main__':
    display = Tk()

    # create frame kg
    frame_kg = Frame(display)
    label_kg = Label(frame_kg, text = "Enter the weight in Kg")
    entry_kg = Entry(frame_kg, width = 20)

    label_kg.grid(row=0, column=0)
    entry_kg.grid(row=0, column=1)

    # Create button convert
    button_convert = Button(display, text = "Convert", command = convert)
    
    # Create frame gram
    frame_gram = Frame(display)
    label_gram = Label(frame_gram, text = "Gram")
    label_result_gram = Label(frame_gram, text = "0")
    
    label_gram.grid(row=0, column=0, sticky="E")
    label_result_gram.grid(row=0, column=1, sticky="W")
    
    # Create frame pounds
    frame_pounds = Frame(display)
    label_pounds = Label(frame_pounds, text = "Pounds")
    label_result_pounds = Label(frame_pounds, text = "0")
    
    label_pounds.grid(row=0, column=0, sticky="E")
    label_result_pounds.grid(row=0, column=1, sticky="W")
    
    # Create frame ounce
    frame_ounce = Frame(display)
    label_ounce = Label(frame_ounce, text = "Ounce")
    label_result_ounce = Label(frame_ounce, text = "0")
    
    label_ounce.grid(row=0, column=0, sticky="E")
    label_result_ounce.grid(row=0, column=1, sticky="W")

    # display
    frame_kg.grid(row=0, column=0, padx=10)
    button_convert.grid(row=0, column=1)
    frame_gram.grid(row=1, column=0)
    frame_pounds.grid(row=2, column=0)
    frame_ounce.grid(row=3, column=0)
    
    display.mainloop()