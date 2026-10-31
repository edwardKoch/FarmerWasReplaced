
def plant_(entity):
	# Tills if necessary & Plants an entity
	# entity: entity to plant from Entites.*

	if entity == Entities.Carrot:
		if get_ground_type() != Grounds.Soil:
			till()

	plant(entity)

def plantTreeBush_(x, y):
	toPlant = Entities.Bush
	if y % 2 == 0 and x % 2 == 0:
		toPlant = Entities.Tree
	elif y % 2 == 1 and x % 2 == 1:
		toPlant = Entities.Tree

	plant_(toPlant)