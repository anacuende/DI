# Importa la biblioteca tkinter como tk
import tkinter as tk

# Importa la clase Label de tkinter
from tkinter import Label
import requests
# Importa las clases Image y ImageTk de la biblioteca PIL (Pillow)
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import ttk
from main import Main
# Define una clase llamada DetailWindow
# Agregar al final de tu archivo

class DetailWindow:
    def __init__(self, root, title, image_url, description):
        self.root = root
        self.root.title("Detalle")

        # Crear una etiqueta para el título
        title_label = tk.Label(root, text=title, font=("Arial", 16))
        title_label.pack()

        # Descargar y mostrar la imagen
        response = requests.get(image_url)
        image_data = response.content if response.status_code == 200 else b''  # Tratamiento de errores
        image = Image.open(BytesIO(image_data))
        image.thumbnail((200, 200), Image.ANTIALIAS)
        image_tk = ImageTk.PhotoImage(image)
        image_label = tk.Label(root, image=image_tk)
        image_label.image = image_tk  # Evitar que el recolector de basura elimine la imagen
        image_label.pack()

        # Crear una etiqueta para la descripción
        description_label = tk.Label(root, text=description, font=("Arial", 12))
        description_label.pack()

# Modificar la clase Window para abrir la ventana de detalle al hacer clic en una celda
class Window:
    def __init__(self, root, json_data):
        # ... (código existente)

        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            label.bind("<Button-1>", lambda event, cell=cell: self.on_button_clicked(cell))

    def on_button_clicked(self, cell):
        detail_root = tk.Toplevel(self.root)
        detail_window = DetailWindow(detail_root, cell.title, cell.image_url, cell.description)

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()
