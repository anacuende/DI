import tkinter as tk

class NoWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana NO")

        self.label = tk.Label(self.root, text="No")
        self.label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = NoWindow(root)
    root.mainloop()
