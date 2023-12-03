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

class Ship(Object):
    def __init__(self, x, y):
        super().__init__(x, y, settings.IMG_SHIP)

    def update(self, x):
            self.rect.x += x

class Invader(Object):
    direction = 1
    def __init__(self, x, y):
        super().__init__(x, y, settings.IMG_INVADER_GREEN)
        self.life = 1

    def is_over_left(self):
        return (self.rect.x <= 0) and (Invader.direction == -1)
    
    def is_over_right(self):
        return (self.rect.x >= (settings.HEIGHT * 1.28)) and (Invader.direction == 1)

    def add_y(self, level):
        self.rect.y += level * 0.1 + settings.SPEED_DOWN_INVADERS

    def update(self):
        self.rect.x += settings.SPEED_MOVE_INVADERS * Invader.direction

    def collision(self):
        self.image = pg.image.load(settings.IMG_INVADER_RED)
        self.life -= 1
        return self.life +1


class ShotInvader(Object):
    def __init__(self, x, y):
        super().__init__(x, y, settings.IMG_SHOT)
        self.speed = random.randint(3, 5)

    def update(self, level):
        self.rect.y += self.speed * (1 + (level * 0.05))


class ShotShip(ShotInvader):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._sound()

    def _sound(self):
        pg.mixer.init()
        pg.mixer.music.load(settings.SOUND_SHOT)
        pg.mixer.music.play()

    def update(self):
        self.rect.y -= settings.SPEED_SHOT_SHIP


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
        self._life = 1

    def collision(self):
        self.image.fill(settings.RED)
        self._life -= 1
        return self._life +1
    










