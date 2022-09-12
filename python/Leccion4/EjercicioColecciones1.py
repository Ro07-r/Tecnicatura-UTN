#Ejercicio 1: Eliminar duplicados de una lista

#CREAMOS UNA LISTA
lista = [20, 18, 10, 20, 20, 28, 18, 17, 17, 10, 20, 20]
print(lista)

#PASAMOS LA LISTA A UN CONJUNTO Y DE ESTA MANERA SE ELIMINAN LOS ELEMENTOS REPETIDOS
#EL CONJUNTO ES EL TIPO QUE NO ACEPTA ELEMENTOS REPETIDOS
conjunto = set(lista)
print(conjunto)

#VOLVEMOS A CONVERTIR A LISTA PARA QUE SE IMPRIMA DE ESA MANERA
lista = list(conjunto)
print(lista)

#MANERA ABREVIADA
lista = list(set(lista))
print(lista)