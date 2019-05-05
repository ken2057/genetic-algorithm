import pygame as pg
from wall import Wall
from population import *
from func import createGoodWall, getDistance
from configs import *

class Game(object):
	def __init__(self, population, badWall, goodWall, width, height, fps=60):
		pg.init()
		pg.display.set_caption('Genetic')
		self.font = pg.font.SysFont('Aria',25)
		self.screen = pg.display.set_mode([height,width])
		self.gameExit = False
		self.gamePause = True	
		self.clock = pg.time.Clock()
		self.fps = fps
		self.pop = population
		self.listWall = badWall
		self.listWallGood = goodWall

	def even_loop(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.gameExit = True
			#create wall
			mouse = pg.mouse.get_pressed()
			if mouse[0] == 1:
				pos = pg.mouse.get_pos()
				wall = Wall(pos[0]-5, pos[1]-5,10,10)
				wall_list.add(wall)
				self.listWall = wall_list
			#xoa wall
			elif mouse[2] == 1:
				pos = pg.mouse.get_pos()
				pos = [x-5 for x in pos]
				flag = False
			#scan trong phạm vi -4->3 pixell (x,y)
				for i in wall_list:
					for x in range(-4,4):
						for y in range(-4,4):
							if i.rect == pg.Rect(pos[0]+x, pos[1]+y,10,10):
								wall_list.remove(i)
								flag = True
								break
						if flag:
							break
					if flag:
						break
				
				self.listWall = wall_list

			if event.type == pg.KEYDOWN:
			#xoa all wall
				if event.key == pg.K_q:
					wall_list.empty()
					self.listWall = pg.sprite.Group()
			#pause/unpause game
				elif event.key == pg.K_SPACE:
					self.gamePause = not self.gamePause
			#reset population
				elif event.key == pg.K_r:
					self.pop = Population(self.pop.number_population, self.pop.mutation_chance, self.pop.speed, self.pop.startPos)
			#set new pos for finish
				elif event.key == pg.K_f:
					pos = pg.mouse.get_pos()
					prePos = self.pop.finishPos
					self.pop.finishPos = (pos[0], pos[1], 10, 10)
					good_wall_list.empty()
					createGoodWall(self.pop.finishPos)
			#set new pos for start
				elif event.key == pg.K_s:
					pos = pg.mouse.get_pos()
					self.pop = Population(self.pop.number_population, self.pop.mutation_chance, self.pop.speed, (pos[0], pos[1], 10, 10))
				
	def draw(self):
		colorLast = (232, 150, 217)

		distance = getDistance(self.pop.population, self.pop.finishPos)
		count_Dead = 0
		count_Finish = 0
		pos_min_fit = [10000,10000]
		for i in range(self.pop.number_population):
			if self.pop.population[i].finish:
				count_Finish += 1
			if self.pop.population[i].dead:
				count_Dead += 1
			if not self.pop.population[i].dead and not self.pop.population[i].finish and distance[i] < pos_min_fit[1]:
				pos_min_fit[0] = i
				pos_min_fit[1] = distance[i]

		#setting text
		self.screen.fill(pg.Color('black'))
		genTxt = self.font.render('Gen: %s'%self.pop.gen, 1,(255,255,255))
		second = self.font.render('%s/%s'%(self.pop.count, DNA_length),1,(255,255,255))
		
		mutationTxt = self.font.render('Mutation: %s%%'%(self.pop.mutation_chance*100), 1, (255,255,255))
		popTxt = self.font.render('Number population: %s'%(self.pop.number_population), 1, (255,255,255))
		currentFitness = self.font.render('Current specie fitness: %s - %s'%(pos_min_fit[0], round(pos_min_fit[1],2)),1, pg.Color('green'))
		countFinish = self.font.render('Finish: %s'%count_Finish, 1, (197, 232, 52))
		countDead = self.font.render('Dead: %s'%count_Dead, 1, (43, 50, 52))

		#draw start pos
		pg.draw.rect(self.screen, pg.Color('blue'), (self.pop.startPos[0]-5, self.pop.startPos[1]-5,10,10))

		#draw species
		for pos in range(self.pop.number_population):
			if pos_min_fit[0] == pos:
				self.pop.population[pos].draw(self.screen, 'green')
			else:
				self.pop.population[pos].draw(self.screen)

		#draw wall
		self.listWall.draw(self.screen)
		self.listWallGood.draw(self.screen)

		#text
		self.screen.blit(genTxt,(10,10))
		self.screen.blit(second,(100,10))
		
		self.screen.blit(currentFitness,(10,30))
		self.screen.blit(countFinish,(10,50))
		self.screen.blit(countDead,(10,70))
		
		self.screen.blit(mutationTxt, (10,screen_width-40))
		self.screen.blit(popTxt,(10,screen_width-20))
		
	def update(self):
		for member in self.pop.population:
			member.update(self.pop.count)

	def run(self):
		while not self.gameExit:
			self.even_loop()
			self.draw()
			
			if not self.gamePause:
				self.update()

				self.pop.count += 1
				crossOver = False
				for i in self.pop.population:
					if not i.dead and not i.finish:
						break
				else:
					crossOver = True

				if crossOver or self.pop.count == DNA_length:
					self.pop.crossOver()
					crossOver = False
					self.pop.count = 0

			pg.display.flip()
			pg.display.update()
			pg.display.flip()
			self.clock.tick(self.fps)

class Game2(object):
	def __init__(self, population, badWall, goodWall, width, height, fps=60):
		pg.init()
		pg.display.set_caption('Genetic')
		self.font = pg.font.SysFont('Aria',25)
		self.screen = pg.display.set_mode([height,width])
		self.gameExit = False
		self.gamePause = True	
		self.clock = pg.time.Clock()
		self.fps = fps
		self.pop = population
		self.listWall = badWall
		self.listWallGood = goodWall

	def even_loop(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.gameExit = True
			#create wall
			mouse = pg.mouse.get_pressed()
			if mouse[0] == 1:
				pos = pg.mouse.get_pos()
				wall = Wall(pos[0]-5, pos[1]-5,10,10)
				wall_list.add(wall)
				self.listWall = wall_list
			#xoa wall
			elif mouse[2] == 1:
				pos = pg.mouse.get_pos()
				pos = [x-5 for x in pos]
				flag = False
			#scan trong phạm vi -4->3 pixell (x,y)
				for i in wall_list:
					for x in range(-4,4):
						for y in range(-4,4):
							if i.rect == pg.Rect(pos[0]+x, pos[1]+y,10,10):
								wall_list.remove(i)
								flag = True
								break
						if flag:
							break
					if flag:
						break
				
				self.listWall = wall_list

			if event.type == pg.KEYDOWN:
			#xoa all wall
				if event.key == pg.K_q:
					wall_list.empty()
					self.listWall = pg.sprite.Group()
			#pause/unpause game
				elif event.key == pg.K_SPACE:
					self.gamePause = not self.gamePause
			#reset population
				elif event.key == pg.K_r:
					self.pop = Population2(self.pop.number_population, self.pop.mutation_chance, self.pop.speed, self.pop.startPos)
			#set new pos for finish
				elif event.key == pg.K_f:
					pos = pg.mouse.get_pos()
					prePos = self.pop.finishPos
					self.pop.finishPos = (pos[0], pos[1], 10, 10)
					good_wall_list.empty()
					createGoodWall(self.pop.finishPos)
			#set new pos for start
				elif event.key == pg.K_s:
					pos = pg.mouse.get_pos()
					self.pop = Population2(self.pop.number_population, self.pop.mutation_chance, self.pop.speed, (pos[0], pos[1], 10, 10))
				
	def draw(self):
		colorLast = (232, 150, 217)

		distance = getDistance(self.pop.population, self.pop.finishPos)
		count_Dead = 0
		count_Finish = 0
		pos_min_fit = [10000,10000]
		for i in range(self.pop.number_population):
			if self.pop.population[i].finish:
				count_Finish += 1
			if self.pop.population[i].dead:
				count_Dead += 1
			if not self.pop.population[i].dead and not self.pop.population[i].finish and distance[i] < pos_min_fit[1]:
				pos_min_fit[0] = i
				pos_min_fit[1] = distance[i]

		#setting text
		self.screen.fill(pg.Color('black'))
		genTxt = self.font.render('Gen: %s'%self.pop.gen, 1,(255,255,255))
		second = self.font.render('%s/%s'%(self.pop.count, DNA_length),1,(255,255,255))
		
		mutationTxt = self.font.render('Mutation: %s%%'%(self.pop.mutation_chance*100), 1, (255,255,255))
		popTxt = self.font.render('Number population: %s'%(self.pop.number_population), 1, (255,255,255))
		currentFitness = self.font.render('Current specie fitness: %s - %s'%(pos_min_fit[0], round(pos_min_fit[1],2)),1, pg.Color('green'))
		countFinish = self.font.render('Finish: %s'%count_Finish, 1, (197, 232, 52))
		countDead = self.font.render('Dead: %s'%count_Dead, 1, (43, 50, 52))

		#draw start pos
		pg.draw.rect(self.screen, pg.Color('blue'), (self.pop.startPos[0]-5, self.pop.startPos[1]-5,10,10))

		#draw species
		for pos in range(self.pop.number_population):
			if pos_min_fit[0] == pos:
				self.pop.population[pos].draw(self.screen, 'green')
			else:
				self.pop.population[pos].draw(self.screen)

		#draw wall
		self.listWall.draw(self.screen)
		self.listWallGood.draw(self.screen)

		#text
		self.screen.blit(genTxt,(10,10))
		self.screen.blit(second,(100,10))
		
		self.screen.blit(currentFitness,(10,30))
		self.screen.blit(countFinish,(10,50))
		self.screen.blit(countDead,(10,70))
		
		self.screen.blit(mutationTxt, (10,screen_width-40))
		self.screen.blit(popTxt,(10,screen_width-20))

		pg.display.flip()
		
	def update(self):
		for member in self.pop.population:
			member.update(self.pop.count)

	def run(self):
		while not self.gameExit:
			self.even_loop()
			self.draw()
			
			if not self.gamePause:
				self.update()

				self.pop.count += 1
				crossOver = False
				for i in self.pop.population:
					if not i.dead and not i.finish :
						break
				else:
					crossOver = True

				if crossOver or self.pop.count == DNA_length:
					self.pop.crossOver()
					crossOver = False
					self.pop.count = 0

			pg.display.update()
			self.clock.tick(self.fps)
