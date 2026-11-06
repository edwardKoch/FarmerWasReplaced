from _move_ import *

def rawHamiltonSnake():
	# Play snake with a raw hamiltionian path

	dim = get_world_size() - 1

	# Start in the Bottom Left
	moveTo((0,0))

	# Equip Dino Hat - Spawns Apple underneath
	change_hat(Hats.Dinosaur_Hat)

	# Go until we hit our own tail
	ableToMove = True
	while ableToMove:

		# Move to the top left corner
		while ableToMove:
			ableToMove = move(North)

		# move to the far right
		ableToMoveE = True
		while ableToMoveE:
			ableToMove = move(East)
			ableToMoveE = ableToMove

		# move down one
		ableToMove = move(South)

		# Move back to the left column - 1
		ableToMoveW = True
		while ableToMoveW and get_pos_x() > 1:
			ableToMove = move(West)
			ableToMoveW = ableToMove

		# move down one
		ableToMove = move(South)

		# If we have completed a full cycle, try again
		if get_pos_x() == 1 and get_pos_y() == 0:
			ableToMove = move(West)

	# Equip Default hat- Harvests Tail
	change_hat(Hats.Straw_Hat)

def updatePos(curX, curY, dir):
	# Update the CurX/Y
	if dir == South: 
		curY -= 1
	elif dir == North: 
		curY += 1
	elif dir == East: 
		curX += 1
	elif dir == West: 
		curX -= 1

	return curX, curY

def dynamicHamiltonSnake():
	# Play snake with a dynamic hamiltionian path
	# Calculates direciton based on current coords
	
	dim = get_world_size() - 1
	
	# Start in the Bottom Left
	moveTo((0,0))
	curX, curY = 0,0

	# Equip Dino Hat - Spawns Apple underneath
	change_hat(Hats.Dinosaur_Hat)

	appleX, appleY = measure()

	ableToMove = True
	while ableToMove:

		# Calculate constants
		curYMod2 = curY % 2
		
		if curX == 0 and curY != dim:
			ableToMove = move(North)
			curX, curY = updatePos(curX, curY, North)

		elif (curX == 1 and curYMod2 == 0) or (curX == dim and curYMod2 != 0):
			# Handle end of path wrap around
			if curY == 0:
				ableToMove = move(West)
				curX, curY = updatePos(curX, curY, West)
			else:
				ableToMove = move(South)
				curX, curY = updatePos(curX, curY, South)

		else:
			if curYMod2 == 0:
				ableToMove = move(West)
				curX, curY = updatePos(curX, curY, West)
			else:
				ableToMove = move(East)
				curX, curY = updatePos(curX, curY, East)

		if curX == appleX and curY == appleY and measure() != None:
			appleX, appleY = measure()

	# Equip Default hat- Harvests Tail
	change_hat(Hats.Straw_Hat)