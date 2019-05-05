import pygame as pg

class Wall(pg.sprite.Sprite):
	def __init__(self, x, y, width, height):
		super().__init__()

		self.image = pg.Surface([width, height])
		self.image.fill(pg.Color('grey'))

		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x