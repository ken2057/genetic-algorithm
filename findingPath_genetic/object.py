import pygame as pg
import numpy as np
from func import *
from configs import *
import copy

class Box(pg.sprite.Sprite):
	def __init__(self, pos, speed = 1):
		self.pos = pos
		self.speed = speed
		self.radius = 10
		self.rect = pg.Rect(0,0,self.radius,self.radius)
		self.DNA = DNA()
		self.dead = False
		self.finish = False
		self.finish_at_count = -1
		self.rect.center = pos

	def resetPos(self, pos):
		self.pos = pos
		self.rect.center = self.pos
		self.dead = False
		self.finish = False
		self.finish_at_count = -1

	def update(self, count):
		if not self.dead and not self.finish:
			block_hit_list = pg.sprite.spritecollide(self, wall_list, False)
			finish_hit = pg.sprite.spritecollide(self, good_wall_list, False)

			if len(block_hit_list) == 0:	
				self.pos = project(self.pos, self.DNA[count], self.speed)
				self.rect.center = self.pos
			else:
				self.dead = True
				#self.DNA[count] = randomAngle()

			if len(finish_hit) > 0:
				for i in finish_hit:
					self.pos = [i.rect[0]+5, i.rect[1]+5]
					break
				self.finish = True
				self.finish_at_count = count

	def draw(self, surface, color = 'white'):
		pos = [int(x) for x in self.pos]
		if self.dead and not self.finish:
			pg.draw.circle(surface, (43, 50, 52), pos, self.radius)
		elif self.finish:
			pg.draw.circle(surface, (197, 232, 52), pos, self.radius)
		else:
			if type(color) == str:
				pg.draw.circle(surface, pg.Color(color), pos, self.radius)
			else:
				pg.draw.circle(surface, color, pos, self.radius)

class Box2(pg.sprite.Sprite):
	def __init__(self, pos, speed = 1):
		self.pos = pos
		self.speed = speed
		self.radius = 6
		self.rect = pg.Rect(0,0,self.radius,self.radius)

		self.DNA = [randomAngle()] * DNA_length
		self.current = 0
		self.dead = False
		self.finish = False
		self.finish_at_count = -1
		self.dead_at_count = -1
		self.rect.center = pos

	def resetPos(self, pos):
		self.pos = pos
		self.rect.center = self.pos
		self.dead = False
		self.finish = False
		self.finish_at_count = -1
		self.dead_at_count = -1
		self.current = 0

	def update(self, count):
		if not self.dead and not self.finish:
			self.rect.center = project(self.rect.center, self.DNA[count], self.speed * 2)
			block_hit_list = pg.sprite.spritecollide(self, wall_list, False)

			if len(block_hit_list) > 0:	
				deg = np.random.randint(-180, 181)
				self.DNA[count] += deg

				if self.DNA[count] > 180:
					self.DNA[count] -= 360
				elif self.DNA[count] < -180:
					self.DNA[count] += 360

			self.pos = project(self.pos, self.DNA[count], self.speed)
			self.rect.center = self.pos

			block_hit_list = pg.sprite.spritecollide(self, wall_list, False)
			if len(block_hit_list) > 0:
				self.dead = True
				self.dead_at_count = count

			finish_hit = pg.sprite.spritecollide(self, good_wall_list, False)
			if len(finish_hit) > 0:
				for i in finish_hit:
					self.pos = [i.rect[0]+5, i.rect[1]+5]
					break
				self.finish = True
				self.finish_at_count = count

			self.current += 1

	def draw(self, surface, color = 'white'):
		pos = [int(x) for x in self.pos]
		if self.dead and not self.finish:
			pg.draw.circle(surface, (43, 50, 52), pos, self.radius)
		elif self.finish:
			pg.draw.circle(surface, (197, 232, 52), pos, self.radius)
		else:
			if type(color) == str:
				posEnd = project(self.pos, self.DNA[self.current], self.speed)

				print()
				print(self.pos)
				print(posEnd)

				pg.draw.circle(surface, pg.Color(color), pos, self.radius)

				pg.draw.line(surface, pg.Color(color), self.pos, posEnd, self.speed*self.radius)
				
			else:
				pg.draw.circle(surface, color, pos, self.radius)