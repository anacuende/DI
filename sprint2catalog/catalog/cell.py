# Importa las clases Image y ImageTk de la biblioteca PIL (Pillow)
from PIL import Image, ImageTk

# Importa la biblioteca tkinter como tk
import tkinter as tk

# Importa la clase DetailWindow desde el módulo detail_window
from detail_window import DetailWindow

# Define una clase llamada Cell
class Cell:
    def __init__(self, title, path, description):
        self.title = title
        self.path = path
        self.description = description
        self.load_and_resize_image()

    # Método para cargar y redimensionar la imagen
    def load_and_resize_image(self):
        original_image = Image.open(self.path)
        resized_image = original_image.resize((100, 100), Image.LANCZOS)
        self.image_tk = ImageTk.PhotoImage(resized_image)

    # Método para manejar el clic en un botón
    def on_button_clicked(self):
        # Crea una nueva ventana emergente (Toplevel)
        root = tk.Toplevel()
        
        # Crea una instancia de la clase DetailWindow en la nueva ventana
        detail_window = DetailWindow(root, self.title, self.path, self.description)
