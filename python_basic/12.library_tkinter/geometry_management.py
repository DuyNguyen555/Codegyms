from tkinter import *
# create window
window_login = Tk()
# create title
window_login.title("Login")
window_login.geometry("300x150")
# Option
username = Label(window_login, text = "Username:").place(x = 10, y = 20)
email = Label(window_login, text = "Email:").place(x = 10, y = 50)
password = Label(window_login, text = "Password:").place(x = 10, y = 80)
# Enter
label_username = Entry(window_login).place(x = 100, y = 20, width = 150)
label_username = Entry(window_login).place(x = 100, y = 50, width = 150)
label_password = Entry(window_login).place(x = 100, y = 80, width = 150)
# window
window_login.mainloop()