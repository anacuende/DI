import tkinter as tk
import requests
import threading
from window import Window

class LoadingWindow:
    def __init__(self, root, callback):
        # Inicializar la ventana principal
        self.finished = False
        self.root = root
        self.root.title("Cargando")
        self.root.geometry("170x120")
        self.root.resizable(False, False)
        self.callback = callback

        # Crear una etiqueta en la ventana
        self.label = tk.Label(self.root, text="Cargando datos...", font=("Arial", 14))
        self.label.pack(side=tk.TOP, pady=10)

        # Obtiene el color de fondo de la etiqueta
        label_bg_color = self.label.cget("bg")

        # Crear un lienzo para dibujar la circunferencia
        self.canvas = tk.Canvas(self.root, width=60, height=60, bg=label_bg_color)
        self.canvas.pack()

        # Inicializar la circunferencia en 0 y dibujarla
        self.progress = 0
        self.draw_progress_circle(self.progress)

        # Inicia la actualización de la circunferencia
        self.update_progress_circle()
        self.thread = threading.Thread(target=self.fetch_json_data)
        self.thread.start()
        self.check_data()

    def draw_progress_circle(self, progress):
        # Borra la circunferencia anterior
        self.canvas.delete("progress")
        # Calcula el ángulo del arco de la circunferencia
        angle = 360 * (progress / 100)

        # Dibuja el arco de la circunferencia
        self.canvas.create_arc(10, 10, 50, 50, start=90, extent=angle, tags="progress", outline='green', width=4, style=tk.ARC)

    def update_progress_circle(self):
        if self.progress < 100:
            # Aumenta la circunferencia en 2
            self.progress += 1
        else:
            # Reinicia la circunferencia al alcanzar el 100%
            self.progress = 0

        # Dibuja la nueva circunferencia
        self.draw_progress_circle(self.progress)
        # Programa la próxima actualización
        self.root.after(15, self.update_progress_circle)

    def close_window(self):
        # Cierra la ventana de carga
        self.root.destroy()
        # Llama a la función de devolución de llamada
        self.callback()

    def fetch_json_data(self):
        response = requests.get("https://raw.githubusercontent.com/anacuende/DI/main/recursos/Ejercicio2.json")
        if response.status_code == 200:
            self.json_data = response.json()
            self.finished = True

    def check_data(self):
        if self.finished:
            self.root.destroy()
            launch_main_window(self.json_data)
        else:
            self.root.after(100, self.check_data)

if __name__ == "__main__":
    root = tk.Tk()
    app = LoadingWindow(root, lambda: root.destroy())
    root.mainloop()

def launch_main_window(json_data):
    root = tk.Tk()
    app = Window(root, json_data)
    root.mainloop()