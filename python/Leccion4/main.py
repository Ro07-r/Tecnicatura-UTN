# 16/08
# Lista = Ariel, Liliana, Natalia, Osvaldo
nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
print(nombres)
print(nombres[0])
print(nombres[-1])  # [3]

print(nombres[0:2])  # Muestra la posicion 0 y la posicion 1
print(nombres[ :3])  # Muestra el indice 0, el indice 1 y el indice 2
print(nombres[1: ])  # Muestra desde el indice indicado hasta el final

# Modificamos un valor
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)

#Iterar una lista
for nombre in nombres:  # nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

# Preguntamos cuantos elementos tiene la lista
print(len(nombres))

# Agregamos un elemento (se agrega al final de la lista)
nombres.append('Marcelo')
print(nombres)

# Insertar un elemento en un indice especifico
nombres.insert(1, 'Alberto')  # Indicamos la posicion de esa manera y luego el objeto que queremos añadir en dicha posicion
print(nombres)

# Eliminar un elemento
nombres.remove('Alberto')
print(nombres)

# Eliminar el ultimo elemento de la lista
nombres.pop()
print(nombres)

# Eliminar un indice especifico
del nombres[2]
print(nombres)

# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar lista
# del nombres
# print(nombres)



