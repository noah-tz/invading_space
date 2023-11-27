import settings
from class_ship import Ship
from class_invaders import Invaders
from class_shots import Shot_ship
from class_shots_invaders import Shot_invaders
from class_joker import Jokers
from class_protector import Protector

import random
import pygame as pg




pg.init()
class Game:
	def __init__(self, level, life, score):
		self.level = level
		self.image = settings.IMG_GAME
		self.name = 'invaders space'
		self.scr = pg.display.set_mode(settings.SIZE)
		self.clock = pg.time.Clock()
		self.running = True
		self.clock = pg.time.Clock()
		self.revers = False
		self.life = life
		self.score = score
		self.stay = True
		self.image_game_over = settings.IMG_GAME_OVER
		self.image_you_winner = settings.IMG_YOU_WINNER
		self.ship = Ship((settings.WIDTH - 100) // 2, int(settings.HEIGHT * 0.8))

	def background_music(self):
		explosion_sound = pg.mixer.Sound(settings.SOUND_GAME)
		pg.mixer.Sound.play(explosion_sound)

	def shot_sound(self):
		pg.mixer.init()
		pg.mixer.music.load(settings.SOUND_SHOT)
		pg.mixer.music.play()

	def text(self, size, vec, txt):
		font = pg.font.Font('freesansbold.ttf', size)
		text = font.render(txt, True, settings.RED, settings.WHITE)
		textRect = text.get_rect()
		textRect.center = vec
		self.scr.blit(text, textRect)

	def events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.running = False
				self.stay = False
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_SPACE:
					self.shot_sound()
					self.shots_ship.add(Shot_ship(self.ship.rect.x + (settings.WIDTH_SHIP / 2) - (settings.WIDTH_SHOT / 2), self.ship.rect.y))
					self.score -= 1
		keys = pg.key.get_pressed()
		if keys[pg.K_LEFT] and self.ship.rect.x > 10:
			self.ship.move_ship(- settings.SPEED_MOVE_SHIP)
		elif keys[pg.K_RIGHT] and self.ship.rect.x < (settings.WIDTH - 57):
			self.ship.move_ship(settings.SPEED_MOVE_SHIP)

	def move_objects(self):
		self.move_automatic_object()
		self.move_invaders(self.invaders_group.sprites())
		self.shot_invaders()

	def move_automatic_object(self):
		self.shots_ship.update()
		self.shots_invaders.update(self.level)
		self.jokers.update(self.level)

	def move_invaders(self, invaders):
		if len(self.invaders_group) > 0:
			x_max = max([i.rect.x for i in invaders])
			x_min = min([i.rect.x for i in invaders])
			if (x_min <= 0) and (self.revers == True):
				self.invaders_group.update(0, self.level * 0.2 + settings.SPEED_DOWN_INVADERS)
				self.revers = False
			if (x_max >= (settings.HEIGHT * 1.28)) and (self.revers == False):
				self.revers = True
				self.invaders_group.update(0, self.level * 0.2 + settings.SPEED_DOWN_INVADERS)
			if self.revers:
				self.invaders_group.update(- settings.SPEED_MOVE_INVADERS, 0)
			else:
				self.invaders_group.update(settings.SPEED_MOVE_INVADERS, 0)

	def shot_invaders(self):
		shot = random.randint(0, settings.PULSE_SHOTS_INVADERS + int(self.level * 0.1 + 1))
		create_joker = random.randint(0, settings.PULSE_CREATE_JOKER)
		if shot == settings.PULSE_SHOTS_INVADERS:
			invader_shot = random.choice(self.invaders_group.sprites())
			self.shots_invaders.add(Shot_invaders(invader_shot.rect.x + (settings.WIDTH_INVADER / 2) - (settings.WIDTH_SHOT / 2), invader_shot.rect.y + (settings.HEIGHT_INVADER)))
		if create_joker == settings.PULSE_CREATE_JOKER:
			self.jokers.add(Jokers(self.level))

	def collide(self):
		collide_ship_shots = pg.sprite.spritecollide(self.ship, self.shots_invaders, True)
		collide_ship_invaders = pg.sprite.spritecollide(self.ship, self.invaders_group, False)
		pg.sprite.groupcollide(self.shots_ship, self.shots_invaders, True, True)
		pg.sprite.groupcollide(self.shots_ship, self.jokers, True, True)
		for i in self.invaders_group.sprites():
			if pg.sprite.spritecollide(i, self.shots_ship, True):
				if i.life > 0:
					i.life -= 1
					i.image = settings.IMG_INVADER_RED
					self.score += 100
				else:
					self.invaders_group.remove(i)
		for i in self.protectors.sprites():
			if pg.sprite.spritecollide(i, self.shots_invaders, True):
				if i.life > 0:
					i.life -= 1
					i.image.fill(settings.RED)
				else:
					self.protectors.remove(i)
		if len(collide_ship_invaders) > 0:
			self.running = False
		if len(collide_ship_shots) > 0:
			if self.life > 0:
				self.life -= 1
				self.score -= 100
			else:
				self.running = False

	def blit_object(self):
		self.scr.blit(self.image, (0, 0))
		self.jokers.draw(self.scr)
		self.invaders_group.draw(self.scr)
		self.shots_ship.draw(self.scr)
		self.shots_invaders.draw(self.scr)
		self.text(25, (settings.HEIGHT * settings.LOCATION_TEXT_GAME_X, settings.WIDTH * settings.LOCATION_TEXT_GAME_Y ), f"your score is {self.score}, your life is {self.life}. level: {self.level }")
		self.scr.blit(self.ship.image, self.ship.rect.topleft)
		self.protectors.draw(self.scr)
		pg.display.flip()

	def create_objects(self):
		self.protectors = Protector.creat_group(self, self.level)
		self.invaders_group = Invaders.creat_group(self, min(self.level, 9))
		self.shots_ship = pg.sprite.Group()
		self.shots_invaders = pg.sprite.Group()
		self.jokers = pg.sprite.Group()

	def run(self):
		pg.display.set_caption('Show Text')
		pg.display.set_caption(self.name)
		self.background_music()
		self.create_objects()
		while self.running and len(self.invaders_group) > 0:
			self.collide()
			self.events()
			self.move_objects()
			self.blit_object()
			self.clock.tick(settings.REFRESH_RATE)
		self.game_over()

	def game_over(self):
		while self.stay:
			if not len(self.invaders_group) > 0:
				self.scr.blit(self.image_you_winner, (0, 0))
				for event in pg.event.get():
					try:
						if event.type == pg.QUIT:
							self.stay = False
						if event.key == pg.K_DOWN:
							game = Game(self.level + 1, self.life + 1, self.score)
							self.stay = False
							game.run()
					except:
						a = 1
				self.text(40, (settings.HEIGHT * 0.7, settings.WIDTH * 0.6), f"your score is {self.score}")
				self.text(40, (settings.HEIGHT * 0.7, settings.WIDTH * 0.1), f"press key-down for up level")
			else:
				self.scr.blit(self.image_game_over, (0, 0))
				for event in pg.event.get():
					try:
						if event.type == pg.QUIT:
							self.stay = False
						if event.key == pg.K_DOWN:
							game = Game(1, 3, 0)
							self.stay = False
							game.run()
					except:
						True

				self.text(40, (settings.HEIGHT * 0.7, settings.WIDTH * 0.6), f"your score is {self.score}")
				self.text(40, (settings.HEIGHT * 0.7, settings.WIDTH * 0.1), f"press key-down for play again")
			pg.display.flip()
			self.clock.tick(5)


