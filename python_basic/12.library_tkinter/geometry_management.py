from tkinter import *
# Create window 
login_window = Tk()
# create area window
login_window.geometry("300x400")
# create title
login_window.title("login")
# login
username = Label(login_window, text = "Username:").place(x = 30, y = 30)
email = Label(login_window, text = "Email:").place(x = 30, y = 60)
password = Label(login_window, text = "Password:").place(x = 30, y = 90)
entry1 = Entry(login_window).place(x = 100, y = 30, width = 150)
entry2 = Entry(login_window).place(x = 100, y = 60, width = 150)
entry3 = Entry(login_window).place(x = 100, y = 90, width = 150)
# Display
login_window.mailoop()