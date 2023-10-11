# Importa la biblioteca tkinter como tk
import tkinter as tk

# Importa la clase Label de tkinter
from tkinter import Label

# Importa las clases Image y ImageTk de la biblioteca PIL (Pillow)
from PIL import Image, ImageTk

# Define una clase llamada DetailWindow
class DetailWindow:
    def __init__(self, root, title, image_path, description):
        # Guarda la ventana principal en la variable self.root y establece el título
        self.root = root
        self.root.title(title)

        # Crea una etiqueta para el título y la agrega a la ventana
        self.title_label = Label(root, text=title, font=("Times New Roman", 14))
        self.title_label.pack()

        # Abre la imagen y la redimensiona
        self.image = Image.open(image_path)
        self.image.thumbnail((200, 200), Image.ANTIALIAS)

        # Convierte la imagen a un formato compatible con tkinter
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.image_label = Label(root, image=self.image_tk)
        self.image_label.pack()

        # Crea una etiqueta para la descripción y la agrega a la ventana
        self.description_label = Label(root, text=description, font=("Arial", 12))
        self.description_label.pack()
