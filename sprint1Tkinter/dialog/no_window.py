# Importa la biblioteca tkinter como tk
import tkinter as tk

# Define una clase llamada NoWindow
class NoWindow:
    def __init__(self, root):
        self.root = root
        # Establece el título de la ventana
        self.root.title("Ventana NO")

        # Crea una etiqueta en la ventana con el texto "No"
        self.label = tk.Label(self.root, text="No")
        self.label.pack()

if __name__ == "__main__":
    # Crea una instancia de la clase Tk para crear la ventana principal
    root = tk.Tk()
    # Crea una instancia de la clase NoWindow en la ventana principal
    app = NoWindow(root)
    # Inicia el bucle principal de la aplicación para mantener la ventana abierta
    root.mainloop()
