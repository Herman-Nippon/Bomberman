import pygame


class Player:
    def __init__(Creature, x: int, y: int, image: pygame.Surface, bomb_count: int, self=None):
        Creature.x = x
        Creature.y = y
        Creature.speed = 5
        Creature.image = image
        Creature.hitbox = pygame.Rect(x, y, image.get_width(), image.get_height())
        Creature.bomb_count = bomb_count
        Creature.hitbox = pygame.Rect(x, y, image.get_width(), image.get_height())



    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))




