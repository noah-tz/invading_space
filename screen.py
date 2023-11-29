import pygame as pg
from typing import Type

from object_game import Object
import settings


class Screen:
    def __init__(self, name: str, image_path: str) -> None:
        self._screen = pg.display.set_mode(settings.SIZE)
        self._name = name
        self._image = pg.image.load(image_path)


    def blit(self, groups: tuple[pg.sprite.Group] = (), objects: tuple[Type[Object]] = ()):
        self._screen.blit(self._image, (0, 0))
        for group in groups:
            group.draw(self._screen)
        for object in objects:
            self._screen.blit(object.image, object.rect.topleft)
        pg.display.flip()
        

    def blit_text(self, font, txt, antialias: bool, color, background, size, vec):
        font = pg.font.Font(font, size)
        text = font.render(txt, antialias, color, background)
        textRect = text.get_rect()
        textRect.center = vec
        self._screen.blit(text, textRect)


