from tkinter import *
from tkinter.ttk import *

# Tạo cửa sổ chính cho giao diện
root = Tk()
# Tạo tiêu đề
root.title("First_program")
# Tạo văn bản
label = Label(root, text = " Hello Tkinter !").pack()
# Hiển thị màn hình
root.mainloop()