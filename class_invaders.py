from setting import *
import pygame as pg




class Invaders(pg.sprite.Sprite):
    def __init__(self, x, y):
        super(__class__, self).__init__()
        self.image = IMG_INVADER_GREEN
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.life = 1


    def creat_group(self, rows):
        invaders_list = pg.sprite.Group()
        for i in range(COLS_INVADERS):
            for u in range(rows):
                invader = Invaders(i * 120, u * 100)
                invaders_list.add(invader)
        return invaders_list

    def update(self, x, y):
        self.rect.x += x
        self.rect.y += y
