from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from cell import Cell

def detailWindow(cell):

    root = tk.Toplevel()
    root.title("Descripción")

    ## Label destinados a mostrar el título, la imagen y la descripción.
    label1 = ttk.Label(root, text = cell.title)
    label2 = ttk.Label(root, image = cell.image_tk)
    label3 = ttk.Label(root, text = cell.desc)
    label1.pack()
    label2.pack()
    label3.pack()

    root.mainloop()
    
    


