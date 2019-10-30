import tcod as libtcod

from input_handler import key_handler

def main():
    pantalla_ancho = 80
    pantalla_alto = 50

    playX = int (pantalla_ancho / 2)
    playY = int (pantalla_alto / 2)

    libtcod.console_set_custom_font("arial10x10.png", libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(pantalla_ancho, pantalla_alto, "SamuRouge!", False)

    con = libtcod.console_new(pantalla_ancho, pantalla_alto)

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():

        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        libtcod.console_set_default_foreground(con, libtcod.white)

        libtcod.console_put_char(con, playX, playY, '@', libtcod.BKGND_NONE)
        libtcod.console_blit(con,0,0,pantalla_ancho, pantalla_alto, 0 ,0 ,0)

        libtcod.console_flush()

        libtcod.console_put_char(con, playX, playY, ' ', libtcod.BKGND_NONE)

        action = key_handler(key)
        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx,dy = move
            playX += dx;
            playY += dy;

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

if __name__ == '__main__':
    main()