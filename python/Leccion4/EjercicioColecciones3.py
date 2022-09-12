# Ejercicio 3: Agregar personajes a una lista
# Escribir un programa donde se cree una lista con los siguientes personajes del Señor de los Anillos

lista = []

diccionario = {
    1: {'Nombre': 'Aragon', 'Clase': 'Guerrero', 'Raza': 'Dunadan del Norte'},
    2: {'Nombre': 'Legolas', 'Clase': 'Arquero', 'Raza': 'Elfo Sindar'},
    3: {'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza': 'Istar'},
    4: {'Nombre': 'Saruman', 'Clase': 'Saruman el Sabio', 'Raza': 'Istari y Ainur'},
    5: {'Nombre': 'Gollum', 'Clase': 'Hobbit', 'Raza': 'Hobbit'},
    6: {'Nombre': 'Eowyn', 'Clase': 'Escudera de Rohan', 'Raza': 'Rohir'},
}

lista.append(diccionario)
print(lista)