import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from cell import Cell
from PIL import Image, ImageTk

class Window:
    def on_button_clicked(self, cell):
        message = "Has hecho clic en la celda " + cell.title
        messagebox.showinfo("Información", message)

    def __init__(self, root):
        root.title("Ventana")

        self.cells = [
            Cell("Tomb Raider Anniversary", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\unedited\\imagen1.png"),
            Cell("Crash Bandicoot: The Wrath of Cortex", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\unedited\\imagen2.png"),
            Cell("Assassins Creed Syndicate", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\unedited\\imagen3.png"),
            Cell("Detroit Become Human", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\unedited\\imagen4.png"),
            Cell("Marvel Spider-Man", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\unedited\\imagen5.png")
        ]

        for i, cell in enumerate(self.cells):
            img = Image.open(cell.path)
            image = img.resize((100, 100), Image.Resampling.LANCZOS)
            cell.image_tk = ImageTk.PhotoImage(image)
            
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            label.bind("<Button-1>", lambda event, cell=cell: self.on_button_clicked(cell))