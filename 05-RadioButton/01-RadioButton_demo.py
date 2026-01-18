from tkinter import *
from tkinter import ttk

def OnSubmit():
    Selected_button = selected_button_var.get()
    print("Selected Button is {}:".format(Selected_button))

def main():
    global selected_button_var
    
    root_window = Tk()
    root_window.title("RadioButton Demo")
    
    selected_button_var = StringVar()
    
    radioButton_1 = ttk.RadioButton(
        root_window,
        variable=selected_button_var,
        text = "RadioButton-1",
        value= "RadioButton-1"
    )
    
    radioButton_1.grid(row=0, column=0, sticky=(W, E))
    
    radioButton_2 = ttk.Radiobutton(
        root_window,
        variable=selected_button_var,
        text="RadioButton-2",
        value="RadioButton-2"
    )
    
    radioButton_2.grid(row=1, column=0, sticky=(E, W))
    
    submit_button = ttk.Button(root_window)
    submit_button.configure(text="Submit", command=OnSubmit)
    submit_button.grid(row=2, column=0, sticky=(W, E))
    
    root_window.mainloop()
    
main()