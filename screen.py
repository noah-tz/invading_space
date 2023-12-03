from object_game import Object
import settings

import pygame as pg
from typing import Type



class Screen:
    def __init__(self, name: str, image_path: str) -> None:
        self._screen = pg.display.set_mode(settings.SIZE)
        pg.display.set_caption(name)
        self._image = pg.image.load(image_path)
        pg.font.init()


    def blit(self, groups: tuple[pg.sprite.Group] = (), objects: tuple[Type[Object]] = (), blit_image: bool = True):
        if blit_image:
            self._screen.blit(self._image, (0, 0))
        for group in groups:
            group.draw(self._screen)
        for object in objects:
            self._screen.blit(object.image, object.rect.topleft)


    def blit_text(self, font, txt, antialias: bool, color, background, size, vec):
        font = pg.font.Font(font, size)
        text = font.render(txt, antialias, color, background)
        textRect = text.get_rect()
        textRect.center = vec
        self._screen.blit(text, textRect)

    def replace_window(self, image_path, name):
        self._image = pg.image.load(image_path)
        pg.display.set_caption(name)

