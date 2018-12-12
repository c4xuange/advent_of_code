from utils import get_input_data

def preprocess_data(data):
	processed = []
	min_x, max_x, min_x_ind, max_x_ind = float("inf"), -float("inf"), -1, -1
	for i in range(len(data)):
		datum = data[i]
		x_coord = int(datum[10:16])
		if x_coord < min_x:
			min_x = x_coord
			min_x_ind = i
		elif x_coord > max_x:
			max_x = x_coord
			max_x_ind = i
		y_coord = int(datum[18:24])
		x_vel = int(datum[36:38])
		y_vel = int(datum[40:42])
		processed.append((x_coord, y_coord, x_vel, y_vel))
	return min_x_ind, max_x_ind, processed

def condense_points(min_x_ind, max_x_ind, data, threshold, mc = 0):
	move_count = mc
	if move_count == 0:
		max_x, max_vel = data[max_x_ind][0], data[max_x_ind][2]
		min_x, min_vel = data[min_x_ind][0], data[min_x_ind][2]
		while max_x - min_x > threshold:
			max_x += max_vel
			min_x += min_vel
			move_count += 1
	condensed = []
	for datum in data:
		x, y, x_vel, y_vel = datum
		x += move_count * x_vel
		y += move_count * y_vel
		condensed.append((x, y, x_vel, y_vel))
	return move_count, condensed

def get_grid(data, show = False):
	min_x = min(data, key = lambda t: t[0])
	max_x = max(data, key = lambda t: t[0])
	min_y = min(data, key = lambda t: t[1])
	max_y = max(data, key = lambda t: t[1])
	width = max_x[0] - min_x[0]
	height = max_y[1] - min_y[1]
	left_offset = 0 - min_x[0]
	top_offset = 0 - min_y[1]
	if show:
		display_grid(data, width, height, left_offset, top_offset)
	return width

def display_grid(data, w, h, lo, to):
	grid = [["." for i in range(w+1)] for j in range(h+1)]
	for datum in data:
		x, y, x_vel, y_vel = datum
		grid[y+to][x+lo] = "$"
	for row in grid:
		print("".join(row))

if __name__ == "__main__":
	data = get_input_data("day10input.txt")
	mnx, mxx, processed_data = preprocess_data(data)
	# threshold here is 366
	# each datum represents a point, they all have to converge to create words
	# since there are only 366 data points, they can be at most that far apart
	# (realistically, much less than that)
	# so let's condense our grid greatly first, before plotting
	total_mc, condensed = condense_points(mnx, mxx, processed_data, len(data))

	# part 1
	last_width, most_condensed = get_grid(condensed), condensed
	while True:
		mc, condensed = condense_points(None, None, condensed, None, 1)
		curr_width = get_grid(condensed)
		if curr_width < last_width:
			last_width, most_condensed = curr_width, condensed
			total_mc += mc
		else:
			break
	get_grid(most_condensed, True)
	# part 2
	print(total_mc)
