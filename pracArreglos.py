import numpy as np

class Arreglos:
    def __init__(self, v):
        self.arregloNP = np.array(v)
    def insertar(self, v):
        self.arregloNP = np.append(self.arregloNP,v)
        print(f"su nuev0 arreglo es: {self.arregloNP}")
    def eliminar(self, indice):
        if 0 <= indice < len(self.arregloNP):
            self.arregloNP = np.delete(self.arregloNP, indice)
            print(f"su nuev0 arreglo es: {self.arregloNP}")
        else:
            print("Índice fuera de rango.")
    def modificar(self, indice, V):
        self.arregloNP[indice] = V
        print(f"su nuevo arreglo es: {self.arregloNP}")

class Lista:
    def __init__(self):
        self.arregloLista = ['2','4','6']
    def insertarList(self, v):
        self.arregloLista.append(v)
        print(f"su nueva lista es: {self.arregloLista}")
    def eliminarList(self, indice):
        if 0 <= indice < len(self.arregloLista):  
            eliminado = self.arregloLista.pop(indice) 
            print(f"Se eliminó {eliminado}. Su nueva lista es: {self.arregloLista}")
        else:
            print("Índice fuera de rango.")
    def modificarList(self, indice, v):
        self.arregloLista[indice] = v
        print(f"su nueva lista es: {self.arregloLista}")

arreglo = Arreglos([10, 20, 30])

lista = Lista()

v = input("Ingree el valor a insertar: ")
lista.insertarList(v)
arreglo.insertar( v)

indice = int(input("ingrese el indice a eliminar: "))
lista.eliminarList(indice)
arreglo.eliminar(indice)

v = input("Ingree el nuevo valor: ")
indice = int(input("ingrese el indice a modificar: "))
lista.modificarList(indice, v)
arreglo.modificar(indice, v)