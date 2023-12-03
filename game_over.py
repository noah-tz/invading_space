from window import Window
import settings

import pygame as pg





class GameOver(Window):
    def __init__(self, score = 0, level: int =0, life: int = 0) -> None:
        self._level = 1
        self.life = 0
        super().__init__(score)
        self._image_path = settings.IMG_GAME_OVER
        self._title = "game over"
        self._life = 0
        self._tik = 5


    def _initial_text(self):
        txt_data = [
            settings.FONT,
            "press key-down for play again",
            False,
            settings.RED,
            settings.WHITE,
            40,
            (settings.HEIGHT * 0.7, settings.WIDTH * 0.1),
        ]
        txt_instructions = [
            settings.FONT,
            f"your score is {self._score}",
            False,
            settings.RED,
            settings.WHITE,
            40,
            (settings.HEIGHT * 0.7, settings.WIDTH * 0.6),
        ]
        self._text = [txt_data, txt_instructions]
    


        



if __name__ == '__main__':
    p = GameOver()
    p.run()