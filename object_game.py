import pygame as pg
import settings
import random

class Object(pg.sprite.Sprite):
    def __init__(self, x: float, y: float, image_path: str = None) -> None:
        """
        Initialize a generic game object.
        Parameters:
        - x (float): The x-coordinate of the object.
        - y (float): The y-coordinate of the object.
        - image_path (str): The file path to the object's image (default is None).
        """
        super(__class__, self).__init__()
        self.image = pg.image.load(image_path) if image_path else pg.Surface((200, 5))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Ship(Object):
    def __init__(self, x: float) -> None:
        """
        Initialize the player's spaceship.
        Parameters:
        - x (float): The initial x-coordinate of the spaceship.
        """
        super().__init__(x, settings.LOCATION_Y_SHIP, settings.IMG_SHIP)

    def update(self, x: float) -> None:
        """
        Update the position of the spaceship.
        Parameters:
        - x (float): The amount to move the spaceship on the x-axis.
        """
        self.rect.x += x

class Invader(Object):
    direction = 1
    def __init__(self, x: float, y: float) -> None:
        """
        Initialize an invader object.
        Parameters:
        - x (float): The initial x-coordinate of the invader.
        - y (float): The initial y-coordinate of the invader.
        """
        super().__init__(x, y, settings.IMG_INVADER_GREEN)
        self.life = 1

    def is_over_left(self) -> bool:
        """
        Check if the invader is over the left boundary.
        Returns:
        - bool: True if the invader is over the left boundary, False otherwise.
        """
        return (self.rect.x <= 0) and (Invader.direction == -1)
    
    def is_over_right(self) -> bool:
        """
        Check if the invader is over the right boundary.
        Returns:
        - bool: True if the invader is over the right boundary, False otherwise.
        """
        return (self.rect.x >= (settings.HEIGHT * 1.28)) and (Invader.direction == 1)

    def add_y(self, level: int) -> None:
        """
        Move the invader down.
        Parameters:
        - level (int): The current level of the game.
        """
        self.rect.y += min(settings.MAX_LEVEL_ADD, level) * 0.1 + settings.SPEED_DOWN_INVADERS

    def update(self) -> None:
        """
        Update the position of the invader.
        """
        self.rect.x += settings.SPEED_MOVE_INVADERS * Invader.direction

    def collision(self) -> int:
        """
        Handle collision with the invader.
        Returns:
        - int: The remaining life of the invader.
        """
        self.image = pg.image.load(settings.IMG_INVADER_RED)
        self.life -= 1
        return self.life + 1

class ShotInvader(Object):
    def __init__(self, x: float, y: float) -> None:
        """
        Initialize an invader's shot.
        Parameters:
        - x (float): The initial x-coordinate of the shot.
        - y (float): The initial y-coordinate of the shot.
        """
        super().__init__(x, y, settings.IMG_SHOT)
        self.speed = random.randint(3, 5)

    def update(self, level: int) -> None:
        """
        Update the position of the invader's shot.
        Parameters:
        - level (int): The current level of the game.
        """
        self.rect.y += self.speed * (1 + min(settings.MAX_LEVEL_ADD, level) * 0.05)

class ShotShip(ShotInvader):
    def __init__(self, x: float) -> None:
        """
        Initialize the player's shot.
        Parameters:
        - x (float): The initial x-coordinate of the shot.
        """
        super().__init__(x, settings.LOCATION_Y_SHIP)
        self._sound()

    def _sound(self) -> None:
        """
        Play the shot sound.
        """
        pg.mixer.init()
        pg.mixer.music.load(settings.SOUND_SHOT)
        pg.mixer.music.play()

    def update(self) -> None:
        """
        Update the position of the player's shot.
        """
        self.rect.y -= settings.SPEED_SHOT_SHIP

class Joker(Object):
    def __init__(self, level: int) -> None:
        """
        Initialize a special joker invader.
        Parameters:
        - level (int): The current level of the game.
        """
        super().__init__(settings.WIDTH, settings.HEIGHT * 0.1, settings.IMG_JOKER)
        self.speed = random.randint(2, level + 3)
        self.level = level

    def update(self) -> None:
        """
        Update the position of the joker invader.
        """
        self.rect.x -= self.speed + min(settings.MAX_LEVEL_ADD, self.level) * 0.3

class Protector(Object):
    def __init__(self, x: int) -> None:
        """
        Initialize a protector object.
        Parameters:
        - x (int): The initial x-coordinate of the protector.
        """
        super().__init__(x, settings.HEIGHT * 0.75)
        self.image.fill(settings.GREEN)
        self._life = 1

    def collision(self) -> int:
        """
        Handle collision with the protector.
        Returns:
        - int: The remaining life of the protector.
        """
        self.image.fill(settings.RED)
        self._life -= 1
        return self._life + 1
