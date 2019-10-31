
class Entidad:
    """
        Un Objeto generico en el que se puede moverse (como un monstruo, objeto, npc o jugador)
    """

    def __init__(self, x, y, color, char):
        self.x = x
        self.y = y
        self.color = color
        self.char = char

    def mueve(self, mx, my):
        self.x += mx;
        self.y += my;
