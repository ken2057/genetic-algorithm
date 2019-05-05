from tkinter import *

class Box(object):
	root = Tk()
	varGen = StringVar()
	varPopulation = StringVar()
	varMutation = StringVar()
	varMaxFit = StringVar()
	varSpMaxFit = StringVar()
	varEmpty = StringVar()
	varTotalMaxFit = StringVar()
	listbox = Listbox(root, height=10)

	def __init__(self):
		self.root.title('Text genetic')
		self.root.geometry("500x600")	
		Label(self.root).grid(row=0)
		Label(self.root).grid(column=1)

		Label(self.root, textvariable = self.varMaxFit, font=("Aria", 14)).grid(sticky="W",row=1)
		Label(self.root, textvariable = self.varTotalMaxFit, font=("Aria", 14)).grid(sticky="W",row=2)
		Label(self.root, textvariable = self.varPopulation, font=("Aria", 14)).grid(sticky="W",row=3)
		Label(self.root, textvariable = self.varMutation, font=("Aria", 14)).grid(sticky="W",row=4)
		Label(self.root, textvariable = self.varGen, font=("Aria", 14)).grid(sticky="W",row=5)
		
		Label(self.root, text='Specie w/ max fitness: ', font=("Aria",14)).grid(row=0)
		Label(self.root, textvariable = self.varSpMaxFit, font=("Aria", 14)).grid(row=0, column=1,columnspan=100)

		self.listbox.grid(row=1, column=2,rowspan=100, columnspan=100)

	def updateValue(self, popA):
		if popA.gen < 5:
			minW = 500
			w = int(len(popA.sample)*22)
			if minW > w:
				h = str(minW)+'x600'
			else:
				h = str(w)+'x600'
			self.root.geometry(h)
			self.listbox.config(width=int(len(popA.sample)*1.5), height=30, justify=CENTER, font=("Aria", 12))
			self.varPopulation.set('Population: %s'%popA.number_population)
			self.varMutation.set('Mutation: %s%%'%(popA.mutation_chance*100))

		self.varTotalMaxFit.set('Total max fitness: %s'%popA.fitness.count(max(popA.fitness)))
		self.varGen.set('Gen: %s'%popA.gen)
		self.varMaxFit.set('Max fitness: %s'%max(popA.fitness))
		self.varSpMaxFit.set('%s'%popA.population[popA.fitness.index(max(popA.fitness))])
		
		self.listbox.delete(0,END)
		self.listbox.insert(END, *popA.population)
		for i in range(len(popA.fitness)):
			if popA.fitness[i] == max(popA.fitness):
				self.listbox.itemconfig(i, {'bg':'green'})
			elif popA.fitness[i] == max(popA.fitness)-1:
				self.listbox.itemconfig(i, {'bg':'yellow'})
			elif popA.fitness[i] == max(popA.fitness)-2:
				self.listbox.itemconfig(i, {'bg':'gray'})
			else:
				self.listbox.itemconfig(i, {'bg':'white'})

		self.root.update()
