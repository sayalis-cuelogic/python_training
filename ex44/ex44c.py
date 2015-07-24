
class Parent(object):
	def altered(self):
		print "Parent altered()"

class Child(Parent):
	def altered(self):
		print "Before Parent altered"
		super(Child,self).altered()
		print "After Parent altered"

##############################################
dad = Parent()
son = Child()

dad.altered()
son.altered()
