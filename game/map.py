import pygame
from random import randint

GRASS, BORDER, DESTRUCTIBLE = 0, 1, 2


class Map:
    def __init__(self, screen: pygame.Surface):
        self.grass_tile = pygame.image.load("../assets/Map/grass.png").convert()
        self.border_tile = pygame.image.load("../assets/Map/border_final.png").convert()
        self.destructible_block = pygame.image.load("../assets/Map/destructible.png").convert()

        self.grass_tile = pygame.transform.scale(self.grass_tile, (48, 48))
        self.border_tile = pygame.transform.scale(self.border_tile, (48, 48))
        self.destructible_block = pygame.transform.scale(self.destructible_block, (48, 48))

        self.screen = screen

        self.map_width = 21
        self.map_height = 15
        self.tile_size = self.grass_tile.get_width()

        self.tiles_map = [[] for _ in range(self.map_width)]
        self.destructible_blocks_map = []

        # Calculate horizontal and vertical offsets to center the map
        map_width_pixels = self.map_width * self.tile_size
        map_height_pixels = self.map_height * self.tile_size

        self.horizontal_offset = (self.screen.get_width() - map_width_pixels) // 2
        self.vertical_offset = (self.screen.get_height() - map_height_pixels) // 2

    def create_map(self):
        for x in range(self.map_width):
            for y in range(self.map_height):
                if (x == 0
                        or x == self.map_width - 1
                        or y == 0
                        or y == self.map_height - 1
                        or (not x % 2 and not y % 2)):
                    self.tiles_map[x].append((BORDER, x, y))
                else:
                    if (y == 1 and x == 1
                            or y == 1 and x == 2
                            or y == 2 and x == 1):
                        self.tiles_map[x].append((GRASS, x, y))
                    elif (y == self.map_height - 2 and x == self.map_width - 3
                          or y == self.map_height - 2 and x == self.map_width - 2
                          or y == self.map_height - 3 and x == self.map_width - 2):
                        self.tiles_map[x].append((GRASS, x, y))
                    else:
                        if randint(0, 1):
                            self.tiles_map[x].append((GRASS, x, y))
                        else:
                            self.tiles_map[x].append((DESTRUCTIBLE, x, y))

    def draw(self):
        for line in self.tiles_map:
            for tile in line:
                x_position = tile[1] * self.tile_size + self.horizontal_offset
                y_position = tile[2] * self.tile_size + self.vertical_offset

                match tile[0]:
                    case 0:
                        self.screen.blit(self.grass_tile, (x_position, y_position))
                    case 1:
                        self.screen.blit(self.border_tile, (x_position, y_position))
                    case 2:
                        self.screen.blit(self.destructible_block, (x_position, y_position))
