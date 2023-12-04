from object_game import Object
import settings
import pygame as pg
from typing import Type

class Screen:
    def __init__(self, name: str, image_path: str) -> None:
        """
        Initialize the game screen.

        Parameters:
        - name (str): The name or title of the game screen.
        - image_path (str): The file path to the background image of the screen.
        """
        self._screen = pg.display.set_mode(settings.SIZE)
        pg.display.set_caption(name)
        self._image = pg.image.load(image_path)
        pg.font.init()

    def blit(self, groups: tuple[pg.sprite.Group] = (), objects: tuple[Type[Object]] = (), blit_image: bool = True) -> None:
        """
        Render and display objects on the game screen.

        Parameters:
        - groups (tuple[pg.sprite.Group]): Tuple of sprite groups to be rendered on the screen.
        - objects (tuple[Type[Object]]): Tuple of Object instances to be rendered on the screen.
        - blit_image (bool): Flag indicating whether to render the background image.

        Note: The order of rendering is background image, sprite groups, and objects.
        """
        if blit_image:
            self._screen.blit(self._image, (0, 0))
        for group in groups:
            group.draw(self._screen)
        for obj in objects:
            self._screen.blit(obj.image, obj.rect.topleft)

    def blit_text(self, font: str, txt: str, antialias: bool, color: tuple[int], background: tuple[int], size: int, vec: tuple[float]) -> None:
        """
        Render and display text on the game screen.

        Parameters:
        - font (str): The file path to the font.
        - txt (str): The text to be rendered.
        - antialias (bool): Flag indicating whether to use antialiasing for the text.
        - color (tuple[int]): The color of the text.
        - background (tuple[int]): The background color of the text.
        - size (int): The font size.
        - vec (tuple[float]): The position of the text as a tuple of (x, y) coordinates.
        """
        font = pg.font.Font(font, size)
        text = font.render(txt, antialias, color, background)
        text_rect = text.get_rect()
        text_rect.center = vec
        self._screen.blit(text, text_rect)

    def replace_window(self, image_path: str, name: str) -> None:
        """
        Replace the background image and update the window caption.

        Parameters:
        - image_path (str): The file path to the new background image.
        - name (str): The new name or title of the game screen.
        """
        self._image = pg.image.load(image_path)
        pg.display.set_caption(name)
