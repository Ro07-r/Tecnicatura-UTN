# Ejercicio 2: Modificar los elementos de una lista
# Llenar una lista con los numeros del 1 al 10
# Modificar los elementos de la lista multiplicandolos por el valor ingresado por el usuario

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Lista original: ", '\n', lista)
num = int(input("Ingrese un numero a multiplicar: "))
for i in lista:
    print(num*lista[i])
