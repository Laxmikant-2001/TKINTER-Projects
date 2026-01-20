from tkinter import * 
from tkinter import ttk 

def SpinBoxValue():
    value = spinebox_var.get()
    if not value:
        value = None
    print(f"SpineBox value : {value}")
    
def main():
    
    global spinebox_var
    
    root_window = Tk()
    root_window.title("LST: SpineBox Demo")
    
    spinebox_var = StringVar()
    
    label = ttk.Label(root_window)
    label.configure(text="SpineBox", foreground="black")
    label.grid(row=0, column=0)
    
    spinebox = ttk.Spinbox(root_window)
    spinebox.configure(textvariable=spinebox_var, from_=0, to=10)
    spinebox.grid(row=0, column=1, sticky=(E, W))
    
    button = ttk.Button(root_window)
    button.configure(text="Get_Value", command=SpinBoxValue)
    button.grid(row=1, column=0, sticky=(E, W))
    
    root_window.mainloop()
    
main()