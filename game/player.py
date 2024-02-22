import pygame

from сreature import Creature


class Player(Creature):
    def __init__(self, x: int, y: int, image: pygame.Surface, bomb_count: int):
        super().__init__(x,y,image)
        self.x=x
        self.y=y
        self.speed = 1
        self.image = image
        self.hitbox = pygame.Rect(x, y, image.get_width(), image.get_height())
        self.bomb_count = bomb_count
        self.hitbox = pygame.Rect(x, y, image.get_width(), image.get_height())



    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def check_collision(self, other):
        return self.hitbox.colliderect(other.hitbox)

    def check_collision_tile(self, tile):
        return self.hitbox.colliderect(tile.hitbox)




