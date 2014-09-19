def word_frequency(words):
	print """Returns frequency of each word given a list of words."""
	frequency = {}
	for w in words:
		frequency[w] = frequency.get(w, 0) + 1
	return frequency



print word_frequency("sujith")
