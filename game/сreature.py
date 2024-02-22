
import pygame

class Creature:
    def __init__(self, x: int, y: int, image: pygame.Surface):
        self.x = x
        self.y = y
        self.speed = 5
        self.image = image
        self.hitbox = pygame.Rect(x, y, image.get_width(), image.get_height())

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))