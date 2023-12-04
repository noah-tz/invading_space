from screen import Screen
from typing import Type
import pygame as pg

class Window:
    def __init__(self, score: int = 0) -> None:
        """
        Initialize a generic window for game windows.

        Parameters:
        - score (int): The initial score for the window (default is 0).
        """
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
        """
        Define initial text elements for the window.
        """
        raise NotImplementedError

    def _text_to_screen(self, screen: Type[Screen]) -> None:
        """
        Render and display text elements on the screen.

        Parameters:
        - screen (Type[Screen]): The screen object to render text on.
        """
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
        """
        Handle events such as quitting or continuing the game.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self._running = False
                self._quit = True
            if event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
                self._running = False
    
    def _loop_game(self, screen: Type[Screen]) -> None:
        """
        Main game loop for the window.

        Parameters:
        - screen (Type[Screen]): The screen object to display the window on.
        """
        while self._running:
            self._handle_event()
            screen.blit()
            self._text_to_screen(screen)
            pg.display.flip()
            self._clock.tick(self._tik)
    
    def run(self, screen: Type[Screen]) -> tuple[bool, bool, int, int, int]:
        """
        Run the window and return relevant game information.

        Parameters:
        - screen (Type[Screen]): The screen object to display the window on.

        Returns:
        - tuple[bool, bool, int, int, int]: 
          - The first value indicates whether the game should continue.
          - The second value indicates whether the player has chosen to quit.
          - The third value is the remaining life.
          - The fourth value is the current level.
          - The fifth value is the current score.
        """
        screen.replace_window(self._image_path, self._title)
        self._loop_game(screen)
        return self._continue, self._quit, self._life, self._level, self._score
