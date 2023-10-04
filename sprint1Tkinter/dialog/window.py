from tkinter import ttk, Button

class MainWindow:
    def on_button_click(self):
        pass
    def __init__(self, root):
        self.root = root

        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        self.label = ttk.Label(self.frame, text = "Etiqueta")
        self.label.pack()

        self.button = ttk.Button(self.root, text="Botón", command=self.on_button_click)
        self.button.pack()