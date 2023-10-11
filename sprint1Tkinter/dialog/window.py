# Importa la biblioteca tkinter como tk
import tkinter as tk

# Importa la clase YesWindow desde el módulo yes_window
from yes_window import YesWindow

# Importa la clase NoWindow desde el módulo no_window
from no_window import NoWindow

# Define una clase llamada App
class App:
	def __init__(self, root):
        	self.root = root
		# Establece el título de la ventana principal
        	self.root.title("Ventana")

		# Crea una etiqueta en la ventana con el texto "Hola, mundo!"
        	self.label = tk.Label(self.root, text="Hola, mundo!")
		self.label.pack()

		# Crea un botón en la ventana con el texto "Haz clic" y vincula la función button_click al evento de clic
		self.button = tk.Button(self.root, text="Haz clic", command=self.button_click)
		self.button.pack()

		# Crea una etiqueta en la ventana con el texto "¿Tienes mascotas?"
		self.label = tk.Label(self.root, text="¿Tienes mascotas?")
		self.label.pack()

		# Crea un botón "Sí" en la ventana y vincula la función open_yes_window al evento de clic
		self.button_yes = tk.Button(self.root, text="Sí", command=self.open_yes_window)
		self.button_yes.pack()

		# Crea un botón "No" en la ventana y vincula la función open_no_window al evento de clic
		self.button_no = tk.Button(self.root, text="No", command=self.open_no_window)
		self.button_no.pack()

	def button_click(self):
		# Cambia el texto de la etiqueta cuando se hace clic en el botón
		self.label.config(text="¡Botón clicado!")
	
	def open_yes_window(self):
		# Crea una nueva ventana emergente (Toplevel) y una instancia de la clase YesWindow en ella
        	yes_window = tk.Toplevel()
        	app = YesWindow(yes_window)

    	def open_no_window(self):
		# Crea una nueva ventana emergente (Toplevel) y una instancia de la clase NoWindow en ella
        	no_window = tk.Toplevel()
        	app = NoWindow(no_window)

if __name__ == "__main__":
	# Crea una instancia de la clase Tk para crear la ventana principal
	root = tk.Tk()
	# Crea una instancia de la clase App en la ventana principal
	app = App(root)
	# Inicia el bucle principal de la aplicación para mantener la ventana abierta
	root.mainloop()
