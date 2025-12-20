#Crea una clase **Vehiculo** con un método mover(). Crea clases hijas como Carro y Bicicleta que implementen su propia versión del método mover().
class Vehiculo:
    def mover(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")
class Carro(Vehiculo):
    def mover(self):
        return "El carro está conduciendo por la carretera."
class Bicicleta(Vehiculo):
    def mover(self):
        return "La bicicleta está pedaleando por el sendero."   
# Ejemplo de uso
carro = Carro() 
bicicleta = Bicicleta()
print(carro.mover())        # Salida: El carro está conduciendo por la carretera.
print(bicicleta.mover())    # Salida: La bicicleta está pedaleando
# por el sendero.
