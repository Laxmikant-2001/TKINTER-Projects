from tkinter import *
from tkinter import ttk

def checkValue():
    value = check_uncheck_var.get()
    print(value)

def main():
    global check_uncheck_var

    root_window = Tk()
    root_window.title("CheckBox Demo")

    check_uncheck_var = StringVar()

    checkbox = ttk.Checkbutton(root_window)
    checkbox.configure(
        text="CheckBox",
        variable=check_uncheck_var,
        onvalue="Check",
        offvalue="Uncheck",
        command=checkValue
    )

    checkbox.grid(row=0, column=0, sticky=(E, W))

    root_window.mainloop()

main()
    
