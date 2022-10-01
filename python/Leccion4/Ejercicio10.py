# Ejercicio 10: No repetir caracteres
# Hacer un programa que pida una cadena por teclado, luego
# meter los caracteres en una lista sin repetir caracteres

lista = []
cadena = input("Introduzca una palabra: ")
lista.append(cadena)
lista = list(set(cadena))
print(lista)
