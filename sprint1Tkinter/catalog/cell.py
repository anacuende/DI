from PIL import Image, ImageTk
import tkinter as tk
from detail_window import DetailWindow

class Cell:
    def __init__(self, title, path, description):
        self.title = title
        self.path = path
        self.description = description
        self.load_and_resize_image()

    def load_and_resize_image(self):
        original_image = Image.open(self.path)
        resized_image = original_image.resize((100, 100), Image.LANCZOS)
        self.image_tk = ImageTk.PhotoImage(resized_image)

    def on_button_clicked(self):
        root = tk.Toplevel()
        detail_window = DetailWindow(root, self.title, self.path, self.description)
