import settings
from screen import Screen

import pygame as pg

class Window:
    def __init__(self, name: str, image_path: str, score: int = 0) -> None:
        self._screen = Screen(name, image_path)
        self._score = score
        self._running = True
        self._continue = True
        self._clock = pg.time.Clock()
        self._initial_text()
        # for initial in subclass
        self._text: list[list]
        self._tik: int
        self._level: int
        self._life: int

    def _initial_text(self):
        raise NotImplementedError

    def _text_to_screen(self):
        for font, text, antialias, color, background, size, local, from_level in self._text:
            if self._level >= from_level:
                self._screen.blit_text(
                    font,
                    text,
                    antialias,
                    color,
                    background,
                    size,
                    local
                )
    
    def _handle_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self._running = False
                self._continue = False
            if event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
                self._running = False
    
    def _loop_game(self) -> False:
        while self._running:
            self._handle_event()
            self._screen.blit()
            self._text_to_screen()
            pg.display.flip()
            self._clock.tick(self._tik)
    
    def run(self) -> bool:
        self._loop_game()
        return self._continue, self._life, self._level, self._score


    







