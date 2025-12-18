import tkinter as tk
from tkinter import messagebox

class Aplicacion:
    def __init__(self):
        # Configuración de la ventana principal
        self.ventana1 = tk.Tk()
        self.ventana1.title("Selección de Género")
        self.ventana1.geometry("300x250")
        self.ventana1.resizable(False, False)
        self.ventana1.configure(padx=20, pady=20)

        # Variable de control (IntVar para manejar los Radiobuttons)
        # Seteamos 2 por defecto (Mujer) como en tu código original
        self.seleccion = tk.IntVar()
        self.seleccion.set(2)

        # Título decorativo
        self.label_titulo = tk.Label(
            self.ventana1, 
            text="Seleccione su género:", 
            font=("Arial", 12, "bold")
        )
        self.label_titulo.grid(column=0, row=0, pady=(0, 10), sticky="w")

        # Radiobutton para Varón
        self.radio1 = tk.Radiobutton(
            self.ventana1, 
            text="Varón", 
            variable=self.seleccion, 
            value=1,
            font=("Arial", 10)
        )
        self.radio1.grid(column=0, row=1, sticky="w")

        # Radiobutton para Mujer
        self.radio2 = tk.Radiobutton(
            self.ventana1, 
            text="Mujer", 
            variable=self.seleccion, 
            value=2,
            font=("Arial", 10)
        )
        self.radio2.grid(column=0, row=2, sticky="w")

        # Botón de acción
        self.boton1 = tk.Button(
            self.ventana1, 
            text="Mostrar seleccionado", 
            command=self.mostrar_seleccionado,
            bg="#2c3e50",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            padx=10,
            pady=5
        )
        self.boton1.grid(column=0, row=3, pady=20)

        # Etiqueta para mostrar el resultado
        self.label_resultado = tk.Label(
            self.ventana1, 
            text="Esperando selección...", 
            fg="#7f8c8d",
            font=("Arial", 10, "italic")
        )
        self.label_resultado.grid(column=0, row=4)

        # Iniciar el bucle de la aplicación
        self.ventana1.mainloop()

    def mostrar_seleccionado(self):
        """Actualiza la etiqueta según la opción elegida."""
        if self.seleccion.get() == 1:
            texto_final = "Varón"
        else:
            texto_final = "Mujer"
        
        # Cambiamos el color y el texto para que se note el cambio
        self.label_resultado.configure(
            text=f"Opción seleccionada: {texto_final}",
            fg="#27ae60", # Color verde
            font=("Arial", 10, "bold")
        )

# Ejecución del programa
if __name__ == "__main__":
    app = Aplicacion()