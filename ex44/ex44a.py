
class parent(object):
	def implicit(self,name):
		self.name = name
		print "Parent Implicit()",name

class child(parent):
		pass

##############################################
dad = parent()
son = child()

dad.implicit("Rajendra")
son.implicit("Arun")
