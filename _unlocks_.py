
def checkAndUnlock(toUnlock):
	cost = get_cost(toUnlock)
	for dic in cost:
		for item in dic:
			if num_items(item) < dic[item]:
				return False

	unlock(toUnlock)
	return True