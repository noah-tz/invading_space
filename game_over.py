from window import Window
import settings

import pygame as pg





class GameOver(Window):
    def __init__(self, level: int, score = 0, life: int = 3) -> None:
        self._level = 1
        self.life = 0
        super().__init__("game over", settings.IMG_GAME_OVER, score)
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
            0
        ]
        txt_instructions = [
            settings.FONT,
            f"your score is {self._score}",
            False,
            settings.RED,
            settings.WHITE,
            40,
            (settings.HEIGHT * 0.7, settings.WIDTH * 0.6),
            0
        ]
        self._text = [txt_data, txt_instructions]
    


        



if __name__ == '__main__':
    p = GameOver()
    p.run()