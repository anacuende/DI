# Importa la biblioteca tkinter como tk
import tkinter as tk

# Importa las clases Image y ImageTk de la biblioteca PIL (Pillow)
from PIL import Image, ImageTk

# Define una clase llamada DetailWindow
# Agregar al final de tu archivo

class DetailWindow:
    def __init__(self, root, title, image_url, description):
        self.root = root
        root.title("Detalle")
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
