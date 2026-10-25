# Move to specific coordinates
def moveTo(coord):
	# coord: Tuple for coordinates (x, y)
	dX = (get_pos_x() - coord[0])
	dY = (get_pos_y() - coord[1])

	for x in range(dX):
		move(East)

	for y in range(dY):
		move(North)