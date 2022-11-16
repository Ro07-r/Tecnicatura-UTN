class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Color: {self.color} Cantidad de ruedas: {str(self.ruedas)}'

class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'Velocidad (Km/Hr): {str(self.velocidad)} {super().__str__()}'

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'Modelo: {self.tipo} {super().__str__()}'


vehiculo1 = Vehiculo('Rojo', 4)
print(vehiculo1)

auto1 = Auto('Verde', 4, 100)
print(auto1)

bicicleta1 = Bicicleta('Rosa', 2, 'Montaña')
print(bicicleta1)

