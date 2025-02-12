class Coche:
    def __init__(self, marca, modelo):
        self.__marca = marca  # Atributo privado
        self.__modelo = modelo  # Atributo privado

    # Métodos públicos para acceder a los atributos privados
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

# Uso
mi_coche = Coche("Toyota", "Corolla")
print(mi_coche.get_marca())  # Acceso controlado
mi_coche.set_modelo("Camry")  # Modificación controlada
print(mi_coche.get_modelo())

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def describir(self):
        return f"Vehículo de marca: {self.marca}"

class Coche(Vehiculo):  # Hereda de Vehiculo
    def __init__(self, marca, modelo):
        super().__init__(marca)  # Llama al constructor de la clase base
        self.modelo = modelo

    def describir(self):
        return f"Coche: {self.marca} {self.modelo}"

# Uso
mi_coche = Coche("Toyota", "Corolla")
print(mi_coche.describir())  # Método heredado y extendido

class Animal:
    def sonido(self):
        pass  # Método abstracto

class Perro(Animal):
    def sonido(self):
        return "¡Guau!"

class Gato(Animal):
    def sonido(self):
        return "¡Miau!"

# Función que usa polimorfismo
def hacer_sonar(animal):
    print(animal.sonido())

# Uso
mi_perro = Perro()
mi_gato = Gato()

hacer_sonar(mi_perro)  # ¡Guau!
hacer_sonar(mi_gato)  # ¡Miau!

from abc import ABC, abstractmethod

class Figura(ABC):  # Clase abstracta
    @abstractmethod
    def area(self):
        pass  # Método abstracto

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * (self.radio ** 2)

# Uso
mi_cuadrado = Cuadrado(5)
mi_circulo = Circulo(3)

print(f"Área del cuadrado: {mi_cuadrado.area()}")  # 25
print(f"Área del círculo: {mi_circulo.area()}")  # 28.2744