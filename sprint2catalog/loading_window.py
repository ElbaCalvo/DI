import tkinter as tk
from window import MainWindow
import threading
import requests

class LoadingWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Cargando...") # Título de la ventana.
        self.root.geometry("170x120") # Definimos el ancho y alto de una ventana.
        self.root.resizable(False, False) # Evita que la ventana sea redimensionable.
        self.finished = False # Variable para rastrear si la tarea ha finalizado.
        self.json_data = [] # Almacenará los datos JSON descargados.

        # Etiqueta que muestra "Cargando datos...".
        self.label = tk.Label(self.root, text="Cargando datos...", font=("Arial", 14))
        self.label.pack(side = tk.TOP, pady=10) # Coloca la etiqueta en la parte superior.

        # Coge el color del fondo del pestaña.
        label_bg_color = self.label.cget("bg")

        # Se crea un lienzo (canvas) para dibujar un círculo de progreso.
        self.canvas = tk.Canvas(self.root, width=60, bg=label_bg_color)
        self.canvas.pack()

        self.progress = 0 # Inicializa el progreso en 0.

        self.draw_progress_circle(self.progress) # Llama a la función para dibujar el círculo de progreso.

        self.update_progress_circle() # Hace que se actualice el progreso del círculo.

        # Se inicia un hilo.
        self.thread = threading.Thread(target=self.fetch_json_data)
        self.thread.start()

        if self.thread.is_alive():
            self.check_thread()

    def draw_progress_circle(self, progress):
        self.canvas.delete("progress")  # Borra el círculo de progreso anterior.
        angle = int(360 * (progress / 100)) # Calcula el ángulo del círculo de progreso.

        self.canvas.create_arc(10, 10, 35, 35,
                                start=0, extent=angle, tags="progress", outline='green', width=4, style=tk.ARC)

    def update_progress_circle(self):
        if self.progress < 100:
            self.progress += 11 # Incrementa el progreso.
        else:
            self.progress = 0 # Reinicia el progreso.

        self.draw_progress_circle(self.progress) # Actualiza el círculo.
        self.root.after(200, self.update_progress_circle)

    def fetch_json_data(self):
            response = requests.get("https://raw.githubusercontent.com/ElbaCalvo/DI/main/recursos/catalog.json") # Solicitud get a GitHub.
            if response.status_code == 200:
                self.json_data = response.json() # Convierte la respuesta JSON en datos.
                self.finished=True # Marca la tarea como finalizada.

    def check_thread(self):
        if self.finished:
            self.root.destroy() # Cierra la ventana de carga.
            launch_main_window(self.json_data) # Lanza la ventana principal con los datos JSON.
        else:
            self.root.after(100, self.check_thread) # Comprueba periódicamente si la tarea ha finalizado.

# Función para lanzar la ventana principal con datos JSON.
def launch_main_window(json_data):
    root = tk.Tk()
    app = MainWindow(root,json_data)
    root.mainloop()