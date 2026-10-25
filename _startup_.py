from _move_ import *

####################
# STARTUP PHASE 
# Unlock Basic abilities & Square Farm
####################

moveTo((0,0))

# Get 20 Hay for Speed 1
while num_items(Items.Hay) < 20:
	harvest()
# TODO Unlock Speed 1

# Get 30 Hay for Expand 1 (1x3)
while num_items(Items.Hay) < 30:
	harvest()
# TODO Unlock Expand 1

# Get 50 Hay for Planting (Bush)
while num_items(Items.Hay) < 50:
	move(North)
	if can_harvest():
		harvest()
# TODO Unlock Plant 1

# Get 50 Wood for Carrots
while num_items(Items.Wood) < 50:
	move(North)
	if can_harvest():
		harvest()
		plant(Entities.Bush)
# TODO Unlock Carrots

# Get 50 Wood for Expand 2 (3x3)
while num_items(Items.Wood) < 50:
	move(North)
	if can_harvest():
		harvest()
		plant(Entities.Bush)
# TODO  Unlock Expand 2

