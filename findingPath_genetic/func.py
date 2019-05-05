import math
import numpy as np
from configs import *
from wall import Wall

def createGoodWall(finishPos):
	wall = Wall(finishPos[0]-5, finishPos[1]-5, finishPos[2], finishPos[3])
	wall.image.fill(pg.Color('red'))
	good_wall_list.add(wall)

def randomAngle():
	angle = np.random.uniform(0, 2.0*math.pi)
	#angle = (np.random.uniform(0, 1)*360)
	#angle = np.random.randint(-180,181)
	#return round(angle,2)
	return angle

def getVector(angle, speed):
	vector = [speed * math.cos(angle), speed * math.sin(angle)]
	vector = [round(x,2) for x in vector]
	return vector

def project(pos, angle, distance):
	x = pos[0] + (math.cos(angle) * distance)
	y = pos[1] - (math.sin(angle) * distance)
	if x < 0:
		x = 0
	elif x > screen_height:
		x = pos[0]
	if y < 0:
		y = 0
	elif y > screen_width:
		y = pos[1]
	
	return(x,y)

def DNA():
	DNA = []
	for i in range(DNA_length):
		DNA.append(randomAngle())
	return DNA

def DNA2():
	DNA = []
	for i in range(int(DNA_length/10)):
		DNA.append([randomAngle()]*10)
	DNA = np.array(DNA).ravel()
	return DNA

def getDistance(listPop, finishPos):
	listFitness = []
	for i in listPop:
		fit = math.sqrt((finishPos[0] - i.pos[0])**2 + (finishPos[1] - i.pos[1])**2)
		listFitness.append(fit)
	return listFitness