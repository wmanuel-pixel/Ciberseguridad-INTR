# Crea una clase base llamada **Animal** con un método hablar(). Luego crea clases hijas como Perro y Gato que sobreescriban el método.

class animal:

    def hablar(self):
        raise NotImplementedError("Subclase debe implementar este método")

class Perro(animal):
    def hablar(self):
        return "Guau"

class Gato(animal):
    def hablar(self):
        return "Miau"
# Prueba las clases creando instancias de Perro y Gato y llamando al método hablar().
if __name__ == "__main__":
    mi_perro = Perro()
    mi_gato = Gato()
    
    print("El perro dice:", mi_perro.hablar())
    print("El gato dice:", mi_gato.hablar())
