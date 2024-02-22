import pygame

from game.creatures.сreature import Creature


class Player(Creature):
    def __init__(self, x: int, y: int, image: pygame.Surface, bomb_count: int):
        super().__init__(x, y, image)
        self.x = x
        self.y = y
        self.speed = 5
        self.image = image
        self.hitbox = pygame.Rect(x, y, image.get_width(), image.get_height())
        self.bomb_count = bomb_count

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def is_collided_with(self, player: Creature):
        if self.hitbox.colliderect(player.hitbox):
            return True

    def check_collision(self, other):
        return self.hitbox.colliderect(other.hitbox)

    # def check_collision_tile(self, tile):
    #     if tile.type == TileType.BORDER:
    #         print("Collision with border")
    #     return self.hitbox.colliderect(tile.hitbox)
