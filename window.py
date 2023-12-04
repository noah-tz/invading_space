from screen import Screen
from typing import Type

import pygame as pg

class Window:
    def __init__(self, score: int = 0) -> None:
        self._score = score
        self._running = True
        self._continue = True
        self._quit = False
        self._clock = pg.time.Clock()
        self._initial_text()
        # for initial in subclass
        self._text: list[list]
        self._tik: int
        self._level: int
        self._life: int
        self._image_path: str
        self._title: str

    def _initial_text(self) -> None:
        raise NotImplementedError

    def _text_to_screen(self, screen: Type[Screen]) -> None:
        for font, text, antialias, color, background, size, local in self._text:
            screen.blit_text(
                font,
                text,
                antialias,
                color,
                background,
                size,
                local
            )
    
    def _handle_event(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self._running = False
                self._quit = True
            if event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
                self._running = False
    
    def _loop_game(self, screen: Type[Screen]) -> None:
        while self._running:
            self._handle_event()
            screen.blit()
            self._text_to_screen(screen)
            pg.display.flip()
            self._clock.tick(self._tik)
    
    def run(self, screen: Type[Screen]) -> tuple[bool, bool, int, int, int]:
        screen.replace_window(self._image_path, self._title)
        self._loop_game(screen)
        return self._continue, self._quit, self._life, self._level, self._score


    







