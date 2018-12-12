from utils import get_input_data

PATTERN_LEN = 5

def get_next_state(input_state, patterns):
	left_padding, right_padding = "", ""
	first_pot_offset, curr_pot = -1, 0
	shift_right = 0
	while first_pot_offset < 0:
		if input_state[curr_pot] == "#":
			first_pot_offset = curr_pot
		curr_pot += 1
	left_padding = "."*(4 - first_pot_offset)

	last_pot_offset, curr_pot_offset = -1, 0
	while last_pot_offset < 0:
		if input_state[(-1) - curr_pot_offset] == "#":
			last_pot_offset = curr_pot_offset
		curr_pot_offset += 1
	right_padding = "."*(4 - last_pot_offset)

	padded_state = left_padding + input_state + right_padding
	if first_pot_offset > 4:
		padded_state = padded_state[(first_pot_offset - 4):]
		shift_right = first_pot_offset - 4

	state_len = len(padded_state)
	next_state = ["."]*state_len
	for i in range(state_len - PATTERN_LEN + 1):
		for pattern in patterns:
			if padded_state[i:i+PATTERN_LEN] == pattern[0]:
				next_state[i+2] = pattern[1]
				break
	return len(left_padding) - shift_right, "".join(next_state)

def get_state(input_state, patterns, state_num, total_lp):
	if state_num == 0:
		return total_lp, input_state
	lp, next_state = get_next_state(input_state, patterns)
	return get_state(next_state, patterns, state_num-1, total_lp + lp)

def get_pot_sum(state, total_lp):
	total = 0
	for i in range(len(state)):
		if state[i] == "#":
			total += (i - total_lp)
	return total

def get_large_pot_sum(initial_state, patterns, total_lp):
	acc = 0
	curr_state, curr_lp = initial_state, total_lp
	while acc < 5000:
		new_lp, new_state = get_state(curr_state, patterns, 100, curr_lp)
		curr_state, curr_lp = new_state, new_lp
		print(get_pot_sum(curr_state, curr_lp))
		acc += 100
	return get_pot_sum(curr_state, curr_lp)

if __name__ == "__main__":
	data = get_input_data("day12input.txt")
	initial_state = data[0].split(": ")[1].strip()
	patterns = []
	for pattern in data[2:]:
		split = pattern.strip().split(" => ")
		patterns.append((split[0], split[1]))

	#part 1
	lp, state20 = get_state(initial_state, patterns, 20, 0)
	print(get_pot_sum(state20, lp))

	#part 2
	# print(get_large_pot_sum(initial_state, patterns, 0))
	# after a while, the pot sum increments by 6700 (by observation)
	print(50000000000/100*6700)