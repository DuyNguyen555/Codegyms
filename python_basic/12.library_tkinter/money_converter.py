from tkinter import *

# 1 usd = 23000 vnd

def dollar_to_vnd():
    dollar = entry_dollar.get()
    vnd = float(dollar)*23000
    label_result_dollar["text"] = f"{round(vnd, 0)} VND"

def vnd_to_dollar():
    vnd = entry_vnd.get()
    dollar = float(vnd)/23000
    label_result_vnd["text"] = f"{round(dollar, 2)} USD"

if __name__ == '__main__':
    # Create screen
    screen = Tk()
    screen.title("Money_converter")
    screen.resizable(width = FALSE, height = FALSE)

    # Create frame usd to vnd
    frame_dollar = Frame(screen)
    entry_dollar = Entry(frame_dollar, width = 20)
    label_dollar = Label(frame_dollar, text = "USD")
    # position entry usd in frame
    entry_dollar.grid(row=0, column=0, sticky="E")
    label_dollar.grid(row=0, column=1, sticky="W")
    
    # Result of convert
    label_result_dollar = Label(screen, text="VND")

    # Create button convert
    button_dollar = Button(screen, text="\N{RIGHTWARDS BLACK ARROW}", command=dollar_to_vnd)
    
    # Display convert
    frame_dollar.grid(row=0, column=0, padx=20) 
    button_dollar.grid(row=0, column=1, padx=10)
    label_result_dollar.grid(row=0, column=2, padx=20)
    
    # Create frame vnd to usd
    frame_vnd = Frame(screen)
    entry_vnd = Entry(frame_vnd, width = 20)
    label_vnd = Label(frame_vnd, text="VND")
    # Position entry vnd in frame
    entry_vnd.grid(row=0, column=0, sticky="E")
    label_vnd.grid(row=0, column=1, sticky="W")

    # Result of convert
    label_result_vnd = Label(screen, text="USD")

    # Create button convert
    button_vnd = Button(screen, text="\N{RIGHTWARDS BLACK ARROW}", command=vnd_to_dollar)
    
    # Display convert
    frame_vnd.grid(row=1, column=0, padx=20)
    button_vnd.grid(row=1, column=1, padx=10)
    label_result_vnd.grid(row=1, column=2, padx=20)
    
    # mainloop
    screen.mainloop()