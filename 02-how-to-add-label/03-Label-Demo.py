from tkinter import *

root_window = Tk()
root_window.title("LST: Label-Demo")

L = Label(root_window)
L.configure(text="Label Demo", fg="black")
L.grid(row=0, column=0)

root_window.mainloop()