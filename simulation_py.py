from motion_py import *
from farmTypes_py import *
from farming_py import *
from workers_py import *

#
#
#
def leaderboard_FastReset():
	return True

# 1770.77 - When Simulated
# leaderboard_run(Leaderboards.Maze, "simulation_py", 1024)
# 30:34.418 - #1276
def leaderboard_Maze():
	def condition():
		return not (num_items(GOLD) >= 9863168)

	def mazeMinion(x, y):
		# Go to Starting Point
		moveTo((x, y))
		# Wait for Maze to be there
		while get_entity_type() != HEDGE:
			continue
		# Search for Treasure
		spawn_drone(leftWallMethod, 32)
		rightWallMethod(32)

	while condition():
		spawn_drone(mazeMinion, 0, 31)
		spawn_drone(mazeMinion, 31, 31)
		spawn_drone(mazeMinion, 31, 0)
		createAndSolveMaze(0, 0, 32)

# 1289.03 - When Simulated
# leaderboard_run(Leaderboards.Maze, "simulation_py", 1024)
# 21:29.908 - #1215
def leaderboard_MazeSpammer():
	def condition():
		return not (num_items(GOLD) >= 9863168)

	spamMazes(condition)

# Hamiltonion Array Snake - with Shortcuts - Phase optimization
# Greed = 70, brute = 375
# Unable to simulate because of hat upgrades?
# leaderboard_run(Leaderboards.Dinosaur, "simulation_py", 2048)
# 17:25.618 - #303
def leaderboard_Dinos():
	def condition():
		return not (num_items(BONES) >= 33488928)

	dinosaurWorker(condition)

# 66.52 - When Simulated
# leaderboard_run(Leaderboards.Cactus, "simulation_py", 512)
# 1:06.819 - #1291
def leaderboard_Cacti():
	# Starts with 1B Pumpkin, no need to plant anything else
	# Run Cacti
	def condition():
		return not (num_items(CACTI) >= 33554432)

	megaWorker(CACTUS, cactusWorker, condition)

# 609.17 - When Simulated
# leaderboard_run(Leaderboards.Sunflowers, "simulation_py", 1024)
# 10:09.624 - #922
def leaderboard_Sunflowers():
	def condition():
		return not (num_items(POWER) >= 100000)

	megaWorker(SUNFLOWER, cactusWorker, condition)


# 1561.29 - When Simulated
# leaderboard_run(Leaderboards.Pumpkins, "simulation_py", 1024)
# 25:20.846 - #1234
def leaderboard_Pumpkins():
	def condition():
		return not (num_items(PUMPKINS) >= 200000000)

	megaWorker(PUMPKIN, cactusWorker, condition)


# 2792.07 - When Simulated
# leaderboard_run(Leaderboards.Wood, "simulation_py", 1024)
# 46:02.122 - #779
def leaderboard_Wood():
	def condition():
		return not (num_items(WOOD) >= 10000000000)

	# Get starter wood to plant carrots
	for i in range(25):
		harvestAndPlant(BUSH, False, False, True, False)
		if get_water() < 0.75:
			use_item(WATER)

	Xs = [2, 7, 12, 17, 22, 27]
	Ys = [2, 7, 12, 17, 22, 27]

	for x in Xs:
		for y in Ys:
			spawn_drone(polyWorker, condition, x, y, 5)

	while condition():
		for x in range (30):
			for y in range(30):
				moveTo((x, y))
				while get_water() < 0.75:
					use_item(WATER)

# 3207.1 - When Simulated
# leaderboard_run(Leaderboards.Carrots, "simulation_py", 1024)
# 54:25.840 - #528
def leaderboard_Carrots():
	def condition():
		return not (num_items(CARROTS) >= 2000000000)

	# Get starter wood to plant carrots
	for i in range(25):
		harvestAndPlant(BUSH, False, False, True, False)
		if get_water() < 0.75:
			use_item(WATER)

	Xs = [2, 7, 12, 17, 22, 27]
	Ys = [2, 7, 12, 17, 22, 27]

	for x in Xs:
		for y in Ys:
			spawn_drone(polyWorker, condition, x, y, 5)

	while condition():
		for x in range (30):
			for y in range(30):
				moveTo((x, y))
				while get_water() < 0.75:
					use_item(WATER)

# 2213.24 - When Simulated
# leaderboard_run(Leaderboards.Hay, "simulation_py", 512)
# 37:42.715 - #1027
def leaderboard_Hay():
	def condition():
		return not (num_items(HAY) > 2000000000)


	# Get starter wood to plant carrots
	for i in range(25):
		harvestAndPlant(BUSH, False, False, True, False)
		if get_water() < 0.75:
			use_item(WATER)

	Xs = [2, 7, 12, 17, 22, 27]
	Ys = [2, 7, 12, 17, 22, 27]

	for x in Xs:
		for y in Ys:
			spawn_drone(polyWorker, condition, x, y, 5)

	while condition():
		for x in range (30):
			for y in range(30):
				moveTo((x, y))
				while get_water() < 0.75:
					use_item(WATER)

#
#
#
def leaderboard_MazeSingle():
	def condition():
		return not (num_items(GOLD) >= 616448)

#
#
#
def leaderboard_CactiSingle():
	def condition():
		return not (num_items(CACTI) >= 131072)

#
#
#
def leaderboard_SunflowersSingle():
	def condition():
		return not (num_items(POWER) >= 10000)

#
#
#
def leaderboard_PumpkinsSingle():
	def condition():
		return not (num_items(PUMPKINS) >= 10000000)

#
#
#
def leaderboard_WoodSingle():
	def condition():
		return not (num_items(WOOD) >= 500000000)

#
#
#
def leaderboard_CarrotsSingle():
	def condition():
		return not (num_items(CARROTS) >= 100000000)

# 
# 
# 
def leaderboard_HaySingle():
	def condition():
		return not (num_items(CARROTS) >= 100000000)
	
############################
########### MAIN ###########
############################

leaderboard_Dinos()

############################
########### MAIN ###########
############################