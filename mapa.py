
from casilla import Casilla
from rectangulo import Rectangulo

class Mapa:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.casillas = self.genera_casillas()

    def genera_casillas(self):
        casillas = [[Casilla(True) for y in range(self.alto)] for x in range(self.ancho)]

        return casillas

    def crea_mapa(self):
        cuarto1 = Rectangulo(20, 15, 10, 15)
        cuarto2 = Rectangulo(35, 15, 10, 15)

        self.crea_cuarto(cuarto1)
        self.crea_tunel_h(25, 40, 23)
        self.crea_cuarto(cuarto2)

    def crea_tunel_h(self, x1, x2, y):
        for x in range(min(x1, x2),max(x1, x2)+ 1):
            self.casillas[x][y].bloqueado = False;
            self.casillas[x][y].vision = False;

    def crea_tunel_v(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.casillas[x][y].bloqueado = False;
            self.casillas[x][y].vision = False;

    def crea_cuarto(self, cuarto):
        for y in range(cuarto.y1 + 1, cuarto.y2):
            for x in range(cuarto.x1 + 1, cuarto.x2):
                self.casillas[x][y].bloqueado = False;
                self.casillas[x][y].vision = False;

    def estaBloqueado(self,x,y):
        if self.casillas[x][y].bloqueado:

            return True
        else:
            return False