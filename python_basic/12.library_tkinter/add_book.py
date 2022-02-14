from tkinter import *

def update():
    """Update information"""
    select.delete(0, END)
    for n, b, a in data:
        select.insert(END, n)

def add():
    """Add information"""
    global data
    data.append([name.get(), number.get(), address.get(1.0, "end-1c")])
    update()

def view():
    """View information"""
    name.set(data[int(select.curselection()[0])][0])
    number.set(data[int(select.curselection()[0])][1])
    address.delete(1.0,"end")
    address.insert(1.0, data[int(select.curselection()[0])][2])

def delete():
    """Delete information"""
    del data[int(select.curselection()[0])]
    update()

def reset():
    name.set('')
    number.set('')
    address.delete(1.0, "end")

if __name__ == "__main__":
    # Create object
    window = Tk()
    window.geometry("400x500")

    name = StringVar()
    number = StringVar()

    # Information List
    data = []
    
    # Name
    frame_name = Frame()
    frame_name.pack(pady=10)
    Label(frame_name, text="Name", font='arial 12 bold').pack(side=LEFT)
    Entry(frame_name, textvariable=name, width=50).pack()

    # Phone
    frame_phone = Frame()
    frame_phone.pack(pady=10)
    Label(frame_phone, text="Phone No.", font='arial 12 bold').pack(side=LEFT)
    Entry(frame_phone, textvariable=number, width=50).pack()

    # Address
    frame_address =Frame()
    frame_address.pack(pady=10)
    Label(frame_address, text="Address", font="arial 12 bold").pack(side=LEFT)
    address = Text(frame_address, width=50, height=10)
    address.pack()
    
    Button(window, text="Add"   , font="arial 12 bold", command=add   ).place(x=100, y=270)
    Button(window, text="View"  , font="arial 12 bold", command=view  ).place(x=100, y=310)
    Button(window, text="Delete", font="arial 12 bold", command=delete).place(x=100, y=350)
    Button(window, text="Reset"   , font="arial 12 bold", command=reset ).place(x=100, y=390)
    
    scroll_bar = Scrollbar(window, orient=VERTICAL)
    select = Listbox(window, yscrollcommand=scroll_bar.set, height=10, width = 30)
    scroll_bar.config(command=select.yview)
    scroll_bar.pack(side=RIGHT, fill=Y)
    select.place(x=180, y=280)

    # Execute
    window.mainloop()