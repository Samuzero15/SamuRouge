import tcod as libtcod

from input_handler import key_handler
from entidad import Entidad
from render import render_todo, limpia_todo
from mapa import Mapa

def main():
    pantalla_ancho = 80
    pantalla_alto = 50

    centX = int (pantalla_ancho / 2)
    centY = int (pantalla_alto / 2)

    mapa_ancho = pantalla_ancho
    mapa_alto = 45

    colores = {
        'pared_oscura': libtcod.Color(0,0,100),
        'suelo_oscuro': libtcod.Color(50,50,150)
    }

    player = Entidad(centX, centY, libtcod.turquoise,'@')
    bystander = Entidad(centX + 5, centY, libtcod.white, '0')

    entidades = [player, bystander]

    libtcod.console_set_custom_font("arial10x10.png", libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(pantalla_ancho, pantalla_alto, "SamuRouge!", False)

    con = libtcod.console_new(pantalla_ancho, pantalla_alto)

    mapa_juego = Mapa(mapa_ancho, mapa_alto)
    mapa_juego.crea_mapa()

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():

        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        libtcod.console_set_default_foreground(con, libtcod.white)

        render_todo(entidades, con, mapa_juego, pantalla_ancho, pantalla_alto, colores)

        libtcod.console_flush()

        limpia_todo(entidades, con)

        action = key_handler(key)
        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx,dy = move
            if not mapa_juego.estaBloqueado(player.x + dx, player.y + dy):
                player.mueve(dx,dy)

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

if __name__ == '__main__':
    main()