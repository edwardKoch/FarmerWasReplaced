def sSleep(seconds):
	start = get_time()
	while get_time() - start < seconds:
		do_a_flip()