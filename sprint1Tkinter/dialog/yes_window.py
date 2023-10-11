from tkinter import Tk
import tkinter as tk
from tkinter import ttk, Button

def show_yes_window(): 
    ## Se instancia la pestaña.
    yes_root = tk.Tk()
    ## Título de la pestaña "SI".
    yes_root.title("Sí")

    ## Label destinado a mostrar el texto de la No Window.
    label = ttk.Label(yes_root, text = "Ventana de Sí")
    label.pack()

    ## Lanzamos el bucle.
    yes_root.mainloop()
    

