class Sentence(object):

    def __init__(self, subject, verb, obj):
        # remember we take ('noun','princess') tuples and convert them
        self.subject = subject
        self.verb = verb
        self.object = obj

    def peek(self, word_list):
    	if word_list:
        	word = word_list[0]
        	return word[0]
    	else:
        	return None

    def match(self, word_list, expecting):
    	if word_list:
        	word = word_list.pop(0)

        	if word[0] == expecting:
        		return word
        	else:
        		return None
    	else:
    		return None

    def skip(self, word_list, word_type):
    	while self.peek(word_list) == word_type:
        	self.match(word_list, word_type)

    def parse_verb(self, word_list):
    	self.skip(word_list, 'stop')

    	if self.peek(word_list) == 'verb':
        	return self.match(word_list, 'verb')
    	else:
        	print "Expected a verb next."

    def parse_object(self, word_list):
    	self.skip(word_list, 'stop')
    	next_word = self.peek(word_list)

    	if next_word == 'noun':
        	return self.match(word_list, 'noun')
    	elif next_word == 'direction':
        	return self.match(word_list, 'direction')
    	else:
        	print "Expected a noun or direction next."

    def parse_subject(self, word_list):
    	#self.skip(word_list, 'stop')
    	#next_word = self.peek(word_list)
    	for next_word in word_list:
    		if next_word == 'noun':
        		return self.match(word_list, 'noun')
    		elif next_word == self.verb:
        		return ('noun', 'player')
    		else:
        		print "Expected a verb next."

    def parse_sentence(self, word_list):
    	print word_list
    	subj = self.parse_subject(word_list)
    	print subj
    	verb = self.parse_verb(word_list)
    	print verb
    	obj = self.parse_object(word_list)

    	#return Sentence(subj, verb, obj)
    	return subj, verb, obj

objects = ('north','south','east')
verbs=('go','kill','eat','run')
subject=('bear','player','honey')

res = Sentence(subject,verbs,objects)
s1 = "verb player run north"
s2 = s1.split(' ')
res1 = res.parse_sentence(s2)
print "Result is : ",res1