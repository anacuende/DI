from PIL import Image, ImageTk

class Cell:
    def __init__(self, title, path):
        self.title = title
        self.path = path
        self.load_and_resize_image()

    def load_and_resize_image(self):
        original_image = Image.open(self.path)
        resized_image = original_image.resize((100, 100), Image.LANCZOS)
        self.image_tk = ImageTk.PhotoImage(resized_image)
