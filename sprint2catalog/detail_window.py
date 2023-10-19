from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from cell import Cell

def detailWindow(cell):

    ## Creamos una ventana emergente con su respectivo título.
    det_root = tk.Toplevel() 
    det_root.title(cell.title)
    x = (det_root.winfo_screenwidth() - det_root.winfo_reqwidth()) / 2 # Obtiene el ancho de la pantalla
    y = (det_root.winfo_screenheight() - det_root.winfo_reqheight()) / 2 # Obtiene el alto de la pantalla
    det_root.geometry(f"+{int(x)}+{int(y)}") # Establece la geometría de la ventana de manera que quede centrada

    ## Distintos label destinados a mostrar el título, la imagen y la descripción.
    label1 = ttk.Label(det_root, text = cell.title)
    label2 = ttk.Label(det_root, image = cell.image_tk)
    label3 = ttk.Label(det_root, text = cell.desc)
    label1.pack()
    label2.pack()
    label3.pack()

    ## Lanzamos el bucle principal.
    det_root.mainloop()    


