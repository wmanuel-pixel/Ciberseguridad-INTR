# Crea una calculadora sencilla que pueda sumar y restar dos números usando Labels, Entries y Buttons.

#Inserte la resta a manera de prueba

import tkinter as tk

root = tk.Tk()
root.title("Calculadora")
root.geometry("400x300")

label_num1 = tk.Label(root, text="Número 1:")
label_num1.pack(pady=5)

entry_num1 = tk.Entry(root, width=20)
entry_num1.pack(pady=5)

label_num2 = tk.Label(root, text="Número 2:")
label_num2.pack(pady=5)

entry_num2 = tk.Entry(root, width=20)
entry_num2.pack(pady=5)

def sumar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Error: Ingrese números válidos")

def restar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 - num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Error: Ingrese números válidos")

button_sumar = tk.Button(root, text="Sumar", command=sumar)
button_sumar.pack(pady=5)

button_restar = tk.Button(root, text="Restar", command=restar)
button_restar.pack(pady=5)

label_resultado = tk.Label(root, text="", font=("Arial", 12))
label_resultado.pack(pady=10)

root.mainloop()