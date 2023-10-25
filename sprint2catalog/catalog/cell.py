from PIL import Image, ImageTk
import requests
from io import BytesIO

# Define una clase llamada Cell
class Cell:
    def __init__(self, name, description, image_url):
        # Constructor de la clase Cell, que recibe tres parámetros
        self.name = name
        self.description = description
        self.image_url = image_url
