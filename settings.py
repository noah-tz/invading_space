import pygame as pg

LIFE = 3

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MEDIUM_GRAY = (128, 128, 128)
AQUA = (0, 128, 128)
NAVY_BLUE = (0,	0, 128)
GREEN = (0, 255, 0)
ORANGE = (255, 165,	0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

START_TEXT_SIZE = 16

REFRESH_RATE = 60



SOUND_GAME = 'media/music.wav'
SOUND_SHOT = 'media/sound_shot_1.wav' # sound_shot_1.wav

SCORE_INVADER = 100
SCORE_SHOT = 1000
SCORE_JOKER = 400
SCORE_SHOT_SHIP = 1

IMG_SHIP = pg.image.load('media/ship.bmp')
IMG_INVADER_GREEN = pg.image.load('media/elian_green.png')
IMG_INVADER_RED = pg.image.load('media/elian_red.png')
IMG_SHOT = pg.image.load('media/shot.jpeg')
IMG_JOKER = pg.image.load('media/joker.PNG')
IMG_LIFE = pg.image.load('media/ship.bmp')

SPEED_MOVE_SHIP = 7
SPEED_MOVE_INVADERS = 5
SPEED_DOWN_INVADERS = 15
SPEED_SHOT_SHIP = 20
PULSE_SHOTS_INVADERS = 70
PULSE_CREATE_JOKER = 300

WIDTH_SHIP, HEIGHT_SHIP = 57, 99
WIDTH_INVADER, HEIGHT_INVADER = 113, 57
WIDTH_SHOT, HEIGHT_SHOT = 5, 26

mef = True
if mef:
    WIDTH, HEIGHT = 1600, 1158
    #WIDTH_PROTECTOR =
    IMG_GAME = pg.image.load('media/img_game_mef.jpg')
    IMG_GAME_OVER = pg.image.load('media/img_over_mef.jpg')
    IMG_YOU_WINNER = pg.image.load('media/img_win_mef.png')
    ROWS_INVADERS = 4
    COLS_INVADERS = 10
    LOCATION_TEXT_GAME_Y = 0.6
    LOCATION_TEXT_GAME_X = 0.2
else:
    WIDTH, HEIGHT = 960, 660
    IMG_GAME = pg.image.load('media/img_game_home.jpeg')
    IMG_GAME_OVER = pg.image.load('media/img_over_home.jpg')
    IMG_YOU_WINNER = pg.image.load('media/img_win_home.png')
    ROWS_INVADERS = 3
    COLS_INVADERS = 6
    LOCATION_TEXT_GAME_Y = 0.65
    LOCATION_TEXT_GAME_X = 0.3

SIZE = (WIDTH, HEIGHT)
