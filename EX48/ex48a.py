def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return "It's string please enter number"

print "enter data "
num = raw_input(">")
print convert_number(num)

print "enter data "
num1 = raw_input(">")
print convert_number(num1)