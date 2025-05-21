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
