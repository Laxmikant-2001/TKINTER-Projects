from tkinter import * 

root_window = Tk()
root_window.title("LST: Input-Demo")

L = Label(root_window)
L.configure(text="Enter your name:")
L.grid(row=0, column=0)

E = Entry(root_window)
E.grid(row=0, column=1)

root_window.mainloop()