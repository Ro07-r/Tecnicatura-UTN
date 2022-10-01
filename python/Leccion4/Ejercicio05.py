# Factorial de un numero positivo
# Hacer un programa para calcular el factorial de un numero positivo

import math
num = int(input("Ingrese un numero positivo: "))
while num < 0:
    num = int(input("Ingrese un numero positivo: "))
print(f'El factorial del numero {num} es: {math.factorial(num)}')
