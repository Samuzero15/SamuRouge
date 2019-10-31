
class Rectangulo:
    def __init__(self, x, y, ancho, alto):
        self.x1 = x
        self.y1 = y
        self.x2 = x + ancho
        self.y2 = y + alto

    def centro(self):
        centro_x = int ((self.x1 + self.x2)/ 2)
        centro_y = int ((self.y1 + self.y2)/ 2)
        return (centro_x, centro_y)

    def intersecta(self, otro):
        # retorna True si intersecta con otro rectangulo
        return (self.x1 <= otro.x2 and self.x2 >= otro.x1 and
                self.y1 <= otro.y2 and self.y2 >= otro.y1)