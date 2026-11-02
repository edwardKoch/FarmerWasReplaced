
def checkAndUnlock(toUnlock):
	cost = get_cost(toUnlock)
	for item in cost:
		if num_items(item) < cost[item]:
			return False

	unlock(toUnlock)
	return True