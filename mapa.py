
from casilla import Casilla

class Mapa:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.casillas = self.genera_casillas()

    def genera_casillas(self):
        casillas = [[Casilla(True) for y in range(self.alto)] for x in range(self.ancho)]

        return casillas

    def estaBloqueado(self,x,y):
        if self.casillas[x][y].bloqueado:

            return True
        else:
            return False