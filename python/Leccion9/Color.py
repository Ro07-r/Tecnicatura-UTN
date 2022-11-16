class Color:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):  # Metodo Getter
        return self._color  # Retorna el método get

    @color.setter
    def color(self, color):  # Método Setter
        self._color = color

    def __str__(self):
        return f'Color: {self._color}'
