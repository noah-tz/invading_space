import settings
from object_game_copy import (
	Ship,
	Invader,
	ShotShip,
	ShotInvader,
	Joker,
	Protector
)

import random
import pygame as pg

class GameManager:
	def __init__(self, level, life, score):
		pg.init()
		self._level: int = level
		self._image: str = pg.image.load(settings.IMG_GAME)
		self._name: str = 'invaders space'
		self._screen = pg.display.set_mode(settings.SIZE)
		self._running = True
		self._clock = pg.time.Clock()
		self._revers = False
		self._life = life
		self._score = score
		self._stay = True
		self._image_game_over = pg.image.load(settings.IMG_GAME_OVER)
		self._image_you_winner = pg.image.load(settings.IMG_YOU_WINNER)
		self._ship = Ship((settings.WIDTH - 100) // 2, int(settings.HEIGHT * 0.8))

	def background_music(self):
		explosion_sound = pg.mixer.Sound(settings.SOUND_GAME)
		pg.mixer.Sound.play(explosion_sound)


	def text(self, size, vec, txt):
		font = pg.font.Font('freesansbold.ttf', size)
		text = font.render(txt, True, settings.RED, settings.WHITE)
		textRect = text.get_rect()
		textRect.center = vec
		self._screen.blit(text, textRect)

	def events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self._running = False
				self._stay = False
			if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
				self.shots_ship.add(ShotShip(self._ship.rect.x + (settings.WIDTH_SHIP / 2) - (settings.WIDTH_SHOT / 2), self._ship.rect.y))
				self._score -= 1
		keys = pg.key.get_pressed()
		if keys[pg.K_LEFT] and self._ship.rect.x > 10:
			self._ship.update(- settings.SPEED_MOVE_SHIP)
		elif keys[pg.K_RIGHT] and self._ship.rect.x < (settings.WIDTH - 57):
			self._ship.update(settings.SPEED_MOVE_SHIP)

	def move_objects(self):
		self.move_automatic_object()
		self.move_invaders()
		self.shot_invaders()

	def move_automatic_object(self):
		self.shots_ship.update()
		self.shots_invaders.update(self._level)
		self.jokers.update()

	def move_invaders(self):
		if len(self.invaders_group) > 0:
			add_y = False
			for invader in self.invaders_group.sprites():
				if invader.is_over_left():
					add_y = True
					Invader.direction = 1
				elif invader.is_over_right():
					add_y = True
					Invader.direction = -1
			if add_y:
				for invader in self.invaders_group.sprites():
					invader.add_y(self._level)							
			self.invaders_group.update()

	def shot_invaders(self):
		shot = random.randint(0, settings.PULSE_SHOTS_INVADERS + int(self._level * 0.1 + 1))
		create_joker = random.randint(0, settings.PULSE_CREATE_JOKER)
		if shot == settings.PULSE_SHOTS_INVADERS:
			invader_shot = random.choice(self.invaders_group.sprites())
			self.shots_invaders.add(ShotInvader(invader_shot.rect.x + (settings.WIDTH_INVADER / 2) - (settings.WIDTH_SHOT / 2), invader_shot.rect.y + (settings.HEIGHT_INVADER)))
		if create_joker == settings.PULSE_CREATE_JOKER:
			self.jokers.add(Joker(self._level))

	def collide(self):
		if pg.sprite.spritecollide(self._ship, self.shots_invaders, True):
			if self._life > 0:
				self._life -= 1
				self._score -= 100
			else:
				self._running = False
				self._continue = False
		if pg.sprite.spritecollide(self._ship, self.invaders_group, False):
			self._running = False
			self._continue = False
		pg.sprite.groupcollide(self.shots_ship, self.shots_invaders, True, True)
		pg.sprite.groupcollide(self.shots_ship, self.jokers, True, True)
		for invader in self.invaders_group.sprites():
			if pg.sprite.spritecollide(invader, self.shots_ship, True):
				if not invader.collision():
					self.invaders_group.remove(invader)
				self._score += 100
		for protector in self.protectors.sprites():
			if pg.sprite.spritecollide(protector, self.shots_invaders, True) and not protector.collision():
				self.protectors.remove(protector)


	def blit(self):
		self._screen.blit(self._image, (0, 0))
		self.jokers.draw(self._screen)
		self.invaders_group.draw(self._screen)
		self.shots_ship.draw(self._screen)
		self.shots_invaders.draw(self._screen)
		self.text(25, (settings.HEIGHT * settings.LOCATION_TEXT_GAME_X, settings.WIDTH * settings.LOCATION_TEXT_GAME_Y ), f"your score is {self._score}, your life is {self._life}. level: {self._level }")
		self._screen.blit(self._ship.image, self._ship.rect.topleft)
		self.protectors.draw(self._screen)
		pg.display.flip()

	def create_objects(self):
		self.protectors = pg.sprite.Group(Protector(((settings.WIDTH - 205) / (4 - (self._level // 2))) * protector) for protector in range(1, 4 - (self._level // 2) + 1)) # Protector.creat_group(self, self._level)
		self.invaders_group = pg.sprite.Group(Invader(col * 120, row * 100) for row in range(self._level) for col in range(settings.COLS_INVADERS))
		self.shots_ship = pg.sprite.Group()
		self.shots_invaders = pg.sprite.Group()
		self.jokers = pg.sprite.Group()

	def loop_game(self):
		while self._running and len(self.invaders_group) > 0:
			self.collide()
			self.events()
			self.move_objects()
			self.blit()
			self._clock.tick(settings.REFRESH_RATE)

	def run(self):
		self.background_music()
		self.create_objects()
		self.loop_game()
		self.game_over()

	def game_over(self):
		while self._stay:
			if not len(self.invaders_group) > 0:
				self._screen.blit(self._image_you_winner, (0, 0))
				for event in pg.event.get():
					if event.type == pg.QUIT:
						self._stay = False
					if event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
						game = GameManager(self._level + 1, self._life + 1, self._score)
						self._stay = False
						game.run()
				self.text(40, (settings.HEIGHT * 0.7, settings.WIDTH * 0.6), f"your score is {self._score}")
				self.text(40, (settings.HEIGHT * 0.7, settings.WIDTH * 0.1), f"press key-down for up level")
			else:
				self._screen.blit(self._image_game_over, (0, 0))
				for event in pg.event.get():
					try:
						if event.type == pg.QUIT:
							self._stay = False
						if event.key == pg.K_DOWN:
							game = GameManager(1, 3, 0)
							self._stay = False
							game.run()
					except:
						True

				self.text(40, (settings.HEIGHT * 0.7, settings.WIDTH * 0.6), f"your score is {self._score}")
				self.text(40, (settings.HEIGHT * 0.7, settings.WIDTH * 0.1), f"press key-down for play again")
			pg.display.flip()
			self._clock.tick(5)
