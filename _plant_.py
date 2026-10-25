
def plant_(entity):
	# Tills if necessary & Plants an entity
	# entity: entity to plant from Entites.*

	if entity == Entities.Carrot:
		if get_ground_type() != Grounds.Soil:
			till()

	plant(entity)