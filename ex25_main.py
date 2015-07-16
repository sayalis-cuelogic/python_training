import ex25
sentence = "Hi All good things come to those who wait."
words = ex25.break_words(sentence)
print "\nList of splited words : \n %s" % words

sorted_words = ex25.sort_words(words)
print "\nList of sorted words : \n %s" % sorted_words

first_word = ex25.print_first_word(words)
print "\n First word from a List: \n %s" % first_word

last_word = ex25.print_last_word(words)
print "\nLast word from a List : \n %s" % last_word

first_word = ex25.print_first_word(sorted_words)
print "\nFirst word from a sorted List: \n %s" % first_word

last_word = ex25.print_last_word(sorted_words)
print "\nLast word from a sorted List : \n %s" % last_word

sorted_sentence = ex25.sort_sentence(sentence)
print "\nList of sorted words from a sentence: \n %s" % sorted_sentence

print "\n First word from a sentence:  %s and last word is : %s" % ex25.print_first_and_last_word(sentence)

print "\n First word from a sorted sentence:  %s and last word is : %s" % ex25.print_first_and_last_sorted(sentence)
