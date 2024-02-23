import pygame
import os

from game.creatures.npc import Npc
from game.creatures.player import Player
from game.inputs.key_input import read_keyboard
from game.map.background import Background
from game.map.map import Map


class GameLoop:
    def __init__(self):
        pygame.init()

        screen_width = 1200
        screen_height = 800
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Bomberman")

        self.background = Background(screen_width, screen_height)

        self.map = Map(self.screen)
        self.map.create_map()

        self.clock = pygame.time.Clock()

        self.running = False

        self.player1 = Player(self.map.tiles_map[1][1].x, self.map.tiles_map[1][1].y, pygame.image.load(os.getcwd() + "\\..\\assets\\Player\\player_bomberman.png"), 1,
                              self.map.tile_size, self.map.tiles_map)
        # self.player2 = Player(300, 300, pygame.image.load(os.getcwd() + "\\..\\assets\\Player\\player_bomberman.png"),
        #                       1)
        # self.npc1 = Npc(500, 500, pygame.image.load(os.getcwd() + "\\..\\assets\\Player\\apple_npc.png"))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        if read_keyboard(self.player1) == "exit":
            self.running = False

    def update(self):
        self.player1.update_hitbox()
        self.player1.check_collision_tile(self.map.tiles_map)
        pass

    def draw(self):
        self.background.draw(self.screen)
        self.map.draw(self.screen)

        self.player1.draw(self.screen)
        # self.player2.draw(self.screen)
        # self.npc1.draw(self.screen)

        # Show the changes
        pygame.display.update()

    def run(self):
        self.running = True

        while self.running:
            self.handle_events()
            self.draw()
            self.update()
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    game = GameLoop()
    game.run()  # main loop
