#. Diseña una interfaz con un Canvas donde el usuario pueda dibujar líneas manteniendo presionado el botón del mouse y un botón para borrar todo el dibujo. 

import tkinter as tk
root = tk.Tk()
root.title("Dibujo en Canvas")
root.geometry("600x400")
canvas = tk.Canvas(root, bg="white", width=600, height=350)
canvas.pack(pady=10)
def empezar_dibujo(event):
    canvas.old_x = event.x
    canvas.old_y = event.y
def dibujar(event):
    x, y = event.x, event.y
    canvas.create_line(canvas.old_x, canvas.old_y, x, y, width=2, fill="black", capstyle=tk.ROUND, smooth=tk.TRUE)
    canvas.old_x = x
    canvas.old_y = y
def borrar_dibujo():
    canvas.delete("all")
canvas.bind('<ButtonPress-1>', empezar_dibujo)
canvas.bind('<B1-Motion>', dibujar)
button_borrar = tk.Button(root, text="Borrar Dibujo", command=borrar_dibujo)
button_borrar.pack(pady=10)
root.mainloop()
