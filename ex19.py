
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheese !!!" % cheese_count
	print "You have %d boxes of crackers !!!" % boxes_of_crackers
	print "Man that's enough for party !!! \n"

print "We just give numbers to function directly"
cheese_and_crackers(20,30)

print "We can use variables from your script"
amount_of_cheese = 30
amount_of_crackers = 40
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can to math inside too "
cheese_and_crackers(15 + 20 , 20 + 5)

print "We can combine two, variables and math"
cheese_and_crackers(amount_of_cheese + 10 , amount_of_crackers + 5)
