import pygame

from сreature import Creature


class Npc(Creature):
    def __init__(self, x: int, y: int, image: pygame.Surface):
        super().__init__(x, y, image)


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def check_collision(self, other: Creature):
        return self.hitbox.collidepoint(other.x, other.y)

