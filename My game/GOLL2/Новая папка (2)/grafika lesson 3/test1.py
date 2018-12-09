class Father:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def say_hello(self):
		print("Hello! My name is", self.name)

class Son(Father):
	def say_goodbye(self):
		print("Goodbye! My name is", self.name)

father = Father("Olkan", 45)
father.say_hello()
son = Son("Olkan's son", 19)
son.say_hello()
son.say_goodbye()

