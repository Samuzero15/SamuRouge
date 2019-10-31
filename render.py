import tcod as libtcod

from mapa import Mapa

def render_todo(entidades, consola, mapa, ancho, alto, colores):

    #Casillas del mapa
    for y in range(mapa.alto):
        for x in range(mapa.ancho):
            pared = mapa.casillas[x][y].vision

            if(pared):
                libtcod.console_set_char_background(consola, x, y, colores.get("pared_oscura"), libtcod.BKGND_SET)
            else:
                libtcod.console_set_char_background(consola, x, y, colores.get("suelo_oscuro"), libtcod.BKGND_SET)

    #Entidades del mapa
    for ent in entidades:
        render_entidad(ent, consola)

    libtcod.console_blit(consola, 0, 0, ancho, alto, 0 ,0, 0)

def limpia_todo(entidades, consola):
    for ent in entidades:
        limpia_entidad(ent, consola)

def render_entidad (ent, consola):
    # renderiza esta entidad.
    libtcod.console_set_default_foreground(consola, ent.color)
    libtcod.console_put_char(consola, ent.x, ent.y, ent.char, libtcod.BKGND_NONE)

def limpia_entidad (ent, consola):
    libtcod.console_put_char(consola, ent.x, ent.y, ' ', libtcod.BKGND_NONE)