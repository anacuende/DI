# Importa la clase App desde el módulo window
from window import App

# Importa la biblioteca tkinter como tk
import tkinter as tk

# Comprueba si el programa se está ejecutando como script principal
if __name__ == "__main__":
    # Crea una instancia de la clase Tk para crear la ventana principal
    root = tk.Tk()
    # Crea una instancia de la clase App en la ventana principal
    app = App(root)
    # Inicia el bucle principal de la aplicación para mantener la ventana abierta
    root.mainloop()
