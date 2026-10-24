# Global shorthand for all Item types
HAY = Items.Hay
WOOD = Items.Wood
CARROTS = Items.Carrot
PUMPKINS = Items.Pumpkin
CACTI = Items.Cactus
BONES = Items.Bone
WEIRD = Items.Weird_Substance
GOLD = Items.Gold
WATER = Items.Water
FERTILIZER = Items.Fertilizer
POWER = Items.Power

ITEMS = [
	HAY,
	WOOD,
	CARROTS,
	PUMPKINS,
	CACTI,
	BONES,
	WEIRD,
	GOLD,
	WATER,
	FERTILIZER,
	POWER
]

# Items to keep track of
COUNTABLE_ITEMS = [
	HAY,
	WOOD,
	CARROTS,
	PUMPKINS,
	CACTI,
	BONES,
	#WEIRD, # Used for Mazes constantly, dont worry
	GOLD,
	WATER,
	FERTILIZER,
	POWER
]

# Global shorthand for all Entity types
APPLE = Entities.Apple
BUSH = Entities.Bush
CACTUS = Entities.Cactus
CARROT = Entities.Carrot
DEAD_PUMP = Entities.Dead_Pumpkin
DINO = Entities.Dinosaur
GRASS = Entities.Grass
HEDGE = Entities.Hedge
PUMPKIN = Entities.Pumpkin
SUNFLOWER = Entities.Sunflower
TREASURE = Entities.Treasure
TREE = Entities.Tree

ENTITIES = [
	APPLE,
	BUSH,
	CACTUS,
	CARROT,
	DEAD_PUMP,
	DINO,
	GRASS,
	HEDGE,
	PUMPKIN,
	SUNFLOWER,
	TREASURE,
	TREE
	]
	
PLANTABLE_ENTITIES = [
	#BUSH, # Used as Maze marker, not to be planted
	CACTUS,
	#CARROT, #Used in PolyCulture
	#GRASS, # Used in PolyCulture
	PUMPKIN,
	SUNFLOWER,
	TREE # Used in PolyCulture
	]

# Subset of Plantable Entities that are worth watering
WATERABLE_ENTITIES = [
	#BUSH, # Used as Maze marker, not to be planted
	#CACTUS, # Takes a long time to sort, not worth the water
	#CARROT, # not planting carrots solo - polyculture
	GRASS, # Want to water the PolyCulture Area
	#PUMPKIN, # Only helps for short dead pumpkin searches
	#SUNFLOWER, # should be done growing by the time we get back
	#TREE # Not currently planting trees solo - polyculture
	]

NON_PLANTABLE_ENTITIES = [
	DEAD_PUMP,
	HEDGE,
	TREASURE
	]

# Plantable Entities with no Special Rules
BASIC_ENTITIES = [
	#BUSH, # Used as Maze marker, not to be planted
	CARROT,
	GRASS,
	TREE
	]

HARVESTABLE_ENTITIES = [
	BUSH,
	CACTUS,
	CARROT,
	# DEAD_PUMP, # Will always return False for can_harvest()
	GRASS,
	#HEDGE, # Will always return False for can_harvest()
	PUMPKIN,
	SUNFLOWER,
	#TREASURE, # Will always return False for can_harvest()
	TREE
	]

# Entities that would like a companion
# Return non-None when get_companion() is called
LONELY_ENTITIES = [
	BUSH,
	#CACTUS,
	#CARROT,
	#DEAD_PUMP,
	GRASS,
	HEDGE,
	#PUMPKIN,
	#SUNFLOWER,
	TREASURE,
	TREE
	]
	
# Global shorthand for all Ground types
GRASSLAND = Grounds.Grassland
SOIL = Grounds.Soil

# Map Entities to required Ground Type
SOILS = {
	BUSH      : GRASSLAND,
	CACTUS    : SOIL,
	CARROT    : SOIL,
	DEAD_PUMP : SOIL,
	GRASS     : GRASSLAND,
	HEDGE     : GRASSLAND,
	PUMPKIN   : SOIL,
	SUNFLOWER : SOIL,
	TREASURE  : GRASSLAND,
	TREE      : GRASSLAND
	}
	
# Map Entities to required Costs
COSTS = {
	BUSH      : [],
	CACTUS    : [],
	CARROT    : [],
	DEAD_PUMP : [],
	GRASS     : [],
	HEDGE     : [],
	PUMPKIN   : [],
	SUNFLOWER : [],
	TREASURE  : [],
	TREE      : []
	}
	
# Generate Costs
for entity in COSTS:
	cost = get_cost(entity)
	for item in cost:
		COSTS[entity].append((item, cost[item]))

# Map Entities to Max Grow Times
# Listed in Time order
TIMES = {
	TREE      : 8.4,
	SUNFLOWER : 8.4,
	CARROT    : 7.2,
	BUSH      : 4.8,
	PUMPKIN   : 3.8,
	CACTUS    : 1.0,
	GRASS     : 0.5,
	DEAD_PUMP : 0,
	HEDGE     : 0,
	TREASURE  : 0,
	} 	

# Sunflower Petal Limits
MIN_SUNFLOWER_PETALS = 7
MAX_SUNFLOWER_PETALS = 15

# Cactus Sizes
MIN_CACTUS_SIZE = 0
MAX_CACTUS_SIZE = 9