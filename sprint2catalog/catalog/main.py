import tkinter as tk
from LoadingWindow import LoadingWindow

if __name__ == "__main__":
    # Crear una instancia de la clase Tk de tkinter
    root = tk.Tk()
    # Crear una instancia de la ventana de carga (LoadingWindow)
    loading_app = LoadingWindow(root)
    # Iniciar el ciclo principal del programa
    root.mainloop()
