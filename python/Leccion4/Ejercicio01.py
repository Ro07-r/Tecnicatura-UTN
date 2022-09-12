# Ejercicio 1: Llenar una lista
# Llenar una lista con los numeros del 1 al 50: 1-2-3-4-5...-50
# Mostrar la lista con un bucle for

lista1 = []
for x in range(1, 51):
    lista1.append(x)
for x in lista1:
    print(x, end='-') # Imprime guiones

print('\n') # Imprime un salto de linea

lista2 = []
x = 0
while x < 51:
    lista2.append(x)
    x += 1
for x in lista2:
    print(x, end='-')
