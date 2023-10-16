import tkinter as tk

# Definir clase LoadingWindow
class LoadingWindow:
	def __init__(self, root):
        # Inicializar la ventana principal
		self.root = root
        # Establecer el título de la ventana
		self.root.title("Cargando")
        # Establecer el tamaño de la ventana
		self.root.geometry("170x120")
        # Deshabilitar la capacidad de redimensionar la ventana
		self.root.resizable(False, False)
        
		# Crear una etiqueta en la ventana
		self.label = tk.Label(self.root, text="Cargando datos...", font=("Arial", 14))
        # Colocar la etiqueta en la parte superior
		self.label.pack(side=tk.TOP, pady=10)

		# Obtiene el color de fondo de la etiqueta
		label_bg_color = self.label.cget("bg")

		# Crear canvas para dibujar la circunferencia
		self.canvas = tk.Canvas(self.root, width=60, height=60, bg=label_bg_color)
		self.canvas.pack()

		# Inicializar la circunferencia en 0 y dibujarla
		self.progress = 0
		self.draw_progress_circle(self.progress)

		# Inicia la actualización de la circunferencia
		self.update_progress_circle()

	# Función para dibujar la cincunferencia
	def draw_progress_circle(self, progress):
		# Borra la circunferencia anterior
		self.canvas.delete("progress")
		# Calcula el ángulo del arco de la circunferencia
		angle = 360 * (progress / 100)

		# Dibuja el arco de la circunferencia
		self.canvas.create_arc(10, 10, 50, 50, start=90, extent=angle, tags="progress", outline='green', width=4, style=tk.ARC)

	# Función para actualizar la circunferencia
	def update_progress_circle(self):
		if self.progress < 100:
			# Aumenta la circunferencia en 2
			self.progress += 1
		else:
			# Reinicia la circunferencia al alcanzar el 100%
			self.progress = 0

		# Dibuja la nueva circunferencia
		self.draw_progress_circle(self.progress)
		# Programa la próxima actualización
		self.root.after(15, self.update_progress_circle)

# Verifica si el programa se está ejecutando como script principal
if __name__ == "__main__":
	# Crea una instancia de la ventana principal de Tkinter
    root = tk.Tk()
	# Crea una instancia de la ventana de carga
    loading_window = LoadingWindow(root)
	# Inicia el bucle principal de la aplicación para mantener la ventana abierta
    root.mainloop()