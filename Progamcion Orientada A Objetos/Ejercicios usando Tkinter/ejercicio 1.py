# Ejercicio 1: Crear una ventana simple con Tkinter que muestre un mensaje de bienvenida.

import tkinter as tk

root = tk.Tk()
root.title("Ejercicio 1")
root.geometry("400x200")

label_bienvenida = tk.Label(root, text="¡Bienvenido a mi aplicación!", font=("Arial", 12))
label_bienvenida.pack(pady=20)

root.mainloop()