# Crea una interfaz con un Entry y un Button. Al presionar el botón, muestra el texto escrito en el Entry en un Label.

import tkinter as tk

root = tk.Tk()
root.title("Ejercicio 2")
root.geometry("400x200")

entry_texto = tk.Entry(root, width=30)
entry_texto.pack(pady=10)

label_resultado = tk.Label(root, text="", font=("Arial", 12))
label_resultado.pack(pady=10)

def mostrar_texto():
    texto = entry_texto.get()
    label_resultado.config(text=texto)

button_mostrar = tk.Button(root, text="Mostrar Texto", command=mostrar_texto)
button_mostrar.pack(pady=10)

root.mainloop()