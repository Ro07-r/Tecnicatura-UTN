# Juego adivina el numero
# Realizar un juego para adivinar un numero. Para ello se debe
# generar un numero aleatorio entre 1 - 100, y luego ir pidiendo
# numeros indicando "es mayor" o "es menor" segun lo sea con respecto a N.
# El proceso termina cuando el usuario acierta y alli se debe mostrar el numero de intentos.
import random

aleatorio = random.randint(0, 100)
contador = 0
while True:
    numero = int(input("¡Adivine el número secreto! Ingrese un número: "))
    contador += 1
    if numero > aleatorio:
        print("El numero secreto es menor")
    elif numero < aleatorio:
        print("El numero secreto es mayor")
    elif numero == aleatorio:
        print("¡Felicitaciones! El numero secreto es: ", aleatorio)
        break




