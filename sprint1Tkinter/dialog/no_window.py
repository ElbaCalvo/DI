from tkinter import Tk
import tkinter as tk
from tkinter import ttk, Button

def show_no_window(): 
    no_root = tk.Tk()
    no_root.title("No")
    
    label = ttk.Label(no_root, text = "Ventana de No")
    label.pack()

    no_root.mainloop()

