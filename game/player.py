import pygame

from npc import Npc
from bomb import Bomb
from tile import TileType, Tile
from сreature import Creature


class Player(Creature):
    def __init__(self, x: int, y: int, image: pygame.Surface, bomb_count: int):
        super().__init__(x,y,image)
        self.x=x
        self.y=y
        self.speed = 5
        self.image = image
        self.hitbox = pygame.Rect(x, y, image.get_width(), image.get_height())
        self.rect = self.image.get_rect()
        self.bomb_count = bomb_count
        self.bombs_list = []



    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def is_collided_with(self, player: Creature):
        if self.hitbox.colliderect(player.hitbox):
            return True

    def check_collision_npc(self, npc: Npc):
        #if self.hitbox.colliderect(npc.hitbox):
        if self.rect.colliderect(npc.rect):
            print("npc collision")
            self.life -= 1
            print(self.life)
            self.death()
            if self.life > 0:
                self.death()
                #todo: spawn places for players
                self.x = 140
                self.y = 48



    def check_collision_tile(self, tile_map: list[list[Tile]]):
        for line in tile_map:
            for tile in line:
                if tile.type == TileType.BORDER:
                    pass
                    #print("Collision border")
                if tile.type == TileType.GRASS:
                    pass
                    #print("Collision grass")
                if tile.type == TileType.DESTRUCTIBLE:
                    pass
                    #print("Collision destructible")
    def can_move(self, dx, dy):
        self.check_collision_tile(self.map.tiles_map)
    def drop_bomb(self):
        self.bombs_list.append(Bomb(self.x, self.y, pygame.image.load("../assets/Bomb/Bomb32.png")))
        self.bomb_count -= 1
        print("Bomb count: ",self.bomb_count)



    def action(self):
        pass

    def death(self):
        #todo: animation of death
        pass

    def gameover(self):
        #todo: end game score, time, go to main menu
        pass



