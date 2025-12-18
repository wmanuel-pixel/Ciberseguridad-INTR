# una ventana con un Listbox que muestre una lista de elementos. Agrega un botón para añadir nuevos elementos a la lista.

import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
root = tk.Tk()
root.title("Lista de Elementos")
root.geometry("400x300")
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=20)
def agregar_elemento():
    nuevo_elemento = simpledialog.askstring("Agregar Elemento", "Ingrese el nuevo elemento:")
    if nuevo_elemento:
        listbox.insert(tk.END, nuevo_elemento)
        messagebox.showinfo("Información", "Elemento agregado exitosamente")
button_agregar = tk.Button(root, text="Agregar Elemento", command=agregar_elemento)
button_agregar.pack(pady=10)
root.mainloop()

