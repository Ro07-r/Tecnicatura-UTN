# Sacar la raiz cuadrada de un numero ingresado por pantalla
import math
num = int(input("Ingresar un positivo: "))
while num < 0:
    num = int(input("Ingresar un positivo: "))
#raizCuadrada = math.sqrt(num)
#print(f"La raiz cuadrada del numero ingresado {num} es: {raizCuadrada}")
print(f"La raiz cuadrada del numero ingresado {num} es: {math.sqrt(num):.2f}") # Esto sirve para que no nos largue tantos decimales

