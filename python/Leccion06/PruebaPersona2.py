from Persona2 import Persona2 # Si ponemos * en lugar de Persona2 al final, podemos importar todas las clases o funciones del modulo Persona2

if __name__ == '__main__': # Sirve para imprimir unicamente lo que está dentro de PruebaPersona2 (Comprobación del módulo principal en ejecución)
    persona5 = Persona2('Lionel', 'Messi', 35)
    persona5.mostrar_detalles()

    print(__name__)