
from random import randint

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

    def crea_mapa(self, max_cuartos, cuar_tam_min, cuar_tam_max, mapa_ancho, mapa_alto, player):
        cuartos = []
        n_cuartos = 0

        for r in range(max_cuartos):

            # Tamaños aleatorios
            an = randint(cuar_tam_min, cuar_tam_max)
            al = randint(cuar_tam_min, cuar_tam_max)
            # Posiciones aleatorias
            x = randint(0, mapa_ancho - an - 1)
            y = randint(0, mapa_alto - al - 1)

            nuevo_cuarto = Rectangulo(x, y, an, al)

            for otro_cuarto in cuartos:
                if nuevo_cuarto.intersecta(otro_cuarto):
                    break
            else:
                self.crea_cuarto(nuevo_cuarto)

                (nuevo_x, nuevo_y) = nuevo_cuarto.centro()

                if n_cuartos == 0:
                    player.x = nuevo_x
                    player.y = nuevo_y
                else:
                    (ant_x, ant_y) = cuartos[n_cuartos - 1].centro()

                    if randint(0,1) == 1:
                        # Primero horizontal y luego vertical
                        self.crea_tunel_h(ant_x, nuevo_x, ant_y)
                        self.crea_tunel_v(ant_y, nuevo_y, nuevo_x)

                    else: # Primero vertical y luego horizontal
                        self.crea_tunel_v(ant_y, nuevo_y, nuevo_x)
                        self.crea_tunel_h(ant_x, nuevo_x, ant_y)

                cuartos.append(nuevo_cuarto)
                n_cuartos += 1


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