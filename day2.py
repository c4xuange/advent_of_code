from utils import get_input_data

def get_two_three_counts(word):
	letter_count = {}
	for letter in word:
		if letter not in letter_count:
			letter_count[letter] = 0
		letter_count[letter] += 1
	exactly_two = 0
	exactly_three = 0
	for letter in letter_count:
		if letter_count[letter] == 2:
			exactly_two = 1
		elif letter_count[letter] == 3:
			exactly_three = 1
	return (exactly_two, exactly_three)

def get_product(labels):
	twos, threes = 0, 0
	for label in labels:
		two, three = get_two_three_counts(label)
		twos += two
		threes += three
	return twos * threes

def get_edit_distance(w1, w2):
	if len(w1) != len(w2):
		print("Invalid inputs: varying length")
		return
	distance = 0
	for i in range(len(w1)):
		if w1[i] != w2[i]:
			distance += 1
	return distance

def find_edit_distance_one(labels):
	len_labels = len(labels)
	for i in range(len_labels):
		for j in range(i, len_labels):
			if get_edit_distance(labels[i], labels[j]) == 1:
				return (labels[i], labels[j])

if __name__ == "__main__":
	labels = get_input_data("day2input.txt")
	# part 1
	print(get_product(labels))
	# part 2
	word1, word2 = find_edit_distance_one(labels)
	common_letters = ""
	for i in range(len(word1)):
		if word1[i] == word2[i]:
			common_letters += word1[i]
	print(common_letters)
