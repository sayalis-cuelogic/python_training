people = 30
cars = 40
trucks = 15

if cars > people :
	print "We should take the cars"

elif cars < people :
	print "We should not take the cars"
else :
	print "We can't decide."

if cars < trucks :
	print "That's too many trucks.."
elif cars > trucks :
	print "Maybe We could take trucks.."
else :
	print "Still We can't decide."

if people > trucks :
	print "Alright,Let's just take trucks.."
else :
	print "Alright,let's stay at home.."

