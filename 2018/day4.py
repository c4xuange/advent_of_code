from utils import get_input_data

def preprocess_data(events):
	split_events = []
	for event in events:
		split = event.split("]")
		time = split[0][1:]
		desc = split[1].strip()
		split_events.append((time, desc))
	sorted_events = sorted(split_events, key=lambda tup: tup[0])
	return sorted_events

if __name__ == "__main__":
	events = get_input_data("day4input.txt")
	sorted_events = preprocess_data(events)
	print(sorted_events[:20])	
