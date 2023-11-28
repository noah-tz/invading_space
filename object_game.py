import pygame as pg
import settings
import random

class Object(pg.sprite.Sprite):
    def __init__(self, x, y, image_path = None) -> None:
        super(__class__, self).__init__()
        self.image = pg.image.load(image_path) if image_path else pg.Surface((200, 5))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self) -> None:
        raise NotImplementedError


class Ship(Object):
    def __init__(self, x, y):
        super().__init__(x, y, settings.IMG_SHIP)

    def update(self, x):
            self.rect.x += x

class Invader(Object):
    def __init__(self, x, y):
        super().__init__(x, y, settings.IMG_INVADER_GREEN)
        self.life = 1

    def creat_group(self, rows):
        invaders_list = pg.sprite.Group()
        for i in range(settings.COLS_INVADERS):
            for u in range(rows):
                invader = Invader(i * 120, u * 100)
                invaders_list.add(invader)
        return invaders_list

    def update(self, x, y):
        self.rect.x += x
        self.rect.y += y


class ShotShip(Object):
    def __init__(self, x, y):
        super().__init__(x, y, settings.IMG_SHOT)

    def shot_sound(self):
        pg.mixer.init()
        pg.mixer.music.load(settings.SOUND_SHOT)
        pg.mixer.music.play()

    def update(self):
        self.rect.y -= settings.SPEED_SHOT_SHIP


class ShotInvader(Object):
    def __init__(self, x, y):
        super().__init__(x, y, settings.IMG_SHOT)
        self.speed = random.randint(3, 5)

    def update(self, level):
        self.rect.y += self.speed * (1 + (level * 0.05))


class Joker(Object):
    def __init__(self, level):
        super().__init__(settings.WIDTH, settings.HEIGHT * 0.1, settings.IMG_JOKER)
        self.speed = random.randint(2, level + 3)
        self.level = level

    def update(self):
        self.rect.x -= self.speed + (self.level * 0.3)


class Protector(Object):
    def __init__(self, x):
        super().__init__(x, settings.HEIGHT * 0.75)
        self.image.fill(settings.GREEN)
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









