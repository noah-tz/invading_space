from class_shots import Shot_ship
import random


class Shot_invaders(Shot_ship):
    def __init__(self, x, y):
        Shot_ship.__init__(self, x, y)
        self.speed = random.randint(3, 5)

    def update(self, level):
        self.rect.y += self.speed * (1 + (level * 0.05))

