from _move_ import *
from _unlocks_ import *

####################
# STARTUP PHASE 
# Unlock Basic abilities & Square Farm
####################

moveTo((0,0))
clear()

# Get 20 Hay for Speed 1
while num_items(Items.Hay) < 20:
	harvest()
	do_a_flip()
checkAndUnlock(Unlocks.Speed)

# Get 30 Hay for Expand 1 (1x3)
while num_items(Items.Hay) < 30:
	harvest()
	do_a_flip()
checkAndUnlock(Unlocks.Expand)

# Get 50 Hay for Planting (Bush)
while num_items(Items.Hay) < 50:
	move(North)
	if can_harvest():
		harvest()
checkAndUnlock(Unlocks.Plant)

# Get 50 Wood for Carrots
while num_items(Items.Wood) < 50:
	move(North)
	if can_harvest():
		harvest()
		plant(Entities.Bush)
checkAndUnlock(Unlocks.Carrots)

# Get 50 Wood for Expand 2 (3x3)
while num_items(Items.Wood) < 50:
	move(North)
	if can_harvest():
		harvest()
		plant(Entities.Bush)
checkAndUnlock(Unlocks.Expand)

