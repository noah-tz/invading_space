import pygame as pg
import settings

class Protector(pg.sprite.Sprite):
    def __init__(self, x):
        super(__class__, self).__init__()
        self.image = pg.Surface((200, 5))
        self.image.fill(settings.GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = settings.HEIGHT * 0.75
        self.life = 1

    def creat_group(self, level):
        protectors_list = pg.sprite.Group()
        protector = Protector(10)
        protectors_list.add(protector)
        for i in range(1, 4 - (level // 2) + 1):
            protector = Protector(((settings.WIDTH - 205) / (4 - (level // 2))) * i)
            protectors_list.add(protector)
        return protectors_list



    def life_protector(self):
        self.life -= 1
