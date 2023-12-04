from pre_game import PreGame
from level_game import LevelGame
from game_over import GameOver
from screen import Screen
import settings
import pygame as pg
import os

class GameManager:
    def __init__(self, level_start: int = 1) -> None:
        self._level_start = level_start -1
        self._screen = Screen(f"level {self._level_start}", settings.IMG_GAME)

    def _background_music(self) -> None:
        pg.mixer.init()
        explosion_sound = pg.mixer.Sound(settings.SOUND_GAME)
        pg.mixer.Sound.play(explosion_sound)

    def run(self) -> None:
        self._background_music()
        level = self._level_start
        life = settings.LIFE -1
        score = 0
        continue_ = True
        while continue_:
            level += 1
            life += 1
            pre_game = PreGame(level, score, life)
            _, quit, life, level, score = pre_game.run(self._screen)
            if quit:
                return
            level_game = LevelGame(level, life, score)
            continue_, quit, life, level, score = level_game.run(self._screen)
            if quit:
                return
        self._game_over(score)
        
    def _game_over(self, score: int) -> None:
        game_over = GameOver(score, self._is_game_record(score))
        quit = game_over.run(self._screen)[1]
        if not quit:
            self.run()

    def _is_game_record(self, score: int) -> bool:
        game_record = False
        if not os.path.exists(settings.GAME_RECORD_PATH):
            with open(settings.GAME_RECORD_PATH, 'w') as file:
                file.write('0')
        with open(settings.GAME_RECORD_PATH, 'r+') as file:
            current_game_record = int(file.read())
            if score > current_game_record:
                game_record = True
                file.seek(0)
                file.truncate(0)
                file.write(str(score))
        return game_record            



if __name__ == '__main__':
    game = GameManager(8)
    game.run()