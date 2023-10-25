import tkinter as tk
import requests
import threading
from window import Window

class LoadingWindow:
    def __init__(self, root):
        # Inicializar la ventana principal
        self.finished = False
        self.root = root
        # Establece el título de la ventana
        self.root.title("Cargando")
        # Establece el tamaño de la ventana
        self.root.geometry("170x120")
        # Bloquea el redimensionamiento de la ventana
        self.root.resizable(False, False)
        # Calcula la posición para centrar la ventana en la pantalla
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}")

        # Crear una etiqueta en la ventana
        self.label = tk.Label(self.root, text="Cargando datos...", font=("Arial", 14))
        # Coloca la etiqueta en la parte superior con un espacio en la parte superior
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
        # Inicia un subproceso para obtener los datos JSON
        self.thread = threading.Thread(target=self.fetch_json_data)
        self.thread.start()
        # Verifica si el subproceso está en ejecución
        if self.thread.is_alive():
            self.check_data()

    # Dibuja la circunferencia de progreso
    def draw_progress_circle(self, progress):
        # Borra la circunferencia anterior
        self.canvas.delete("progress")
        # Calcula el ángulo del arco de la circunferencia
        angle = 360 * (progress / 100)

        # Dibuja el arco de la circunferencia
        self.canvas.create_arc(10, 10, 50, 50, start=90, extent=angle, tags="progress", outline='green', width=4, style=tk.ARC)

    # Actualiza el progreso de la circunferencia
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

    # Realiza una solicitud HTTP para obtener datos JSON
    def fetch_json_data(self):
        response = requests.get("https://raw.githubusercontent.com/anacuende/DI/main/recursos/Ejercicio2.json")
        if response.status_code == 200:
            # Almacena los datos JSON si la solicitud fue exitosa
            self.json_data = response.json()
            self.finished = True

    # Verifica si los datos se han cargado y muestra la ventana principal o sigue esperando
    def check_data(self):
        if self.finished:
            self.root.destroy()
            # Lanza la ventana principal con los datos cargados
            launch_main_window(self.json_data)
        else:
            # Programa la verificación nuevamente después de 100 milisegundos
            self.root.after(100, self.check_data)

# Función para lanzar la ventana principal con datos JSON
def launch_main_window(json_data):
    root = tk.Tk()
    app = Window(root, json_data)
    root.mainloop()