# Tabla de multiplicar
# Hacer un programa que pida un numero por teclado y guarde
# en una lista su tabla de multiplicar hasta el 10.

lista = []
num = int(input("Ingrese un numero: "))
for x in range(1, 11):
    lista.append(num*x)
print(f'La tabla de multiplicar del numero ingresado {num} es: {lista}')
