from tkinter import Tk
from window import MainWindow
from loading_window import LoadingWindow

if __name__ == "__main__":
    ## Se crea una instancia de la clase Tk, que representa una ventana.
    root = Tk()
    ## Guardamos la ventana en el root.
    app = LoadingWindow(root)
    ## Lanzamos el bucle principal de la aplicación.
    root.mainloop()