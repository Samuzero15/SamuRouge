
from casilla import Casilla

class Mapa:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.casillas = self.genera_casillas()

    def genera_casillas(self):
        casillas = [[Casilla(False) for y in range(self.alto)] for x in range(self.ancho)]

        casillas[30][22].bloqueado = True;
        casillas[30][22].vision = True;
        casillas[31][22].bloqueado = True;
        casillas[31][22].vision = True;
        casillas[32][22].bloqueado = True;
        casillas[32][22].vision = True;

        return casillas

    def estaBloqueado(self,x,y):
        if self.casillas[x][y].bloqueado:

            return True
        else:
            return False