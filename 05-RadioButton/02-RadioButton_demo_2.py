from tkinter import *
from tkinter import ttk

def OnSubmit():
    Selected_button = selected_button_var.get()
    print("Submited button is {}:".format(Selected_button))

def main():
    
    global selected_button_var 
    
    root_window = Tk()
    root_window.title("LST: RadioButton-Demo")
    
    selected_button_var = StringVar()
    
    radioButton_1 = ttk.Radiobutton(
        root_window,
        variable=selected_button_var,
        text = "RadioButton-1",
        value = "RadioButton-1"
    )
    
    radioButton_1.grid(row=0, column=0, sticky=(W, E))
    
    radioButton_2 = ttk.Radiobutton(
        root_window,
        variable = selected_button_var,
        text ="RadioButton_2",
        value = "RadioButton_2"
    )
    
    radioButton_2.grid(row=0, column=1, sticky=(E, W))
    
    submit_Button = ttk.Button(root_window)
    submit_Button.configure(text="Submit", command=OnSubmit)
    submit_Button.grid(row=0, column=3)
    
    root_window.mainloop()
    
    
    
main()