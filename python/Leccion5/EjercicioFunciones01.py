# Ejercicio 1: crear una funcion para sumar los valores recibidos de tipo numericos,
# utilizando argumentos variables *args como parametro de la funcion y agregar como resultado
# la suma de todos los valores pasados como argumentos
def sumar(*args): # Recibimos una cantidad de parametros indefinidos
    resultado = 0
    # Iteramos cada elemento
    for valor in args:
        resultado += valor
    print(resultado)

sumar(5, 22, 40, 32)




