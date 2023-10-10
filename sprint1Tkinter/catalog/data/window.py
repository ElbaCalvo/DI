from tkinter import ttk
import tkinter as tk
from cell import Cell
from tkinter import messagebox
from detail_window import detailWindow

class MainWindow():

    ## En el button_on_clicked se crea la pestaña poniendole el título y el texto que se quiera.

    ##def on_button_clicked(self, cell):
    ##   message = "Esto es un/a " + cell.title
    ##   messagebox.showinfo("Frutas", message)
    
    ## Hacemos una lista de celdas

    def __init__(self, root):
        root.title("Frutas")

        self.cells = [
            Cell("Manzana", "C:\\msys64\\home\\Elba\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\manzana_uned.jpg", "Fruta versátil y nutritiva, fuente de vitaminas y fibra, ideal para meriendas y platos saludables."),
            Cell("Naranja", "C:\\msys64\\home\\Elba\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\naranja_uned.jpg", "La naranja, fruta cítrica, es jugosa, dulce y llena de vitamina C, perfecta para refrescarse y disfrutar."),
            Cell("Plátano", "C:\\msys64\\home\\Elba\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\platano_uned.jpg", "Deliciosa fruta amarilla, fuente de energía y potasio, ideal para un snack saludable."),
            Cell("Pera", "C:\\msys64\\home\\Elba\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\pera_uned.jpg", "Fruta jugosa, dulce y rica en fibra, ideal para un bocado fresco y saludable."),
            Cell("Arandanos", "C:\\msys64\\home\\Elba\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\arandanos_uned.jpg", "Pequeñas joyas azules, llenas de antioxidantes y sabor fresco, perfectas para postres y desayunos.")
        ]

        ## Recorremos (con el enumerate), almacenando en cada iteración el elemento iterado y su posición.

        for i, cell in enumerate(self.cells):

            ## Por cada iteración creamos una etiqueta label con su título e imagen.
            label = ttk.Label(root, image = cell.image_tk, text=cell.title, compound = tk.BOTTOM)
            ## Agregamos la etiqueta a una matriz.
            label.grid(row=0, column=i)
            ## Indicamos que label está pendiente de pulsar el botón izquierdo del ratón sobre la celda.
            label.bind("<Button-1>", lambda event, celda = cell: detailWindow(celda))