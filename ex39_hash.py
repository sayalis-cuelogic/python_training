import hashmap

states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')

cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'OR', 'Portland')
hashmap.set(cities, 'NY','New York')

print "NY state has : %s" % hashmap.get(cities,'NY')
print "CA state has : %s" % hashmap.get(cities,'CA')

print "Florida's abbreviation is : %s" % hashmap.get(states, 'Florida')
print "New York's abbreviation is : %s" % hashmap.get(states, 'New York')

print "California state has : %s" % hashmap.get(cities,hashmap.get(states,'California'))
print "Oregon state has : %s" % hashmap.get(cities,hashmap.get(states,'Oregon'))

print "-" * 20
hashmap.list(states)
print "-" * 20
hashmap.list(cities)
print "-" * 20
state = hashmap.get(states, 'Texas')

if not state:
	print "Sorry, no Texas.."

city = hashmap.get(cities, 'TX', 'Do not exist')
print "The city for the TX is %s" % city
