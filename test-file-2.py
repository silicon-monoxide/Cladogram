import tkinter as tk
 
# CLADE HEIGHT and CLADE POSITION data
clade_height = {
    'clade0': 0, 'clade1': 0, 'clade2': 0, 'clade3': 0, 'clade4': 0, 'clade5': 0, 'clade6': 0,
    '<clade0>': 1, '<<clade0>>': 2, '<clade5>': 1,
    'clade3clade4<clade5>clade6': 2, 'clade2clade3clade4<clade5>clade6': 3,
    '<<clade0>>clade1clade2clade3clade4<clade5>clade6': 4
}
 
clade_position = {
    'clade0': 0.0, 'clade1': 1.0, 'clade2': 2.0, 'clade3': 3.0, 'clade4': 4.0, 'clade5': 5.0, 'clade6': 6.0,
    '<clade0>': 0.0, '<<clade0>>': 0.0, '<clade5>': 5.0,
    'clade3clade4<clade5>clade6': 4.5, 'clade2clade3clade4<clade5>clade6': 3.25,
    '<<clade0>>clade1clade2clade3clade4<clade5>clade6': 1.4166666666666667
}
 
clade_children = {
    'clade0': [], 'clade1': [], 'clade2': [], 'clade3': [], 'clade4': [], 'clade5': [], 'clade6': [],
    '<clade0>': ['clade0'], '<<clade0>>': ['<clade0>'], '<clade5>': ['clade5'],
    'clade3clade4<clade5>clade6': ['clade3', 'clade4', '<clade5>', 'clade6'],
    'clade2clade3clade4<clade5>clade6': ['clade2', 'clade3clade4<clade5>clade6'],
    '<<clade0>>clade1clade2clade3clade4<clade5>clade6': ['<<clade0>>', 'clade1', 'clade2clade3clade4<clade5>clade6']
}


# Create the main window
root = tk.Tk()
input("text")
root.title("Cladogram")
 
# Create a canvas
canvas_width, canvas_height = 800, 600
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='white')
canvas.pack(padx=10, pady=10)
 
# Calculate scaling factors and offsets
max_x = max(clade_position.values())
max_y = max(clade_height.values())
scale_x = (canvas_width - 100) / max_x  # Leave some margin
scale_y = (canvas_height - 100) / max_y  # Leave some margin
offset_x = 50  # Horizontal margin
offset_y = 50  # Vertical margin
 
# Calculate coordinates
clade_coordinates = {}
for clade in clade_height:
    x = clade_position[clade] * scale_x + offset_x
    y = (max_y - clade_height[clade]) * scale_y + offset_y  # Invert Y-axis
    clade_coordinates[clade] = (x, y)


# Draw the cladogram
for clade, (x, y) in clade_coordinates.items():
    # Draw the clade name
    canvas.create_text(x, y, text=clade[:16], anchor=tk.SW, font=("Arial", 8))
 
    # Draw lines to children
    if clade in clade_children:
        for child in clade_children[clade]:
            child_x, child_y = clade_coordinates[child]
            canvas.create_line(x, y, child_x, child_y, fill="black")
 
# Start the Tkinter event loop
root.mainloop()