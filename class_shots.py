import pygame as pg
import settings
from class_invaders import Invaders


class Shot_ship(pg.sprite.Sprite):
    def __init__(self, x, y):
        super(__class__, self).__init__()
        self.image = settings.IMG_SHOT
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y -= settings.SPEED_SHOT_SHIP


