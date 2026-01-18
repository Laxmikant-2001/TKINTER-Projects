from tkinter import *
from tkinter import ttk

def OnSubmit():
    selected_button = selected_button_var.get()
    print("Selected button is {} :".format(selected_button))


def main():
    
    global selected_button_var
    
    root_window = Tk()
    root_window.title("LST: Radiobutton-Demo")
    
    selected_button_var = StringVar()
    
    radioButton_1 = ttk.Radiobutton(
        root_window,
        variable=selected_button_var,
        text="Radiobutton-1",
        value="Radiobutton-2"
    )
    
    radioButton_1.grid(row=0, column=1, sticky=(W, E))
    
    radioButton_2 = ttk.Radiobutton(
        root_window,
        variable = selected_button_var,
        text = "Radiobutton-2",
        value = "Radiobutton-2"
    )
    
    radioButton_2.grid(row=0, column=2, sticky=(E, W))
    
    submit_button = ttk.Button(root_window)
    submit_button.configure(text="Submit", command=OnSubmit)
    submit_button.grid(row=0, column=3)
    
    root_window.mainloop()
    
main()