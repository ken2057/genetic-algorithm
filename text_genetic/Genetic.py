import numpy as np

class Gen(object):
	number_population = 200
	mutation_chance = 0.1
	sample = 'New_The_Her_Nor_Case_That_Lady_Paid_Read_InvitaTion_FriendShip_TraveLling_Eat_EveryThing_The_Out_Two'

	gen = 0
	population = []
	fitness = []

	def __init__(self, population, mutation, sample):
		self.number_population = population
		self.mutation_chance = mutation
		self.sample = sample

	def simulation(self):
		if self.gen == 0:
			for i in range(self.number_population):
				self.population.append(self.DNA(len(self.sample)))

		self.fitness = [self.checkFitness(x) for x in self.population]

		self.crossOver()

		self.gen+=1

	def crossOver(self):
		totalFit = sum(self.fitness)
		childs = []
		fit = []
		if totalFit > 0:
			fit = [round(float(x/totalFit),2)+0.1 for x in self.fitness]
			#print(fit)
			matingpool = []

			for i in range(int(len(self.population)/2)):
				while True:
					num = np.random.randint(len(fit))
					numFit = np.random.uniform(0,1)
					if numFit <= fit[num]:
						matingpool.append(self.population[num])
						break

			for i in range(int(len(fit)/2)):
				parent1 = np.random.choice(matingpool)
				parent2 = np.random.choice(matingpool)
				child = self.mating(parent1, parent2)
				childs.append(child)
		else:
			A = np.random.choice(self.population)
			B = np.random.choice(self.population)

			childs = self.mating(A, B)

		for i in range(len(childs)):
			childs[i] = self.mutation(childs[i])

		for i in range(len(childs)):
			count = 0
			pos = np.random.randint(len(fit))
			while True:
				pos = np.random.randint(len(fit))
				if self.fitness[pos] < max(self.fitness) or count > int(len(self.fitness)/2):
					break
				count+=1

			self.population[pos] = childs[i]

	def checkFitness(self, strI):
		fitness = 0

		for i in range(len(self.sample)):
			if strI[i] == self.sample[i]:
				fitness += 1

		return fitness

	def mating(self, A, B):
		n = len(A)
		child = A[0:int(n/2)-1]
		child += B[int(n/2)-1:]

		"""for i in range(n):
						if np.random.randint(2) == 0:
							child+=A[i]
						else: 
							child+=B[i]"""
		return child

	def mutation(self, strI):
		rate = self.mutation_chance * 100
		newStr = ''
		for i in range(len(strI)):
			if(np.random.randint(100) <= rate):
				newStr += chr(np.random.randint(65,123))
			else:
				newStr += strI[i]
		return newStr

	def DNA(self, n):
		gen = ''
		for i in range(n):
			char = chr(np.random.randint(65,123))
			gen+=char
		return gen
