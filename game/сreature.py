import pygame


class Creature:
    def __init__(self, x: int, y: int, image: pygame.Surface):
        self.x = x
        self.y = y
        self.speed = 5
        self.image = image
        self.rect = self.image.get_rect()
        self.life = 3
        self.hitbox = pygame.Rect(x, y, image.get_width(), image.get_height())

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))

    def damage(self, damage: int):
        self.life -= damage
