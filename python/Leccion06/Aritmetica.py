class Aritmetica:
    """
    Vamos a hacer en esta clase algunas operaciones de: suma, resta, multiplicación, etc.
    """
    # Creamos el metodo init (inicializador de los atributos)
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    # Metodo para sumar
    def sumar(self):
        return self.operandoA + self.operandoB

    def resta(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB

# Creamos una instancia de la clase Aritmetica
aritmetica1 = Aritmetica(7, 9) # Le pasamos los argumentos para los operandos
print(aritmetica1.sumar())
print(aritmetica1.resta())
print(aritmetica1.multiplicar())
print(round(aritmetica1.dividir(), 2)) # Con esto indicamos que se muestren solo 2 numeros despues del punto (redondea los numeros flotantes)
