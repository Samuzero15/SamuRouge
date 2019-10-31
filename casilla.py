
class Casilla:
    def __init__(self, bloqueado, vision = None):
        self.bloqueado = bloqueado

        if(vision == None):
            vision = bloqueado;

        self.vision = vision;