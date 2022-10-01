# Ejercicio 5: Convertidos de temperaturas
# Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa.
# Investigar las formulas

# Funcion para convertir de grados celsius a fahrenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    print(f'{celsius} grados celsius equivalen a {fahrenheit} grados fahrenheit')

celsius_a_fahrenheit(35)

# Funcion para convertir de grados fahrenheit a celsius
def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    print(f'{fahrenheit} grados fahrenheit equivalen a {celsius} grados celsius')

fahrenheit_a_celsius(70)
