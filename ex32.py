count = [1, 2, 3, 4, 5]
fruits = ['Apple', 'Mango', 'Banana', 'Orange', 'Pears']
change = [1, 'Sayali', 2, 'Sonali', 3, 'Deepa', 4, 'Shruti']

for number in count:
	print "This is the count : %d " % number

for fruit in fruits:
	print "A fruit is %s" % fruit

for i in change:
	print "I got : %r" % i

elements = []

print "Adding elements..."

for  e in range(1,6):
	print "Enter %d element for the list" % e
	data = raw_input()
	elements.append(data)

for e in elements:
	print "element is %r" % e
	