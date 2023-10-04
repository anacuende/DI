import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana")

        self.label = tk.Label(self.root, text="Hola, mundo!")
        self.label.pack()

        self.button = tk.Button(self.root, text="Haz clic", command=self.button_click)
        self.button.pack()

    def button_click(self):
        self.label.config(text="¡Botón clicado!")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
