from tkinter import Tk
import tkinter as tk
from tkinter import ttk, Button

def show_no_window():
    ## Se instancia la pestaña.
    no_root = tk.Tk()
    ## Título de la pestaña "NO".
    no_root.title("No")

    ## Label destinado a mostrar el texto de la No Window.
    label = ttk.Label(no_root, text = "Ventana de No")
    label.pack()

    ## Lanzamos el bucle.
    no_root.mainloop()

