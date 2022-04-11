from tkinter import *
import os

def Shutdown():
    return os.system("shutdown /s /t 1")

def Restart():
    return os.system("shutdown /r /t 1")

def Login():
    return os.system("shutdown -l")

if __name__ == '__main__':
    screen = Tk()
    screen.geometry("200x200")
    screen.configure(background= "light grey")

    # Create Button
    shutdown = Button(screen, text="Shutdown", width=10, height = 2, command=Shutdown).grid(row=0, padx=60)
    restart  = Button(screen, text="Restart" , width=10, height = 2, command=Restart ).grid(row=1, padx=60)
    login    = Button(screen, text="Login"   , width=10, height = 2, command=Login   ).grid(row=2, padx=60)
    
    screen.mainloop()