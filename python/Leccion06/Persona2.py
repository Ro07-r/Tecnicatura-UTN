class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre # Con el guion bajo encapsulamos. Cuando encapsulamos no deberíamos modificar
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

# Para cada uno de los atributos necesitamos crear un método set y get

    @property # Vamos a necesitar para acceder al metodo como atributo y de manera indirecta un decorador
    def nombre(self): # Metodo Getter
        print('Estamos utilizando el método get')
        return self._nombre # Retorna el método get

    @nombre.setter
    def nombre(self, nombre): # Método Setter
        print('Estamos utilizando el método set')
        self._nombre = nombre

    @property
    def apellido(self): # Metodo Getter
        print('Estamos utilizando el método get')
        return self._apellido

    @apellido.setter
    def apellido(self, apellido): #Metodo Setter
        print('Estamos utilizando el método set')
        self._apellido = apellido

    @property
    def edad(self): # Metodo Getter
        print('Estamos utilizando el método get')
        return self._edad

    @edad.setter
    def edad(self, edad): # Metodo Setter
        print('Estamos utilizando el método set')
        self._edad = edad

if __name__ == '__main__': # Sirve para mostrar unicamente lo que está dentro de Persona2 (Comprobación del módulo principal en ejecución)
    persona1 = Persona2('Rosalía', 'Lotierzo', 31)
    print(persona1.nombre) # Llamamos al método getter
    print(persona1.apellido)
    print(persona1.edad)
    persona1.mostrar_detalles()

    # Para llamar al método Set
    persona1.nombre = "Sofía hermosa"
    print(persona1.nombre)

    persona1.mostrar_detalles()

    # PUEDE HABER ATRIBUTOS QUE NO TENGAN EL METODO SET, A ESTOS SE LOS LLAMA: Atributos read-only (solo lectura)

    # TAREA: Crear 3 objetos más, utilizando los métodos getter y setter
    # para modificar y mostrar los cambios con el método mostrar_detalles()
    persona2 = Persona2('Cristian', 'Garcia', 50) # Primer objeto
    persona2.mostrar_detalles()
    persona2.nombre = 'The G man'
    persona2.apellido = 'Garcia man'
    persona2.edad = 37
    persona2.mostrar_detalles()

    persona3 = Persona2('Sofia', 'Garcia', 8) # Segundo objeto
    persona3.mostrar_detalles()
    persona3.nombre = 'Tatunia'
    persona3.apellido = 'Lotierzo'
    persona3.edad = 9
    persona3.mostrar_detalles()

    persona4 = Persona2('Rosalia', 'Lotierzo', 31) # Tercer objeto
    persona4.mostrar_detalles()
    persona4.nombre = 'La Rosalia'
    persona4.apellido = 'De Garcia'
    persona4.edad = 32
    persona4.mostrar_detalles()

    print(__name__)




