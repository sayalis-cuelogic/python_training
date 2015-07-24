class Parent(object):
	def implicit(self):
		print "Parent implicit()"

	def override(self):
		print "parent override...."

	def altered(self):
		print "Parent altered()"

class  Child(Parent):
	def override(self):
		print "child override...."

	def altered(self):
		print "Before Parent altered"
		super(Child,self).altered()
		print "After Parent altered"

##############################################
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
