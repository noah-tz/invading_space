import pygame as pg
import random
import settings


class Jokers(pg.sprite.Sprite):
    def __init__(self, level):
        super(__class__, self).__init__()
        self.speed = random.randint(2, level + 3)
        self.image = settings.IMG_JOKER
        self.rect = self.image.get_rect()
        self.rect.x = settings.WIDTH
        self.rect.y = settings.HEIGHT * 0.1

    def update(self, level):
        self.rect.x -= self.speed + (level * 0.5)
