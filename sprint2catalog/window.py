from tkinter import ttk
import tkinter as tk
from cell import Cell
from tkinter import messagebox
from detail_window import detailWindow

class MainWindow:
    cells = []
    
    def __init__(self, root, json_data):
        ## El titulo de la pestaña.
        root.title("Frutas")

        for fruta in json_data: ## For que recorre los elementos del json.
            name = fruta.get("name")
            description = fruta.get("description")
            image_url = fruta.get("image_url")

            cell = Cell(name, description, image_url)
            self.cells.append(cell) # Añade a la lista cell.



        ## Recorremos (con el enumerate), almacenando en cada iteración el elemento iterado y su posición.
        for i, cell in enumerate(self.cells):

            ## Por cada iteración creamos una etiqueta label con su título e imagen.
            label = ttk.Label(root, image = cell.image_tk, text=cell.title, compound = tk.BOTTOM)
            ## Agregamos la etiqueta a una matriz.
            label.grid(row=i, column=0)
            ## Indicamos que label está pendiente de pulsar el botón izquierdo del ratón sobre la celda.
            ##label.bind("<Button-1>", lambda event, celda = cell: detailWindow(celda))