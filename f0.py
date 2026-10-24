from motion_py import *
from farmTypes_py import *
from farming_py import *
from workers_py import *
from time_py import *

clear()

PLOTS[PUMPKIN] = []
for x in range(get_world_size()):
    for y in range(get_world_size()):
        PLOTS[PUMPKIN].append((x, y))

calculateRowsCols(PUMPKIN)

def condition():
    return True

pumpkinWorker(condition)