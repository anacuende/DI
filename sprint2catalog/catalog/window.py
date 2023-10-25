import tkinter as tk
from tkinter import messagebox, Label, Frame, Scrollbar, Canvas
from PIL import Image, ImageTk, UnidentifiedImageError
import requests
from io import BytesIO
from cell import Cell
from detail_window import DetailWindow

class Window:
    def __init__(self, root, json_data):
        # Establece los datos de la ventana principal
        self.data = root
        self.json_data = json_data
        # Establece el título de la ventana principal
        root.title("Ventana")
        # Calcula la posición para centrar la ventana en la pantalla
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
        root.geometry(f"+{int(x)}+{int(y)}")
        
        # Crea un lienzo (canvas) para la interfaz principal
        self.canvas = tk.Canvas(root)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Crea una barra de desplazamiento vertical
        scrollbar = tk.Scrollbar(root, command=self.canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.config(yscrollcommand=scrollbar.set)

        # Crea un marco (frame) que contendrá los elementos desplazables
        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor=tk.NW)

    
        # Crear una lista de objetos Cell con los datos del JSON
        self.datas = []
        for data in self.json_data:
            # Extrae los datos de cada JSONObject 
            name = data.get("name")
            description = data.get("description")
            url = data.get("image_url")
            img = self.load_image_from_url(url)
            
            # Crear una celda para cada dato(object) e incluírla en una lista
            self.datas.append(Cell(name, description, img))

        # Itera sobre las celdas y configura las etiquetas correspondientes en la ventana
        for i, cell in enumerate(self.datas):
            label = tk.Label(self.frame, text=cell.name, image=cell.image_url, compound=tk.BOTTOM)
            label.pack()
            # Asocia el evento de clic izquierdo del ratón con la función on_button_clicked
            label.bind("<Button-1>", lambda event, cell=cell: self.on_button_clicked(cell))
            label.config(anchor="center")
        # Ajusta el lienzo y el marco para que funcione con la barra de desplazamiento
        self.frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        
        # Crea un menú en la ventana principal
        self.create_menu(root)
    
    def create_menu(self, root):
        # Crea una barra de menú
        menubar = tk.Menu(root)
        root.config(menu=menubar)

        # Menú "Ayuda"
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=help_menu)

        # Elemento "Acerca de" en el menú "Ayuda"
        help_menu.add_command(label="Acerca de", command=self.show_about_dialog)

    # Cargar la imagen desde la url
    def load_image_from_url(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Verifica si la solicitud es exitosa
            image_data = Image.open(BytesIO(response.content))
            foto = ImageTk.PhotoImage(image_data)
            return foto
        except requests.exceptions.RequestException as e:
            # Manejo de error de solicitud
            print(f"Error en la solicitud: {e}")
        except UnidentifiedImageError as e:
            # Manejo de error de imagen no identificada
            print(f"Error al abrir la imagen: {e}")
        except Exception as e:
            # Otros errores
            print(f"Error inesperado: {e}")
        return None

    # Abrir la ventana DetailWindow al clicar en una celda
    def on_button_clicked(self, cell):
        # Abre una nueva ventana emergente para mostrar detalles del elemento
        root = tk.Toplevel()
        # Muestra un cuadro de diálogo de información "Acerca de"
        detail_window = DetailWindow(root, cell.name, cell.image_url, cell.description)

    # Abrir el diálogo del menú
    def show_about_dialog(self):
        messagebox.showinfo("Acerca de", "Desarrollado por Ana Betsabé Cuende Tomé")
