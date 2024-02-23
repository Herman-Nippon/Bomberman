import pygame as py

from game.creatures.player import Player
SPEED = 1


def read_keyboard(player: Player):
    # print(player.x, player.y)

    keys = py.key.get_pressed()  # returns a dictionary with pressed keys; no Shift Ctrl Alt
    if keys[py.K_ESCAPE]:
        return "exit"

    if keys[py.K_LEFT]:
        player.move(-SPEED, 0)
    if keys[py.K_RIGHT]:
        player.move(SPEED, 0)
    if keys[py.K_UP]:
        player.move(0, -SPEED)
    if keys[py.K_DOWN]:
        player.move(0, SPEED)
