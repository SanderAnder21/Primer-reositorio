import numpy as np

arreglo = np.array([1, 2, 3, "4", 5])
lista = [1, "hola", True, 3.2, 5]
tuplaNp = tuple(arreglo)
tuplaLista = tuple(lista)
conjuntoNp = set(arreglo)
conjuntoLista = set(lista)
diccionario = {"cadena": "Juan", 
               "entero": 24, 
               "Booleano": True,
               "decimal": 3.2,
               "entero": 1}
print(tuplaNp)
print(tuplaLista)
print(conjuntoNp)
print(conjuntoLista)
print(diccionario)