import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
from cell import Cell  # Importa la clase Cell desde el archivo cell.py

class Window:
    def __init__(self, root, json_data):
        self.data = root
        self.json_data = json_data
        # Establece el título de la ventana principal
        root.title("Ventana")

        # Crear una lista de objetos Cell con los datos del JSON
        self.cells = []
        for data in self.json_data:
            #extraigo los datos de cada JSONObject 
            name = data.get("name")
            description = data.get("description")
            image_url = data.get("image_url")
            
            #Crear una celda para cada dato(object) e incluírla en una lista
            self.datos.append(Cell(name, description, image_url))

        # Itera sobre las celdas y configura las etiquetas correspondientes en la ventana
        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, text=cell.name, image = cell.image_url,compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            # Asocia el evento de clic izquierdo del ratón con la función on_button_clicked
            label.bind("<Button-1>", lambda event, cell=cell: self.on_button_clicked(cell))

    def on_button_clicked(self, cell):
        # Define el mensaje que se mostrará en el cuadro de diálogo
        message = f"Has hecho clic en la celda {cell.name}\n{cell.description}"
        # Muestra un cuadro de diálogo de información con el mensaje
        messagebox.showinfo("Información", message)
