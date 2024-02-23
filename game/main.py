import pygame

from npc import Npc
from tile import TileType
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

        self.player1 = Player(140, 48, pygame.image.load("../assets/Player/player_bomberman.png"), 1)
        self.player2 = Player(300, 300, pygame.image.load("../assets/Player/player_bomberman.png"),1)
        self.npc1 = Npc(500, 500, pygame.image.load("../assets/Player/apple_npc.png"))
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        # if self.player1.hitbox.colliderect(self.player2.hitbox):
        #     print("Hi friend")
        # if self.player1.hitbox.colliderect(self.player2.hitbox.topleft, self.player2.hitbox.bottomright):
        #     print("Hi friend")
        # for line in self.map.tiles_map:
        #     for tile in line:
        #         if self.player1.hitbox.collidepoint(tile.x, tile.y) and tile.type == TileType.DESTRUCTIBLE:
        #             print("Collision with destructible tile")
        #         if self.player1.hitbox.collidepoint(tile.x, tile.y) and tile.type == TileType.BORDER:
        #             print("Collision with border")
        #         if self.player1.hitbox.collidepoint(tile.x, tile.y) and tile.type == TileType.GRASS:
        #             print("Collision with grass tile!")
        #print(self.npc1.check_collision(self.player1))
        self.player1.check_collision_tile(self.map.tiles_map)
        self.player2.check_collision_tile(self.map.tiles_map)
        #todo npc list

        self.player1.check_collision_npc(self.npc1)
        self.player2.check_collision_npc(self.npc1)



        #test revers collision
        if self.npc1.check_collision(self.player1):
            #todo animation for npc bite
            pass
            #print("npc bite player1")
        pygame.display.update()

    def draw(self):
        self.background.draw(self.screen)
        self.map.draw(self.screen)


    def run(self):
        self.running = True

        while self.running:
            self.handle_events()
            self.draw()

            #draw players
            self.player1.draw(self.screen)
            self.player2.draw(self.screen)
            self.npc1.draw(self.screen)

            #draw bombs
            #todo: extract to method
            for bomb in self.player1.bombs_list:
                bomb.draw(self.screen)
            for bomb in self.player2.bombs_list:
                bomb.draw(self.screen)

            #read keyboard
            readKeyboard(self.player1,1)
            readKeyboard(self.player2,2)

            self.update()
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    game = GameLoop()
    game.run()  # main loop
