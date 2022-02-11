from tkinter import *
# create window
window = Tk()
window.geometry("400x300")

def call(event):
    print("click at", event.x, event.y)

if __name__ == '__main__':
    frame = Frame(window, width = 400, height = 300)
    frame.bind("<Button-1>", call)
    frame.pack()
    
    window.mainloop()