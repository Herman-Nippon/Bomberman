import pygame

from game.creatures.сreature import Creature
from game.map.tile import Tile, TileType


class Player(Creature):
    def __init__(self, x: int, y: int, image: pygame.Surface, bomb_count: int):
        super().__init__(x, y, image)
        self.x = x
        self.y = y
        self.speed = 5
        self.image = image
        self.hitbox = pygame.Rect(x, y, image.get_width(), image.get_height())
        self.bomb_count = bomb_count

    def update(self):
        self.hitbox.y = self.y
        self.hitbox.x = self.x

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def is_collided_with(self, player: Creature):
        return self.hitbox.colliderect(player.hitbox)

    def check_collision_tile(self, tiles_map: list[list[Tile]]):
        for line in tiles_map:
            for tile in line:
                if tile.type == TileType.BORDER or tile.type == TileType.DESTRUCTIBLE:
                    if self.hitbox.colliderect(tile.hitbox):
                        print("Collision!")
