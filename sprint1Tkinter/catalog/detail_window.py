import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk

class DetailWindow:
    def __init__(self, root, title, image_path, description):
        self.root = root
        self.root.title(title)
        
        self.title_label = Label(root, text=title, font=("Times New Roman", 14))
        self.title_label.pack()
        
        self.image = Image.open(image_path)
        self.image.thumbnail((200, 200), Image.ANTIALIAS)
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.image_label = Label(root, image=self.image_tk)
        self.image_label.pack()
        
        self.description_label = Label(root, text=description, font=("Arial", 12))
        self.description_label.pack()