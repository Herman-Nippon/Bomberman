import pygame

from сreature import Creature


class Bomb(Creature):

    def __init__(self, x: int, y: int, image: pygame.Surface):
        super().__init__(x, y, image)
        self.timer = 3;  # 3 seconds todo: add timer

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def blow_up(self):
        pass
