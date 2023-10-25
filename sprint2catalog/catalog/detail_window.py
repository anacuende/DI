import tkinter as tk
from PIL import Image, ImageTk

# Define una clase llamada DetailWindow
class DetailWindow:
    def __init__(self, root, title, image_url, description):
        # Constructor de la clase DetailWindow, que recibe cuatro parámetros
        self.root = root
        root.title("Detalle")
        # Calcula la posición para centrar la ventana en la pantalla
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}")

        # Crear una etiqueta para el título
        self.title = tk.Label(root, text=title, font=("Arial", 16))
        self.title.pack()

        # Crear una etiqueta para la imagen
        self.image_url = tk.Label(root, image=image_url)
        self.image_url.pack()

        # Crear una etiqueta para la descripción
        self.description = tk.Label(root, text=description, font=("Arial", 12))
        self.description.pack()
