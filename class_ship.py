import settings
import pygame as pg


class Ship(pg.sprite.Sprite):
    def __init__(self, x, y):
        super(__class__, self).__init__()
        self.image = settings.IMG_SHIP
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move_ship(self, x):
            self.rect.x += x

    def move_shot_ship(self):
        self.shot.rect.y += 15


    def los(self):
        if self.life > 0:
            self.life -= 1



