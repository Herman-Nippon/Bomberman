import pygame

from game.creatures.сreature import Creature
from game.map.tile import Tile, TileType


class Player:
    def __init__(self, x: int, y: int, image: pygame.Surface, bomb_count: int, tile_size: int, tiles_map: list[list[Tile]]):
        # self.x = x
        # self.y = y
        self.speed = 1

        self.tile_size = tile_size
        self.tiles_map = tiles_map

        self.tile_x = x // tile_size
        self.tile_y = y // tile_size

        self.image = image
        self.hitbox = pygame.Rect(self.tile_x * tile_size, self.tile_y * tile_size, tile_size, tile_size)
        self.bomb_count = bomb_count

    def move(self, dx, dy):
        new_tile_x = self.tile_x + dx
        new_tile_y = self.tile_y + dy

        # Check if the new position is within the bounds of the game field
        if 0 <= new_tile_x < len(self.tiles_map[0]) and 0 <= new_tile_y < len(self.tiles_map):
            # Check if the new position is not a border tile
            if self.tiles_map[new_tile_y][new_tile_x] != 0:
                self.tile_x = new_tile_x
                self.tile_y = new_tile_y

    def update_hitbox(self):
        self.hitbox.topleft = (self.tile_x * self.tile_size, self.tile_y * self.tile_size)

    def draw(self, screen):
        screen.blit(self.image, (self.tile_x * self.tile_size, self.tile_y * self.tile_size))

    def check_collision_tile(self, tiles_map: list[list[Tile]]):
        for line in tiles_map:
            for tile in line:
                if tile.type == TileType.BORDER or tile.type == TileType.DESTRUCTIBLE:
                    if self.hitbox.colliderect(tile.hitbox):
                        print("Collision!")
