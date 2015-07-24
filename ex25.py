def break_words(stuff):
	words = stuff.split(' ')
	return words 

def sort_words(stuff):
	return sorted(stuff)

def print_first_word(stuff):
	word = stuff.pop(0)
	return word

def print_last_word(stuff):
	word = stuff.pop(-1)
	return word

def sort_sentence(stuff):
	words = break_words(stuff)
	return sort_words(words)

def print_first_and_last_word(stuff):
	words = break_words(stuff)
	word1 = print_first_word(words)
	word2 = print_last_word(words)
	return word1, word2

def print_first_and_last_sorted(stuff):
	words = break_words(stuff)
	sorted_words = sort_words(words)
	word1 = print_first_word(sorted_words)
	word2 = print_last_word(sorted_words)
	return word1, word2
	