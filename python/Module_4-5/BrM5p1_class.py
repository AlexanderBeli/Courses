class ClassName():
	attr1 = 42
	attr2 = 'some info'

	def do_cmth(self):
		print(self.attr2)


a = ClassName()
a.attr2
a.do_cmth()

class Point():


	def __init__(self, x, y):
		self.x = x
		self.y = y


	def distance(self):
		print((self.x ** 2 + self.y ** 2) ** (1/2))


p1 = Point(2, -2)
p1.distance()