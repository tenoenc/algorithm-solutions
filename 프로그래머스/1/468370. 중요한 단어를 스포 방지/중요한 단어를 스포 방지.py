from collections import Counter

def solution(message, spoiler_ranges):
	answer = 0
	message = message + " "
	words = Counter()
	ranges = []
	spoiler_words = set()
	whead = 0
	is_spoiler = False
	for i in range(len(message)):
		if not message[i] == ' ':
			for start, end in spoiler_ranges:
				if start <= i <= end:
					is_spoiler = True
					break
		else:
			if not is_spoiler:
				words[message[whead:i]] += 1
			ranges.append((whead, i))
			whead = i+1
			is_spoiler = False
	for start, end in ranges:
		spoiler_word = message[start:end]
		if spoiler_word not in spoiler_words and spoiler_word not in words:
			words[spoiler_word] += 1
			spoiler_words.add(spoiler_word)
			answer += 1

	return answer