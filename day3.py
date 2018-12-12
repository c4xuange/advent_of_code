from utils import get_input_data

def process_claim(claim):
	split = claim.split(" ")
	offsets = split[2][:-1].split(",")
	id = int(split[0][1:])
	left_offset = int(offsets[0])
	top_offset = int(offsets[1])
	dimensions = split[3].strip().split("x")
	width = int(dimensions[0])
	height = int(dimensions[1])
	#print(left_offset, top_offset, width, height)
	return (id, left_offset, top_offset, width, height)

def preprocess_data(claims):
	max_width = 0
	max_height = 0
	processed_claims = []
	for claim in claims:
		id, lo, to, w, h = process_claim(claim)
		if lo + w > max_width:
			max_width = lo + w
		if to + h > max_height:
			max_height = to + h
		processed_claims.append((id, lo, to, w, h))
	return max_width, max_height, processed_claims

def get_overlap_grid(max_w, max_h, claims):
	grid = [[0 for i in range(max_w)] for i in range(max_h)]
	for claim in claims:
		id, lo, to, w, h = claim
		for i in range(to, to+h):
			for j in range(lo, lo+w):
				grid[i][j] += 1
	return grid

def get_overlap_count(grid):
	count = 0
	num_rows, num_cols = len(grid), len(grid[0])
	for row in range(num_rows):
		for col in range(num_cols):
			if grid[row][col] >= 2:
				count += 1
	return count

def get_grid_sum(grid, lo, to, w, h):
	total = 0
	for row in range(to, to + h):
		row_sum = sum(grid[row][lo:lo+w])
		total += row_sum
	return total

def get_nonoverlap_id(grid, claims):
	for claim in claims:
		id, lo, to, w, h = claim
		if get_grid_sum(grid, lo, to, w, h) == w * h:
			return id 

if __name__ == "__main__":
	claims = get_input_data("day3input.txt")
	max_w, max_h, processed_claims = preprocess_data(claims)
	grid = get_overlap_grid(max_w, max_h, processed_claims)
	
	#part 1
	print(get_overlap_count(grid))
	
	#part 2
	print(get_nonoverlap_id(grid, processed_claims))
