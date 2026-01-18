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
        variable = selected_button_var,
        text = "Radiobutton_1",
        value = "Radiobutton_2"
    )
    
    radioButton_1.grid(row=0, column=0, sticky=(W, E))
    
    radioButton_2 = ttk.Radiobutton(
        root_window,
        variable = selected_button_var,
        text = "Radiobutton_2",
        value = "Radiobutton_2"
    )
    
    radioButton_2.grid(row=1, column=0, sticky = (E, W))
    
    Submit_button = ttk.Button(root_window)
    Submit_button.configure(text="Submit", command= OnSubmit)
    Submit_button.grid(row=2, column=0)
    
    root_window.mainloop()
    

main()