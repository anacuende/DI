# Importa la biblioteca tkinter como tk
import tkinter as tk

# Importa la subclase ttk y el módulo messagebox desde tkinter
from tkinter import ttk
from tkinter import messagebox

# Importa la clase Cell desde el módulo cell
from cell import Cell

# Importa las clases Image y ImageTk de la biblioteca PIL (Pillow)
from PIL import Image, ImageTk

# Define una clase llamada Window
class Window:
    def on_button_clicked(self, cell):
        # Define el mensaje que se mostrará en el cuadro de diálogo
        message = "Has hecho clic en la celda " + cell.title + "\n" + cell.description
        # Muestra un cuadro de diálogo de información con el mensaje
        messagebox.showinfo("Información", message)

    def __init__(self, root):
        # Establece el título de la ventana principal
        root.title("Ventana")

        # Crea una lista de objetos Cell con títulos, rutas de imágenes y descripciones
        self.cells = [
            Cell("Tomb Raider Anniversary", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\unedited\\imagen1.png", "Inspirado en el primer videojuego de la saga Tomb Raider, que se publicó en 1996, Lara Croft Tomb Raider: Anniversary nos trae una aventura actualizada de Lara, preservando de forma fidedigna los elementos que convirtieron el juego original Tomb Raider en un clásico, del que se han vendido más de 7 millones de unidades en todo el mundo."),
            Cell("Crash Bandicoot: The Wrath of Cortex", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\unedited\\imagen2.png", "Juego de plataformas en el que el jugador controla a Crash Bandicoot y Coco, cuyo objetivo es reunir 25 cristales y derrotar a los principales antagonistas de la historia: Doctor Neo Cortex, su nueva super arma Crunch Bandicoot y las fuentes de energía de Crunch, Los Elementales."),
            Cell("Assassins Creed Syndicate", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\unedited\\imagen3.png", "Cuenta la historia de Jacob y Evie Frye, dos hermanos asesinos que buscan la liberación de la ciudad de Londres, Inglaterra, de las manos templarias, en mitad del siglo XIX, en 1868."),
            Cell("Detroit Become Human", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\unedited\\imagen4.png", "Se trata de un androide con forma humana fabricada con una nueva conciencia artificial, lo que la hace escapar de las instalaciones donde fue creada, para intentar vivir entre los humanos como una más y encontrar su lugar en un mundo donde los robots son utilizados como meros sirvientes de la sociedad."),
            Cell("Marvel Spider-Man", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\unedited\\imagen5.png", "Hablamos de un Peter Parker veterano que ha pulido sus habilidades combatiendo el crimen en la Nueva York de Marvel. A su vez, también lucha por poner en orden su caótica vida personal y su carrera, con el destino de millones de neoyorquinos en sus manos.")
        ]
        
        # Itera sobre las celdas y configura las etiquetas correspondientes en la ventana
        for i, cell in enumerate(self.cells):
            img = Image.open(cell.path)
            image = img.resize((100, 100), Image.Resampling.LANCZOS)
            cell.image_tk = ImageTk.PhotoImage(image)
            
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            # Asocia el evento de clic izquierdo del ratón con la función on_button_clicked
            label.bind("<Button-1>", lambda event, cell=cell: self.on_button_clicked(cell))
