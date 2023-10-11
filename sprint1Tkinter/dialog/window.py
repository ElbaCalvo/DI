from tkinter import ttk, Button
from yes_window import show_yes_window
from no_window import show_no_window

## Definimos la clase MainWindow
class MainWindow:
    def __init__(self, root):
        ## Se inicializa la ventana principal
        self.root = root
        self.root.title("Ventana Principal")

        ## Se crea un marco dentro de la ventana
        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        ## Se crea una etiqueta (label) dentro del marco con un texto.
        self.label = ttk.Label(self.frame, text = "blablablabla")
        self.label.pack()

        ## Se crea un botón "SI" que llama a la función show_yes_window al hacer click.
        self.button1 = ttk.Button(self.root, text="Si", command=show_yes_window)
        self.button1.pack(side="left")

        ## Se crea un botón "No" que llama a la función show_no_window al hacer click.
        self.button2 = ttk.Button(self.root, text="No", command=show_no_window)
        self.button2.pack(side="left")