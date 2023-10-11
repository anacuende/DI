# Importa la biblioteca tkinter como tk
import tkinter as tk

# Define una clase llamada YesWindow
class YesWindow:
    def __init__(self, root):
        self.root = root
        # Establece el título de la ventana
        self.root.title("Ventana I")

        # Crea una etiqueta en la ventana con el texto "Sí"
        self.label = tk.Label(self.root, text="Sí")
        self.label.pack()

if __name__ == "__main__":
    # Crea una instancia de la clase Tk para crear la ventana principal
    root = tk.Tk()
    # Crea una instancia de la clase YesWindow en la ventana principal
    app = YesWindow(root)
    # Inicia el bucle principal de la aplicación para mantener la ventana abierta
    root.mainloop()
