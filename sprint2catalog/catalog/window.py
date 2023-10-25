import tkinter as tk
from PIL import Image, ImageTk, UnidentifiedImageError
import requests
from io import BytesIO
from cell import Cell  # Importa la clase Cell desde el archivo cell.py
from detail_window import DetailWindow

class Window:
    def __init__(self, root, json_data):
        self.data = root
        self.json_data = json_data
        # Establece el título de la ventana principal
        root.title("Ventana")
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
        root.geometry(f"+{int(x)}+{int(y)}")

        # Crear una lista de objetos Cell con los datos del JSON
        self.datas = []
        for data in self.json_data:
            #extraigo los datos de cada JSONObject 
            name = data.get("name")
            description = data.get("description")
            url = data.get("image_url")
            img = self.load_image_from_url(url)
            
            #Crear una celda para cada dato(object) e incluírla en una lista
            self.datas.append(Cell(name, description, img))

        # Itera sobre las celdas y configura las etiquetas correspondientes en la ventana
        for i, cell in enumerate(self.datas):
            label = tk.Label(root, text=cell.name, image=cell.image_url, compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            # Asocia el evento de clic izquierdo del ratón con la función on_button_clicked
            label.bind("<Button-1>", lambda event, cell=cell: self.on_button_clicked(cell))

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

    def on_button_clicked(self, cell):
        root = tk.Toplevel()
        detail_window = DetailWindow(root, cell.name, cell.image_url, cell.description)
    