from window import Window
import settings

import pygame as pg





class GameOver(Window):
    def __init__(self, score: int = 0, is_game_record: bool = False) -> None:
        self._is_game_record = is_game_record
        self._level = 1
        self._life = 0
        super().__init__(score)
        self._image_path: str = settings.IMG_GAME_OVER
        self._title = "game over"
        self._life = 0
        self._tik = 5


    def _initial_text(self) -> None:
        txt_highlight = [
            settings.FONT,
            f"New game record! {self._score} points" if self._is_game_record else "",
            True,
            (255, 0, 0),
            (0, 0, 255),
            80,
            (settings.SIZE[0] // 2, settings.SIZE[1] // 5),
        ]
        txt_data = [
            settings.FONT,
            "press key-down for play again",
            False,
            settings.RED,
            settings.WHITE,
            40,
            (settings.HEIGHT * 0.7, settings.WIDTH * 0.6),
        ]
        txt_instructions = [
            settings.FONT,
            f"your score is {self._score}",
            False,
            settings.RED,
            settings.WHITE,
            40,
            (settings.HEIGHT * 0.7, settings.WIDTH * 0.55),
        ]
        self._text = [txt_highlight ,txt_data, txt_instructions]
    


        



if __name__ == '__main__':
    p = GameOver(5000, 0)
    from screen import Screen
    s = Screen("", settings.IMG_GAME_OVER)
    p.run(s)