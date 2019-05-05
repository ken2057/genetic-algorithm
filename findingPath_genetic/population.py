from object import *
from func import getDistance, randomAngle
import numpy as np
from configs import *
import os

def relu(arr):
	arr[arr>0.99] = 0.99
	return arr

class Population(object):
	def __init__(self, number_population, mutation, speed = 1, startPos = (50, screen_width/2,10,10)):
		self.gen = 0
		self.number_population = number_population
		self.mutation_chance = mutation
		self.speed = speed

		self.finishPos = (screen_height-50,screen_width/2,10,10)
		self.startPos = startPos

		self.count = 0
		self.listFitness = []
		self.population = self.createPop()

	def createPop(self):
		population = []
		for i in range(self.number_population):
			newBox = Box([self.startPos[0],self.startPos[1]], self.speed)
			population.append(newBox)
		return population

	def crossOver(self):
		self.listFitness = getDistance(self.population, self.finishPos)
		totalFit = [(x/max(self.listFitness)) for x in self.listFitness]
		listFinishCount = [x.finish_at_count for x in self.population]
		#die => giam ti le chon
		#finish it nuoc di nhat tang ti le
		for i in range(self.number_population):
			if self.population[i].dead:
				totalFit[i] *= 1.1
			elif min(listFinishCount) != -1 and i == listFinishCount.index(min(listFinishCount)):
				totalFit[i] *= 0.5
			elif listFinishCount[i] != -1:
				totalFit[i] *= 0.7
		#all dead => ti le chhon 10% each
		if min(totalFit) == max(totalFit):
			totalFit = [0.5]*self.number_population
		
		theChosen = []
		for i in range(int(self.number_population/2)):
			while True:
				pos = np.random.randint(self.number_population)
				if totalFit[pos] <= np.random.uniform(0,1):
					theChosen.append(self.population[pos].DNA)
					break
		
		childs = []
		for i in range(int(self.number_population)):
			parentA = theChosen[np.random.randint(len(theChosen))]
			parentB = theChosen[np.random.randint(len(theChosen))]
			#child = []
			#if self.mutation_chance >= np.random.uniform(0,1):
			#child = DNA()
			#else:
			child = self.mating(parentA, parentB)

			childs.append(child)

		#replace all current DNA
		#keep the last most fitness
		for i in range(self.number_population):
			#if i != self.listFitness.index(min(self.listFitness)):
			self.population[i].DNA = childs[i]

		for i in self.population:
			i.resetPos([self.startPos[0], self.startPos[1]])

		self.gen += 1

	def mating(self, parentA, parentB):
		mid = np.random.randint(len(parentA))
		child = parentA[0:mid] + parentB[mid:]
		new_DNA = self.mutation(child)
		return new_DNA

	def mutation(self, DNA):
		for i in range(len(DNA)):
			if np.random.uniform(0,1) <= self.mutation_chance :
				DNA[i] = randomAngle()
		return DNA

class Population2(object):
	def __init__(self, number_population, mutation, speed = 1, startPos = (50, screen_width/2,10,10)):
		self.gen = 0
		self.number_population = number_population
		self.mutation_chance = mutation
		self.speed = speed

		self.finishPos = (screen_height-50,screen_width/2,10,10)
		self.startPos = startPos

		self.count = 0
		self.listFitness = []
		self.population = self.createPop()

	def createPop(self):
		population = []
		for i in range(self.number_population):
			newBox = Box2([self.startPos[0],self.startPos[1]], self.speed)
			population.append(newBox)
		return population

	def crossOver(self):
		self.listFitness = getDistance(self.population, self.finishPos)
		totalFit = [(x/max(self.listFitness)) for x in self.listFitness]
		listFinishCount = [x.finish_at_count for x in self.population]
		#die => giam ti le chon
		#finish it nuoc di nhat tang ti le
		theChosen = []

		for i in range(self.number_population):
			if self.population[i].dead:
				totalFit[i] *= 1.15
			elif min(listFinishCount) != -1 and i == listFinishCount.index(min(listFinishCount)):
				totalFit[i] = 0
				theChosen.append(self.population[i])
			elif listFinishCount[i] != -1:
				totalFit[i] *= 0.9
		#all dead => ti le chhon 10% each
		
		totalFit = relu(np.array(totalFit))

		if min(totalFit) >= 0.99:
			totalFit = [0]*self.number_population

		# os.system('cls')
		# t = [round(x,3) for x in totalFit]
		# print(*t, sep='\t')

		for i in range(int(self.number_population/2 - len(theChosen))):
			while True:
				pos = np.random.randint(self.number_population)
				if totalFit[pos] <= np.random.uniform(0,1):
					theChosen.append(self.population[pos])
					break

		childs = []
		for i in range(int(self.number_population)):
			parentA = theChosen[np.random.randint(len(theChosen))]
			parentB = theChosen[np.random.randint(len(theChosen))]

			child = self.mating(parentA, parentB)

			childs.append(child)
	
		#replace all current DNA
		#keep the last most fitness
		for i in range(self.number_population):
			#if i != self.listFitness.index(min(self.listFitness)):
			self.population[i].DNA = childs[i]

		for i in self.population:
			i.resetPos([self.startPos[0], self.startPos[1]])

		self.gen += 1

	def mating(self, parentA, parentB):
		if parentA.finish:
			new_DNA = self.mutation(parentA.DNA)
			return new_DNA
		elif parentA.finish:
			new_DNA = self.mutation(parentB.DNA)
			return np.array(new_DNA)

		child = []
		mid = max(parentA.dead_at_count, parentB.dead_at_count)
		last = [randomAngle()] * (DNA_length - mid + 5)

		if parentA.dead_at_count == parentB.dead_at_count:
			for i in range(DNA_length):
				child.append(round((parentA.DNA[i] + parentB.DNA[i]) / 2, 2))
			child = np.array(child)
		elif parentA.dead_at_count == mid:
			child = np.concatenate((parentA.DNA[0:mid - 5], [parentA.DNA[mid-5]]*(DNA_length-mid+5)), axis = 0)
		else:
			child = np.concatenate((parentB.DNA[0:mid - 5], [parentB.DNA[mid-5]]*(DNA_length-mid+5)), axis = 0)

		new_DNA = self.mutation(child)
		return new_DNA

	def mutation(self, DNA):
		for i in range(len(DNA)):
			if np.random.uniform(0,1) <= self.mutation_chance :
				DNA[i] = randomAngle()
		return DNA
