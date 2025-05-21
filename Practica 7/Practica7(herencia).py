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


