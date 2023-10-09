from tkinter import Tk
import tkinter as tk
from tkinter import ttk, Button

def show_yes_window(): 
    yes_root = tk.Tk()
    yes_root.title("Sí")

    label = ttk.Label(yes_root, text = "Ventana de Sí")
    label.pack()

    yes_root.mainloop()
    

