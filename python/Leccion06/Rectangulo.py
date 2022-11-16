class Rectangulo:
    """
    Crear una clase llamada Rectangulo. Debe tener 2 atributos: altura y base.
    El nombre del metodo sera calcular_area utilizando la formula: area = base * altura.
    Pero la base y la altura deben ser ingresadas por el usuario y los objetos deben ser tres.
    """
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.altura * self.base

base = int(input("Digite el numero para la base del rectangulo: "))
altura = int(input("Digite el numero para la altura del rectangulo: "))

#Instanciamos un objeto de la clase rectangulo
rectangulo1 = Rectangulo(base, altura)
print(f'El area del rectangulo es: {rectangulo1.calcular_area()}')