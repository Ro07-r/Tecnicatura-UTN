# Ejercicio 3: Funcion recursiva
# Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
# puede ser cualquier valor positivo
# si se ingresan numeros negativos no imprime nada

def imprimir_numeros_recursivos(numero):
    if numero >= 1: # Caso base
        print(numero)
        imprimir_numeros_recursivos(numero-1) # Caso recursivo
valorUsuario = int(input("Ingrese un numero: "))
imprimir_numeros_recursivos(valorUsuario)



