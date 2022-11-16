class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    @property
    def ancho(self):  # Metodo Getter
        return self._ancho  # Retorna el método get

    @ancho.setter
    def ancho(self, ancho):  # Método Setter
        self._ancho = ancho

    @property
    def alto(self):  # Metodo Getter
        return self._alto  # Retorna el método get

    @alto.setter
    def alto(self, alto):  # Método Setter
        self._alto = alto

    def __str__(self):
        return f'Figura Geometrica: [Ancho: {self._ancho}] [Alto: {self._alto}]'
