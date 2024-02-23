import pygame

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
        self.bomb_count = bomb_count
        self.bombs_list = []



    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def is_collided_with(self, player: Creature):
        if self.hitbox.colliderect(player.hitbox):
            return True

    def check_collision(self, other):
        return self.hitbox.colliderect(other.hitbox)

    def check_collision_tile(self, tile_map: list[list[Tile]]):
        for line in tile_map:
            for tile in line:
                if tile.type == TileType.BORDER:
                    print("Collision border")
                if tile.type == TileType.GRASS:
                    print("Collision tile!")
                if tile.type == TileType.DESTRUCTIBLE:
                    print("Collision tile")

    def drop_bomb(self):
        self.bombs_list.append(Bomb(self.x, self.y, pygame.image.load("../assets/Bomb/Bomb32.png")))
        self.bomb_count -= 1
        print("Bomb count: ",self.bomb_count)



    def action(self):
        pass



