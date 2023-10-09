from tkinter import ttk
import tkinter as tk
from cell import Cell
from tkinter import messagebox

class MainWindow():

    ## En el button_on_clicked se crea la pestaña poniendole el título y el texto que se quiera.

    def on_button_clicked(self, cell):
        message = "Esto es un/a " + cell.title
        messagebox.showinfo("Frutas", message)
    
    ## Hacemos una lista de celdas

    def __init__(self, root):
        root.title("Frutas")

        self.cells = [
            Cell("Manzana", "C:\\msys64\\home\\Elba\\DI\\sprint1Tkinter\\catalog\\data\\edited\\manzana_ed.jpg"),
            Cell("Naranja", "C:\\msys64\\home\\Elba\\DI\\sprint1Tkinter\\catalog\\data\\edited\\naranja_ed.jpg"),
            Cell("Plátano", "C:\\msys64\\home\\Elba\\DI\\sprint1Tkinter\\catalog\\data\\edited\\platano_ed.jpg"),
            Cell("Pera", "C:\\msys64\\home\\Elba\\DI\\sprint1Tkinter\\catalog\\data\\edited\\pera_ed.jpg"),
            Cell("Arandanos", "C:\\msys64\\home\\Elba\\DI\\sprint1Tkinter\\catalog\\data\\edited\\arandanos_ed.jpg")
        ]

        ## Recorremos (con el enumerate), almacenando en cada iteración el elemento iterado y su posición.

        for i, cell in enumerate(self.cells):
            ## Por cada iteración creamos una etiqueta label con su título e imagen.
            label = ttk.Label(root, image = cell.image_tk, text=cell.title, compound = tk.BOTTOM)
            ## Agregamos la etiqueta a una matriz.
            label.grid(row=0, column=i)
            ## Indicamos que label está pendiente de pulsar el botón izquierdo del ratón sobre la celda.
            label.bind("<Button-1>", lambda event, celda = cell: self.on_button_clicked(celda))