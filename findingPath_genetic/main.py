from population import *
from UI import *
from func import createGoodWall
from configs import *

if __name__ == '__main__':
	#popA = Population(number_population, mutation, speed)
	popA = Population2(number_population, mutation, speed)
	
	createGoodWall(popA.finishPos)

	game = Game2(popA, wall_list, good_wall_list, screen_width, screen_height, fps)

	game.run()
