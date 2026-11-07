
#
# leaderboard_run(Leaderboards.Reset, "_leaderboard_", 1024)
#
def leaderboard_FastReset():
#	from _main_ import *
	return

# 1770.77 - When Simulated
# leaderboard_run(Leaderboards.Maze, "simulation_py", 1024)
# 30:34.418 - #1276
def leaderboard_Maze():
	def condition():
		return not (num_items(Items.Gold) >= 9863168)

# 1289.03 - When Simulated
# leaderboard_run(Leaderboards.Maze, "simulation_py", 1024)
# 21:29.908 - #1215
def leaderboard_MazeSpammer():
	def condition():
		return not (num_items(Items.Gold) >= 9863168)


# Hamiltonion Array Snake - with Shortcuts - Phase optimization
# Greed = 70, brute = 375
# Unable to simulate because of hat upgrades?
# leaderboard_run(Leaderboards.Dinosaur, "simulation_py", 2048)
# 17:25.618 - #303
def leaderboard_Dinos():
	def condition():
		return not (num_items(Items.Bone) >= 33488928)


# 66.52 - When Simulated
# leaderboard_run(Leaderboards.Cactus, "simulation_py", 512)
# 1:06.819 - #1291
def leaderboard_Cacti():
	# Starts with 1B Pumpkin, no need to plant anything else
	# Run Cacti
	def condition():
		return not (num_items(Items.Cactus) >= 33554432)


# 609.17 - When Simulated
# leaderboard_run(Leaderboards.Sunflowers, "simulation_py", 1024)
# 10:09.624 - #922
def leaderboard_Sunflowers():
	def condition():
		return not (num_items(Items.Power) >= 100000)


# 1561.29 - When Simulated
# leaderboard_run(Leaderboards.Pumpkins, "simulation_py", 1024)
# 25:20.846 - #1234
def leaderboard_Pumpkins():
	def condition():
		return not (num_items(Items.Pumpkin) >= 200000000)



# 2792.07 - When Simulated
# leaderboard_run(Leaderboards.Wood, "simulation_py", 1024)
# 46:02.122 - #779
def leaderboard_Wood():
	def condition():
		return not (num_items(Items.Wood) >= 10000000000)

# 3207.1 - When Simulated
# leaderboard_run(Leaderboards.Carrots, "simulation_py", 1024)
# 54:25.840 - #528
def leaderboard_Carrots():
	def condition():
		return not (num_items(Items.Carrot) >= 2000000000)

# 2213.24 - When Simulated
# leaderboard_run(Leaderboards.Hay, "simulation_py", 512)
# 37:42.715 - #1027
def leaderboard_Hay():
	def condition():
		return not (num_items(Items.Hay) > 2000000000)

#
#
#
def leaderboard_MazeSingle():
	def condition():
		return not (num_items(Items.Gold) >= 616448)

#
#
#
def leaderboard_CactiSingle():
	def condition():
		return not (num_items(Items.Cactus) >= 131072)

#
#
#
def leaderboard_SunflowersSingle():
	def condition():
		return not (num_items(Items.Power) >= 10000)

#
#
#
def leaderboard_PumpkinsSingle():
	def condition():
		return not (num_items(Items.Pumpkin) >= 10000000)

#
#
#
def leaderboard_WoodSingle():
	def condition():
		return not (num_items(Items.Wood) >= 500000000)

#
#
#
def leaderboard_CarrotsSingle():
	def condition():
		return not (num_items(Items.Carrot) >= 100000000)

# 
# 
# 
def leaderboard_HaySingle():
	def condition():
		return not (num_items(Items.Hay) >= 100000000)
	
############################
########### MAIN ###########
############################

from _main_ import *

############################
########### MAIN ###########
############################