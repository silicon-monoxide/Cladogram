import tkinter as tk
from tkinter import font as tkfont

def create_canvas_with_text():
    root = tk.Tk()
    root.title("Tkinter Canvas Text Sizes Example")

    canvas = tk.Canvas(root, width=400, height=300, bg="white")
    canvas.pack(pady=20)

    base_font = tkfont.Font(family="Arial", size=12)

    text_sizes = [12, 16, 20, 24, 28]
    y_position = 50

    for size in text_sizes:
        font = base_font.copy()
        font.configure(size=size)
        canvas.create_text(
            200, y_position, 
            text=f"Font size: {size}", 
            font=font, 
            fill="black"
        )
        y_position += size + 10

    root.mainloop()

if __name__ == "__main__":
    create_canvas_with_text()