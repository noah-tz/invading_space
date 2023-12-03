from window import Window
import settings

import pygame as pg





class PreGame(Window):
    def __init__(self, level: int, score = 0, life: int = 3) -> None:
        self._level = level
        self._life = life
        super().__init__(f"level {self._level}", settings.IMG_GAME, score)
        self._tik = 5

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
    


        



if __name__ == '__main__':
    p = PreGame(2)
    p.run()