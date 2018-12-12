from utils import get_input_data

def calc_freq(freqs):
	acc_freq = 0
	for freq in freqs:
		num = int(freq[1:])
		if freq[0] == "+":
			acc_freq += num
		else:
			acc_freq -= num
	print(acc_freq)

def get_first_repeated_freq(freqs):
	i = 0
	len_freq = len(freqs)
	seen_freqs = set([0])
	acc_freq = 0
	while True:
		curr_ind = i % len_freq
	        freq = freqs[curr_ind]
		num = int(freq[1:])
                if freq[0] == "+":
                        acc_freq += num
                else:
                        acc_freq -= num
		if acc_freq in seen_freqs:
			print(acc_freq)
			return
		seen_freqs.add(acc_freq)
		i += 1
	
if  __name__ == "__main__":
	freqs = get_input_data("day1input.txt")
	# part 1
	calc_freq(freqs)
	# part 2
	get_first_repeated_freq(freqs)
	
		
