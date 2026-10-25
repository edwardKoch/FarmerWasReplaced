
def checkUnlock(unlock):
	cost = get_cost(unlock)
	for dic in cost:
		for item in dic:
			if num_items(item) < dic[item]:
				return False

	return True

def checkIncrementalUnlocks():
	if checkUnlock(Unlocks.Speed):
		unlock(Unlocks.Speed)

	if checkUnlock(Unlocks.Expand):
		unlock(Unlocks.Expand)