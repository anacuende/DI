from PIL import Image, ImageTk
import requests
from io import BytesIO

# Define una clase llamada Cell
class Cell:
    def __init__(self, name, description, image_url):
        self.name = name
        self.description = description
        self.image_url = image_url
        self.load_and_resize_image()

    # Método para cargar y redimensionar la imagen
    def load_and_resize_image(self):
        img = Image.open(self.image_url)
        image = img.resize((100, 100), Image.LANCZOS)
        self.image_tk = ImageTk.PhotoImage(image)
