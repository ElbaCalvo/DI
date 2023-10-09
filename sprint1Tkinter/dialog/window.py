from tkinter import ttk, Button
from yes_window import show_yes_window
from no_window import show_no_window

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana Principal")

        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        self.label = ttk.Label(self.frame, text = "blablablabla")
        self.label.pack()

        self.button1 = ttk.Button(self.root, text="Si", command=show_yes_window)
        self.button1.pack(side="left")

        self.button2 = ttk.Button(self.root, text="No", command=show_no_window)
        self.button2.pack(side="left")