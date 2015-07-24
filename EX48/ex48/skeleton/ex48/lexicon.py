direction=('north','south','east')
verbs=('go','kill','eat','run')
nouns=('bear','princess','honey')
stop=('the','in','of')

def scan(words):
	word=words.split(' ')
	result=[]
	for sword in word:
		if sword in direction:
			result.append(('direction',sword))
		elif sword in verbs:
			result.append(('verb',sword))
		elif sword in nouns:
			result.append(('noun',sword))
		elif sword.isdigit():
			result.append(('number',int(sword)))
		elif sword in stop:
			result.append(('stop',sword))
		else:
			result.append(('error',sword))
	return result
	