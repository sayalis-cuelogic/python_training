states = {
	'Oregon' : 'OR',
	'Florida' : 'FL',
	'California' : 'CA',
	'New York' : 'NY',
	'Michigan' : 'MI',
	'Maharashtra' : 'MH'
}

cities = {
	'CA' : 'San Francisco',
	'MI' : 'Detroit',
	'FL' : 'Jacksonville',
	'MH' : 'Pune'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print "_" * 20
print "NY state has : ", cities['NY']
print "OR state has :", cities['OR']

print "Michigan's abbreviation is ", states['Michigan']
print "Florida's abbreviation is ", states['Florida']

print "_" * 20
for state, abbrev in states.items():
	print "%s is abbreviated as %s" % (state, abbrev)

print "_" * 20
for abbrev, city in cities.items():
	print "%s has %s city" % (abbrev, city)

print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
