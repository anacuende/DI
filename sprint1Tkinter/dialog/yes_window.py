import tkinter as tk

class YesWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana I")

        self.label = tk.Label(self.root, text="Sí")
        self.label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = YesWindow(root)
    root.mainloop()
