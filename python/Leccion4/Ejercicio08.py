# Menu interactivo - cajero automatico
# Hacer un programa que simule un cajero automatico con un saldo inicial de $1000
# con el siguiente menu de opciones:
# 1. Ingresar dinero en la cuenta
# 2. Retirar dinero de la cuenta
# 3. Mostrar dinero disponible
# 4. Salir

saldo_inicial = 1000
saldo_actual = 0
opcion = ''
while True:
    print("Menu de opciones")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")
    opcion = int(input("Digite una opcion: "))
    if opcion == 1:
        ingresar_dinero = float(input("¿Cuanto dinero desea ingresar a la cuenta?"))
        saldo_actual = saldo_inicial + ingresar_dinero
        print(f'Su saldo actual es: ${saldo_actual}')
    elif opcion == 2:
        retiro = float(input("¿Cuanto dinero desea extraer?"))
        if retiro > saldo_actual:
            print("No dispone de esa cantidad de dinero")
        else:
            saldo_actual = saldo_actual - retiro
    elif opcion == 3:
        print(f'Dinero disponible en cuenta: ${saldo_actual}')
    elif opcion == 4:
        print("¡Gracias por su visita!")
        break
    else:
        print("Se equivoco de opcion")












