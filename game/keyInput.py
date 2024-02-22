import pygame as py

from Bomberman.game.Player import Player


def readKeyboard(player: Player):
    print(player.x, player.y)
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            quit()

        # Проверка когда клавиша нажимается
    keys = py.key.get_pressed() # возвращает словарь с нажатыми клавишами и их состояниями, нет Shift Ctrl Alt
    if keys[py.K_ESCAPE]:
        py.quit()
        quit()

    if keys[py.K_LEFT]:
        player.x -= player.speed
    if keys[py.K_RIGHT]:
        player.x += player.speed
    if keys[py.K_UP]:
        player.y -= player.speed
    if keys[py.K_DOWN]:
        player.y += player.speed


