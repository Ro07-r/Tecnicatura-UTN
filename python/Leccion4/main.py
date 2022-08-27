# 16/08 COLECCIONES (LISTAS - TUPLAS -SET)
# LISTAS (MANTIENE UN ORDEN Y SE PUEDE MODIFICAR)
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
# print(nombres) #Nos sale error porque ya habiamos eliminado la lista

# TUPLAS (MANTIENE UN ORDEN Y NO SE PUEDE MODIFICAR)
# Definir una tupla
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))

# Acceder a un elemento (se utilizan corchetes)
print(cocina[0])

# Acceder a un rango
print(cocina[0:1]) # Imprime y devuelve como tupla ('cuchara',)
                   # Se necesita la coma para que sea una tupla y NO un string

# Recorrer los elementos de una tupla
for cocinar in cocina:
    #print(cocinar) # Print esta usando \n para saltos de linea
    print(cocinar, end=' ') # Usamos end= para eliminar los saltos de linea

cocinaLista = list(cocina) # Ahora la tupla cocina la pasamos a lista y se guarda en la variable cocinaLista
cocinaLista[0] = 'Plato' # Modificacion del primer elemento
cocina = tuple(cocinaLista) # Aca hacemos la conversion de lista a tupla
print('\n', cocina)

# La unica funcion que se puede utilizar con las tuplas es: DELETE
# del cocina
# print(cocina)

# SET (NO TIENE UN ORDEN Y NO PERMITE ALMACENAR ELEMENTOS DUPLICADOS)
# SET (NO SE PUEDE MODIFICAR, UNICAMENTE AGREGAR O ELIMINAR)
# SET (NO MANTIENE UN INDICE, EL ORDEN ES COMPLETAMENTE ALEATORIO)

planetas = {'Marte', 'Júpiter', 'Venus'}
print(planetas)
print(len(planetas))

# Revisar si un elemento existe dentro de set
print('Marte' in planetas)
print('Júpiter' not in planetas)

# Agregar un elemento
planetas.add('Tierra')
print(planetas)

# Eliminar elementos
planetas.remove('Júpiter') # Esta funcion puede arrojar un error si el elemento no existe o está mal ingresado
print(planetas)
planetas.discard('Tierra') # Esta funcion no arroja error
print(planetas)

# Limpiar set o conjunto
planetas.clear()
print(planetas)

# Eliminar set o conjunto
del planetas
# print(planetas) # al eliminar el set nos muestra error, el set ya no existe

# DICCIONARIO (Esta compuesto por 2 elementos: llave y valor)
# DICCIONARIO (No tiene indice al igual que SET)
# DICCIONARIO (Puede modificarse)
diccionario = {
    'IDE':'Integrated Development Enviornment',
    'POO':'Programacion Orientada a Objetos',
    'SABD':'Sistema de Administracion de Base de Datos',
}
print(diccionario)
print(len(diccionario))

# Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))

# Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)




