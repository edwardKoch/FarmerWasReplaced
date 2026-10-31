# Move to specific coordinates
def moveTo(coord):
	# coord: Tuple for coordinates (x, y)
	x = get_pos_x()
	y = get_pos_y()


	dX = 0
	dY = 0

	ns = North
	ew = East

	if x > coord[0]:
		dX = (x - coord[0])
		ew = West
	else:
		dX = (coord[0] - x)
		ew = East


	if y > coord[1]:
		dY = (y - coord[1])
		ns = South
	else:
		dY = (coord[1] - y)
		ns = North

	for x in range(dX):
		move(ew)

	for y in range(dY):
		move(ns)