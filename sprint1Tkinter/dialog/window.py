import tkinter as tk
from yes_window import YesWindow
from no_window import NoWindow

class App:
	def __init__(self, root):
        	self.root = root
        	self.root.title("Ventana")

        	self.label = tk.Label(self.root, text="Hola, mundo!")
		self.label.pack()

		self.button = tk.Button(self.root, text="Haz clic", command=self.button_click)
		self.button.pack()
	
		self.label = tk.Label(self.root, text="¿Tienes mascotas?")
		self.label.pack()

		self.button_yes = tk.Button(self.root, text="Sí", command=self.open_yes_window)
		self.button_yes.pack()

		self.button_no = tk.Button(self.root, text="No", command=self.open_no_window)
		self.button_no.pack()

	def button_click(self):
		self.label.config(text="¡Botón clicado!")
	
	def open_yes_window(self):
        	yes_window = tk.Toplevel()
        	app = YesWindow(yes_window)

    	def open_no_window(self):
        	no_window = tk.Toplevel()
        	app = NoWindow(no_window)

if __name__ == "__main__":
	root = tk.Tk()
	app = App(root)
	root.mainloop()
