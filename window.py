import settings
from screen import Screen

import pygame as pg

class Window:
    def __init__(self, name: str, image_path: str) -> None:
        self._screen = Screen(name, image_path)
        self._running = True
        self._clock = pg.time.Clock()

    def _background_music(self):
        pg.mixer.init()
        explosion_sound = pg.mixer.Sound(settings.SOUND_GAME)
        pg.mixer.Sound.play(explosion_sound)

    def _text_to_screen(self):
        raise NotImplementedError
    
    def _handle_event(self):
        raise NotImplementedError
    
    def _loop_game(self):
        raise NotImplementedError
    
    def run(self):
        raise NotImplementedError


    
class PreGame(Window):
    def __init__(self, level: int, score = 0, life: int = 3) -> None:
        super().__init__(f"Introduction to level {level}", settings.IMG_GAME)
        self._level = level
        self._score = score
        self._life = life
        self._continue_level = True
        self._initial_text()

    def _handle_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self._running = False
                self._continue_level = False
            if event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
                self._running = False

    def _initial_text(self):
        txt_win = [
            settings.FONT,
            "You Win",
            True,
            (255, 0, 0),
            (0, 0, 255),
            200,
            (settings.SIZE[0] // 2, settings.SIZE[1] // 2),
            2
        ]
        txt_data = [
            settings.FONT,
            f"your score is {self._score}, your life is {self._life}. level: {self._level }",
            False,
            settings.RED,
            settings.WHITE,
            25,
            (settings.HEIGHT * settings.LOCATION_TEXT_GAME_X, settings.WIDTH * settings.LOCATION_TEXT_GAME_Y),
            1
        ]
        window_mode = "start" if self._level == 1 else "continue"
        txt_instructions = [
            settings.FONT,
            f"Press down key for {window_mode} play",
            False,
            settings.RED,
            settings.WHITE,
            37,
            (settings.HEIGHT * settings.LOCATION_TEXT_GAME_X +80, settings.WIDTH * settings.LOCATION_TEXT_GAME_Y -50),
            1
        ]
        self._text = [txt_win, txt_data, txt_instructions]


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
    
    def _loop_game(self) -> False:
        while self._running:
            self._handle_event()
            self._screen.blit()
            self._text_to_screen()
            pg.display.flip()
            self._clock.tick(5)

    def run(self) -> bool:
        self._background_music()
        self._loop_game()
        return self._continue_level
    


        



if __name__ == '__main__':
    p = PreGame(2)
    p.run()






