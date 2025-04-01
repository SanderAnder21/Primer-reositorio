#Crea un conjunto de 5 elementos, a ese conjunto le vas a agregar un valor que no existe,
#agregar valor que si existe, le vas a eliminar un valor
#que existe, un valor que no existe y vas a verificar si existe un valor

conjunto = {1, 2, 3, 4, 5}
print(conjunto)
conjunto.add(6)  
conjunto.add(3)  
conjunto.remove(2)
conjunto.remove(8) # Esto lanzará un error si 8 no está en el conjunto
conjunto.discard(7)
print(conjunto)
print(3 in conjunto) 
print(7 in conjunto)