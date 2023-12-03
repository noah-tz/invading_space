from pre_game import PreGame
from level_game import LevelGame
from game_over import GameOver
from screen import Screen
import settings
import pygame as pg

class GameManager:
    def __init__(self, level_start = 1) -> None:
        self._level_start = level_start -1
        self.screen = Screen(f"level {self._level_start}", settings.IMG_GAME)

    def background_music(self):
        pg.mixer.init()
        explosion_sound = pg.mixer.Sound(settings.SOUND_GAME)
        pg.mixer.Sound.play(explosion_sound)

    def run(self):
        self.background_music()
        level = self._level_start
        life = settings.LIFE
        score = 0
        continue_ = True
        while continue_:
            level += 1
            pre_game = PreGame(level, score, life)
            _, quit, life, level, score = pre_game.run(self.screen)
            if quit:
                return
            level_game = LevelGame(level, life, score)
            continue_, quit, life, level, score = level_game.run(self.screen)
            if quit:
                return
        self._game_over(score)
        
    def _game_over(self, score):
        game_over = GameOver(score)
        quit = game_over.run(self.screen)[1]
        if not quit:
            self.run()


if __name__ == '__main__':
    game = GameManager()
    game.run()