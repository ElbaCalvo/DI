import tkinter as tk
from PIL import Image, ImageTk

class Cell:
    def __init__(self, title, path):
        self.title = title
        self.path = path

        ## Reescalamos una imagen dándole nuevos valores al ancho y al alto.
        foto = Image.open(self.path)
        foto_red = foto.resize((100, 100), Image.Resampling.LANCZOS)
        self.image_tk = ImageTk.PhotoImage(foto_red)