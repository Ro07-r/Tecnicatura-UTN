# Funciones recursivas
def factorial(numero):
    if numero == 1: # Caso base
        return 1
    else:
        return numero * factorial(numero-1) # Caso recursivo

resultado = factorial(5) # Lo hacemos en codigo duro
print(f'El factorial del numero 5 es: {resultado}')

# Valor ingresado por el usuario
def factorial(numero):
    if numero == 1: # Caso base
        return 1
    else:
        return numero * factorial(numero-1) # Caso recursivo

resultado = int(input("Ingrese un numero: "))
print(f'El factorial del numero {resultado} es: {factorial(resultado)}')


# Desempaquetado de listas o list unpacking
def show(name, lastName):
    print(name+' '+lastName)
person = ['Ariel', 'Betancud']
show(person[0], person[1]) # Pasamos uno por uno los datos de la lista a la funcion
show(*person) # Esto es lo mismo que lo anterior pero lo pasamos todo junto
person2 = ('Cristian', 'Garcia') # Desempaquetamos a traves de una tupla
show(*person2)
person3 = {'lastName': 'Lotierzo', 'name': 'Rosalia'}
show(**person3) # Los 2 asteriscos equivalen a la llave y valor del diccionario

bottleC = [{"name": "Andes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella", "country": "Belgium"},
           ]
Arg = [c for c in bottleC if c["country"] == "Belgium"] # Es como un buscador
print(Arg)

names = ["Paolo", "Rodrigo", "Lupe", "Cris"]
alongP = [p for p in names if p[1] == 'a'] # Esto regresa una nueva lista
print(alongP)

# La palabra return en funciones
# Creamos una funcion para sumar
def sumar(a, b):
    return a + b
print(f'El resultado de la suma es: {sumar(55, 45)}')


def listarTerminos(**terminos): # Los dos asteriscos equivalen a la llave y al valor
    for llave, valor in terminos.items():
        print(f'{llave} : {valor}')

listarTerminos() # No recibe nada, nada se va a mostrar
listarTerminos(IDE='Integrated Development Environment', PK='Primary Key')









