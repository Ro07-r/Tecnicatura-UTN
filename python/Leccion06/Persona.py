"""
class Persona: #Creamos una clase
    #pass (No se procesa nada más. Sirve para cerrar la clase)
    def __init__(self): #Creación de metodos
        self.nombre = "Juan"
        self.apellido = "Perez"
        self.edad = 22
persona1 = Persona() #Instancia de un objeto persona
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
"""

#CREACION DE OBJETOS CON ARGUMENTOS
class Persona:
    def __init__(self, nombre, apellido, edad, *args, **kwargs):
        self.nombre = nombre # 1: atributo 2: variable por argumento
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.args} {self.kwargs}') # La variable self solo se encuentra dentro de los metodos
                                                                                               # Dentro de la clase si queremos acceder a los atributos
                                                                                               # usamos self.atributo


persona1 = Persona('Rosalia', 'Lotierzo', 31) #Necesitamos enviar argumentos
#print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} {persona1.edad}') # Cuando estamos fuera de la clase,
                                                                                                # para acceder a los atributos usamos el objeto


#CREACION DE UN SEGUNDO OBJETO
persona2 = Persona('Cristian', 'Garcia', 50)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} {persona2.edad}')


#MODIFICACION DE ATRIBUTOS DE UN OBJETO
persona1.nombre = 'Sofia'
persona1.apellido = 'Garcia'
persona1.edad = 8
print(f'El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} {persona1.edad}')


#METODOS DE INSTANCIA
persona1.mostrar_detalle() # La referencia en este caso se pasa de manera automatica
persona2.mostrar_detalle()

#UTILIZAR LA CLASE PARA LLAMAR A UN MÉTODO
# Persona.mostrar_detalle(persona1) # Debemos pasarle una referencia para el self o nos dará error

persona1.telefono = '1234765756' # Creamos un atributo de un objeto
print(persona1.telefono)

# print(persona2.telefono) el objeto persona2 no tiene este atributo por ende nos sale error

persona3 = Persona('Sabrina', 'Cisterna', 31, 'Teléfono', '1567654387', 'Calle Jonte', 765, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso=105, Cfavorito='Azul', Auto='Citroen', Modelo=2021)
persona3.mostrar_detalle()
