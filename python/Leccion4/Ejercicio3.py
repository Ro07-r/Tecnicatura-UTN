# Ejercicio 3: Insertar elementos y ordenarlos
# Pedir numeros y agregarlos en una lista hasta que se ingrese el numero 0
# Mostrar los elementos de menor a mayor

# Funciona pero imprime dentro de la lista el valor 0
lista = []
num = ''
while num != 0:
    num = int(input("Ingresar un numero: "))
    lista.append(num)
lista.sort()
print(f'Lista de valores ingresados ordenados de menor a mayor: {lista}')

# Version profesor (No incluye el numero 0 a la lista)
listaNueva = []
salir = False # Creamos una bandera
while not salir:
    numero = int(input("Digite un numero: "))
    if numero == 0:
        salir = True # Aca es donde descarta el numero 0
    else:
        listaNueva.append(numero) # Aca es donde agrega los valores ingresados que son distinto de 0
listaNueva.sort()
print(f'Lista de valores ingresados ordenados de menor a mayor: {listaNueva}')

