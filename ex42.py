
class Animal(object):
	pass

class  Dog(Animal):

	def __init__(self, name):
		self.name = name
		print name

class  Cat(Animal):
	def __init__(self, name):
		self.name = name
		print name

class Person(object):
	def __init__(self, name):
		self.name = name
		print "Emp name : ", name

class  Empoylee(Person):
	def __init__(self, name, salary):
		super(Empoylee,self).__init__(name)
		self.salary = salary
		print "salary : ", salary
		
monty = Dog("Monty")
lila = Cat("Lila")

sayali = Empoylee("Sayali","25000")


