# Importa la biblioteca tkinter como tk
import tkinter as tk

# Importa la clase Window desde el módulo window
from window import Window

# Importa la clase Cell desde el módulo cell
from cell import Cell

# Comprueba si el programa se está ejecutando como script principal
if __name__ == "__main__":
    # Crea una instancia de la clase Tk para crear la ventana principal
    root = tk.Tk()
    # Crea una instancia de la clase Window en la ventana principal
    app = Window(root)
    # Inicia el bucle principal de la aplicación para mantener la ventana abierta
    root.mainloop()
