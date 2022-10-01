# Ejercicio11: Agenda telefonica
# Hacer un programa que simule una agenda de contactos. Crear un diccionario donde
# la clave sea el nombre del usuario y el valor sea el telefono. El programa tendra el
# siguiente menu de opciones:
# 1. Nuevo contacto
# 2. Borrar contacto
# 3. Ver contactos existentes
# 4. Salir

agenda = {}
while True:
    print("Menu: ")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")
    opcion = int(input("Digite una opcion: "))
    if opcion == 1:
        nombre = input("Ingrese el nombre: ")
        numero = int(input("Ingrese el numero telefonico: "))
        if nombre not in agenda:
            agenda[nombre] = numero
        else:
            print("El contacto ya existe")
    elif opcion == 2:
        nombre = input("¿Cual es el nombre del contacto que desea borrar?")
        if nombre in agenda:
            del (agenda[nombre])
        else:
            print("El contacto no existe")
    elif opcion == 3:
        print("Agenda de contactos: ")
        for clave, valor in agenda.items():  # items() se utiliza para recorrer la clave y el valor
            print(f'Nombre: {clave}, Numero: {valor}')
    elif opcion == 4:
        print("¡Agenda al día!")
        break
    else:
        print("Seleccionar una opcion del menu")





