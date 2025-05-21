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