x = 78

class StringVar:
	def __init__ (self, stroke):
		self.stroke = stroke

		if isinstance(stroke, str):
			print("It's a string")
		else:
#			print("It's not a string")
			return None


	def set(self, stroke):
		self.stroke = str(stroke)
		self.stroke = "Hello, " + self.stroke
		print(self.stroke)


#	def get():


a = StringVar(x) 
b = StringVar('tyu')
a.set("Max")
#print(StringVar.set)
#print(a.set)
#print(a.__dict__)
a.set(89)
b.stroke = 10
print(b.__dict__)
b.set("Max")
print(b.__dict__)