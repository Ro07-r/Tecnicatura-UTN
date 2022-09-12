#Ejercicio 2: Operaciones de conjuntos con listas
#Escribir un programa que tenga 2 listas: (No se deben repetir los elementos)
# 1 Lista de palabras que aparecen en las listas
# 2 Lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 Lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 lista de palabras que aparecen en ambas listas

# 1
lista1 = ["Cristian", "Sofia", "Sofia", "Laura", "Rosalia", "Rosalia"]
lista2 = ["Cristian", "Alma", "Julieta", "Sofia", "Noelia", "Noelia"]

lista1 = (set(lista1))
lista2 = (set(lista2))

print(f'Lista de palabras que aparecen en la lista 1: {lista1}')
print(f'Lista de palabras que aparecen en la lista 2: {lista2}')

# 2
lista3 = lista1 - lista2
print(f'La lista de palabras que aparecen en la primera lista pero no en la segunda son: {lista3}')
lista3 = lista2 - lista1
print(f'La lista de palabras que aparecen en la segunda lista pero no en la primera son: {lista3}')

# 4
lista3 = (lista1 | lista2)
print(lista3)




