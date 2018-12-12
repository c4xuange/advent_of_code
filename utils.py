def get_input_data(filename):
	f = open(filename, "r")
	items = []
	line = f.readline()
	while line:
		items.append(line)
		line = f.readline()
	f.close()
	return items
