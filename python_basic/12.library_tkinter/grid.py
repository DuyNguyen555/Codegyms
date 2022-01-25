from tkinter import *
# create window
window = Tk()
window.geometry("400x400")
# title
window.title("Grid")
for i in range(5):
    for j in range(3):
        frame = Frame(master = window, relief = RAISED, borderwidth = 3, bg = "skyblue")
        frame.grid(row=i, column=j)
        label = Label(master=frame, text=f"Row {i}\nColumn {j}", fg = "green")
        label.pack()

# Display window
window.mainloop()