# DADA LA SIGUIENTE TUPLA
# CREAR UNA LISTA QUE SOLO INCLUYA LOS NUMEROS MENORES A 5
# IMPRIMA POR PANTALLA [1, 3, 2]

print('OPCION NUMERO 1')
tupla = (13, 1, 8, 3, 2, 5, 8)
for numero in tupla:
    if numero < 5:
        print(numero, end=' ')

print('\nOPCION PROFESOR')
lista = []  # Se crea una lista vacia
tupla = (13, 1, 8, 3, 2, 5, 8)  # Definimos la tupla
for numero in tupla:
    if numero < 5:
        lista.append(numero)  # Agregamos el valor a la lista
print(lista)