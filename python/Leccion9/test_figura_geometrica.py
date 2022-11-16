# Hoja para testear

from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado(7, 'Azul')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f'El área del cuadrado es: {cuadrado1.calcular_area()}')

# Método MRO: Method Resolution Order
print(Cuadrado.mro())

print(cuadrado1) # Acá no hace falta poner el .ancho o .alto porque ya se declaró el método str
print(f'El área del cuadrado es: {cuadrado1.calcular_area()}')

rectangulo1 = Rectangulo(5, 4, 'Verde')
print(rectangulo1)
print(f'El área del rectángulo es: {rectangulo1.calcular_area()}')
