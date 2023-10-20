from tkinter import ttk
import tkinter as tk
from cell import Cell
from tkinter import messagebox
from detail_window import detailWindow

class MainWindow:
    cells = []

    def showMenu(self):
        messagebox.showinfo("Ayuda", "Desarrolladora: Elba.")

    def __init__(self, root, json_data):
        self.root = root
        ## El titulo de la pestaña.
        self.root.title("Frutas")
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2 # Obtiene el ancho de la pantalla
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2 # Obtiene el alto de la pantalla
        self.root.geometry(f"+{int(x)}+{int(y)}") # Establece la geometría de la ventana de manera que quede centrada
        
        self.root.resizable(False, False)

        barra = tk.Menu() # Crear una barra de menús.
        archivo = tk.Menu(barra, tearoff=False) # Crear el primer menú.

        archivo.add_command(
        label="Acerca del desarrollador",
        command=self.showMenu
        )

        barra.add_cascade(menu=archivo, label="Ayuda") # Agregarlo a la barra.
        self.root.config(menu = barra) # Insertarla en la ventana principal.

        for fruta in json_data: ## For que recorre los elementos del json.
            name = fruta.get("name")
            description = fruta.get("description")
            image_url = fruta.get("image_url")

            cell = Cell(name, description, image_url)
            self.cells.append(cell) # Añade a la lista cell.

        ## Recorremos (con el enumerate), almacenando en cada iteración el elemento iterado y su posición.
        ##for i, cell in enumerate(self.cells):
            ## Por cada iteración creamos una etiqueta label con su título e imagen.
            ##label = ttk.Label(root, image = cell.image_tk, text=cell.title, compound = tk.BOTTOM)
            ## Agregamos la etiqueta a una matriz.
            ##label.grid(row=i, column=0)
            ## Indicamos que label está pendiente de pulsar el botón izquierdo del ratón sobre la celda.
            ##label.bind("<Button-1>", lambda event, celda = cell: detailWindow(celda))
    
        # Creación de un canvas y una barra de desplazamiento
        self.canvas = tk.Canvas(self.root)
        self.scrollbar = tk.Scrollbar(self.root, orient="vertical", command = self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        # Configuración para que se ajuste al tamaño del canvas
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0,0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        for i, cell in enumerate(self.cells):
            self.add_item(cell, i)

        # Colocación de lienzo y barra de desplazamiento en la ventana.
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        # Para que los elementos ocupen todo el espacio disponible
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    # Función para agregar un elemento al marco desplazable
    def add_item(self, cell, i):
        frame = ttk.Frame(self.scrollable_frame)
        frame.pack(pady=10)

        label = ttk.Label(frame, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
        label.grid(row=i, column=0)

        label.bind("<Button-1>", lambda event, celda = cell: detailWindow(celda))