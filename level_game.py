from window import Window
import settings
from screen import Screen

from object_game_copy import(
    Ship,
    Invader,
    ShotShip,
    ShotInvader,
    Joker,
    Protector
)
import pygame as pg
import random
from typing import Type





class LevelGame(Window):
    def __init__(self, level: int, life: int, score: int = 0) -> None:
        self._level = level
        self._life = life
        super().__init__(score)
        self._image_path = settings.IMG_GAME
        self._title = f"level {self._level}"
        self._tik = settings.REFRESH_RATE
        self._initial_objects()

    def _initial_text(self):
        txt_data = [
            settings.FONT,
            "",
            False,
            settings.RED,
            settings.WHITE,
            25,
            (settings.HEIGHT * settings.LOCATION_TEXT_GAME_X, settings.WIDTH * settings.LOCATION_TEXT_GAME_Y),
        ]
        self._text = [txt_data]

    def _initial_objects(self):
            self._protectors = pg.sprite.Group(Protector(((settings.WIDTH - 205) / (4 - (self._level // 2))) * protector) for protector in range(4 - (self._level // 2) + 1)) # Protector.creat_group(self, self._level)
            self._invaders = pg.sprite.Group(Invader(col * 120, row * 100) for row in range(self._level) for col in range(settings.COLS_INVADERS))
            self._shots_ship = pg.sprite.Group()
            self._shots_invaders = pg.sprite.Group()
            self._jokers = pg.sprite.Group()
            self._ship = Ship((settings.WIDTH - 100) // 2, int(settings.HEIGHT * 0.8))

    def _handle_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self._running = False
                self._quit = True
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                self._shots_ship.add(ShotShip(self._ship.rect.x + (settings.WIDTH_SHIP / 2) - (settings.WIDTH_SHOT / 2), self._ship.rect.y))
                self._score = max(self._score -1 ,0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self._ship.rect.x > 10:
            self._ship.update(- settings.SPEED_MOVE_SHIP)
        elif keys[pg.K_RIGHT] and self._ship.rect.x < (settings.WIDTH - 57):
            self._ship.update(settings.SPEED_MOVE_SHIP)

    def _dynamic_text(self):
        self._text[0][1] = f"your score is {self._score}, your life is {self._life}. level: {self._level }"

    def _move_invaders(self):
        if len(self._invaders) > 0:
            add_y = False
            for invader in self._invaders.sprites():
                if invader.is_over_left():
                    add_y = True
                    Invader.direction = 1
                elif invader.is_over_right():
                    add_y = True
                    Invader.direction = -1
            if add_y:
                for invader in self._invaders.sprites():
                    invader.add_y(self._level)							
            self._invaders.update()

    def _move_objects(self):
        self._shots_ship.update()
        self._shots_invaders.update(self._level)
        self._jokers.update()
        self._move_invaders()

    def _create_random_objects(self):
        shot = random.randint(0, settings.PULSE_SHOTS_INVADERS + int(self._level * 0.1 + 1))
        create_joker = random.randint(0, settings.PULSE_CREATE_JOKER)
        if shot == settings.PULSE_SHOTS_INVADERS and len(self._invaders.sprites()):
            invader_shot = random.choice(self._invaders.sprites())
            self._shots_invaders.add(ShotInvader(invader_shot.rect.x + (settings.WIDTH_INVADER / 2) - (settings.WIDTH_SHOT / 2), invader_shot.rect.y + (settings.HEIGHT_INVADER)))
        if create_joker == settings.PULSE_CREATE_JOKER:
            self._jokers.add(Joker(self._level))

    def _blit_objects(self, screen: Type[Screen]):
        screen.blit(
            (
                self._jokers,
                self._shots_invaders,
                self._protectors,
                self._shots_ship,
                self._invaders,
            )
        )
        self._text_to_screen(screen)
        screen.blit(objects=(self._ship,), blit_image=False)

    def _collide(self):
        if pg.sprite.spritecollide(self._ship, self._shots_invaders, True):
            if self._life > 0:
                self._life -= 1
                self._score = (max(self._score -100, 0))
            else:
                self._running = False
                self._continue = False
        if pg.sprite.spritecollide(self._ship, self._invaders, False):
            self._running = False
            self._continue = False
        pg.sprite.groupcollide(self._shots_ship, self._shots_invaders, True, True)
        pg.sprite.groupcollide(self._shots_ship, self._jokers, True, True)
        for invader in self._invaders.sprites():
            if pg.sprite.spritecollide(invader, self._shots_ship, True):
                if not invader.collision():
                    self._invaders.remove(invader)
                self._score += 100
        for protector in self._protectors.sprites():
            if pg.sprite.spritecollide(protector, self._shots_invaders, True) and not protector.collision():
                self._protectors.remove(protector)

    def _loop_game(self, screen: Type[Screen]) -> False:
        while self._running and len(self._invaders):
            self._dynamic_text()
            self._handle_event()
            screen.blit()
            self._dynamic_text()
            self._blit_objects(screen)
            pg.display.flip()
            self._clock.tick(self._tik)
            self._move_objects()
            self._create_random_objects()
            self._collide()





    




if __name__ == '__main__':
    p = LevelGame(3, 3, 0)
    p.run()