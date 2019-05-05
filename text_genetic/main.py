from Genetic import Gen
from FormBox import Box

popA = Gen(200,0.05,'hello_world')
#This_is_genetic_algorithm_wellcome_to_the_houze
popA.simulation()
	
root = Box()

if __name__=='__main__':
	while max(popA.fitness) < len(popA.sample):
		popA.simulation()
		root.updateValue(popA)
	root.updateValue(popA)
	root.root.mainloop()