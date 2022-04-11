from tkinter import *
def fill_color1():
    window = Tk()
    window.geometry("400x400")
    window.title("Fill color")
    frame1 = Frame(window, height = 100, bg = "blue").pack(fill = X)
    frame2 = Frame(window, height = 150, bg = "purple").pack(fill = X)
    frame3 = Frame(window, height = 200, bg = "pink").pack(fill = X)
    window.mainloop()

def fill_color2():
    window = Tk()
    window.geometry("400x400")
    window.title("Fill color 2")
    frame1 = Frame(window, height = 100, bg = "red").pack(fill = BOTH, side = LEFT, expand = TRUE)
    frame2 = Frame(window, height = 100, bg = "yellow").pack(fill = BOTH, side = LEFT, expand = TRUE)
    frame3 = Frame(window, height = 100, bg = "orange").pack(fill = BOTH, side = LEFT, expand = TRUE)
    window.mainloop()

if __name__ == "__main__":
    fill_color2()