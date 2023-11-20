import pygame
from setting import *
from class_invaders import Invaders


class Shot_ship(pg.sprite.Sprite):
    def __init__(self, x, y):
        super(__class__, self).__init__()
        self.image = IMG_SHOT
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y -= SPEED_SHOT_SHIP


