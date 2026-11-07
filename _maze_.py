from _move_ import *


def rightWallMethod():
	# Follow the right wall until Treasure is found
		
	while get_entity_type() != Entities.Treasure:
		
		# If somehow we are out of the maze
		if get_entity_type() != Entities.Hedge:
			break

		# Follow the Right Wall
		if can_move(getRight()):
			turnRight()
			moveForward()
		elif can_move(getForward()):
			moveForward()
		else:
			turnRight()
			turnRight()

	# Treasure was found
	harvest()


def leftWallMethod():
	# Follow the left wall until Treasure
		
	while get_entity_type() != Entities.Treasure:
		
		# If somehow we are out of the maze
		if get_entity_type() != Entities.Hedge:
			break

		# Follow the Left Wall
		if can_move(getLeft()):
			turnLeft()
			moveForward()
		elif can_move(getForward()):
			moveForward()
		else:
			turnLeft()
			turnLeft()

	# Treasure was found
	harvest()
			
def createAndSolveMaze(x, y, size):
	# Generate the Maze, Find the Treasure, harvest & Destroy Maze

	moveTo((x, y))
	# Clear the Square
	harvest()
	plant(Entities.Tree)
	use_item(Items.Fertilizer)
	use_item(Items.Water)

	# Get cost of generating the maze
	cost = size * get_cost(Entities.Hedge)[Items.Weird_Substance]

	while num_items(Items.Weird_Substance) < cost * 4:
		if can_harvest():
			harvest()
			plant(Entities.Grass)
			use_item(Items.Fertilizer)
			use_item(Items.Water)

	# Generate the Maze
	harvest()
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, cost)

	# Solve the Maze
	rightWallMethod()

def createAndSolveMazes(x, y, size, num):
	# Generate and solve a number of mazes

	for i in range(num):
		createAndSolveMaze(x, y, size)


def rightWallMethodMulti():
	# Follow the right wall until Treasure is found
	# Spawn helpers every 'get_world_size()' steps
		
	count = 0
	helpCount = get_world_size()
	minion = None
	while get_entity_type() != Entities.Treasure:
		
		# If somehow we are out of the maze
		if get_entity_type() != Entities.Hedge:
			break

		# Follow the Right Wall
		if can_move(getRight()):
			turnRight()
			moveForward()
		elif can_move(getForward()):
			moveForward()
		else:
			turnRight()
			turnRight()

		count += 1
		if count > helpCount and minion == None:
			minion = spawn_drone(leftWallMethodMulti)

	# Treasure was found
	harvest()


def leftWallMethodMulti():
	# Follow the left wall until Treasure
	# Spawn helpers every 'get_world_size()' steps
		
	count = 0
	helpCount = get_world_size()
	minion = None
	while get_entity_type() != Entities.Treasure:
		
		# If somehow we are out of the maze
		if get_entity_type() != Entities.Hedge:
			break

		# Follow the Left Wall
		if can_move(getLeft()):
			turnLeft()
			moveForward()
		elif can_move(getForward()):
			moveForward()
		else:
			turnLeft()
			turnLeft()

		count += 1
		if count > helpCount and minion == None:
			minion = spawn_drone(rightWallMethodMulti)

	# Treasure was found
	harvest()

def createAndSolveMazeMulti(x, y, size):
	# Generate the Maze, Find the Treasure, harvest & Destroy Maze
	# Use multiple Drones

	moveTo((x, y))
	# Clear the Square
	harvest()
	plant(Entities.Tree)
	use_item(Items.Fertilizer)
	use_item(Items.Water)

	# Get cost of generating the maze
	cost = size * get_cost(Entities.Hedge)[Items.Weird_Substance]

	while num_items(Items.Weird_Substance) < cost * 4:
		if can_harvest():
			harvest()
			plant(Entities.Grass)
			use_item(Items.Fertilizer)
			use_item(Items.Water)

	# Generate the Maze
	harvest()
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, cost)

	# Solve the Maze
	spawn_drone(leftWallMethodMulti)
	rightWallMethodMulti()


def createAndSolveMazesMulti(x, y, size, num):
	# Generate and solve a number of mazes use mulitple drones

	for i in range(num):
		createAndSolveMazeMulti(x, y, size)