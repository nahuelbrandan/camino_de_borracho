"""Modulo del Campo."""


class Campo:
    """Clase para el campo donde se mueve le borracho."""

    def __init__(self):
        """Inicializa el campo."""
        self.coordenadas_de_borrachos = {}

    def anadir_borracho(self, borracho, coordenada):
        """Agrega un borracho al diccionario."""
        self.coordenadas_de_borrachos[borracho] = coordenada

    def mover_borracho(self, borracho):
        """Mueve al borracho de coordenada."""
        delta_x, delta_y = borracho.camina()
        coordenada_actual = self.coordenadas_de_borrachos[borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)

        self.coordenadas_de_borrachos[borracho] = nueva_coordenada

    def obtener_coordenada(self, borracho):
        """Retorna la coordenada del borracho."""
        return self.coordenadas_de_borrachos[borracho]
