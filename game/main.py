import pygame

from player import Player
from key_input import readKeyboard
from background import Background
from map import Map


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

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pygame.display.update()

    def draw(self):
        self.background.draw(self.screen)
        self.map.draw(self.screen)

        # Show the changes
        #pygame.display.flip()

    def run(self):
        self.running = True
        player = Player(100, 100, pygame.image.load("../assets/Player/player_bomberman.png"), 1)

        while self.running:
            self.handle_events()
            self.draw()
            player.draw(self.screen)
            readKeyboard(player)
            self.update()
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    game = GameLoop()
    game.run()  # main loop
