class parent():
	def __init__(self, name):
		self.name = name

	def print_name(self):
		print(self.name)

Vitya = parent("Vitya")
Vitya.print_name()
#Vitya.name = "Oleg"
#Vitya.print_name()

class child(parent):
	def print_name(self):
		print("My name is", self.name)
Vitalya = child("Vitalya")
Vitalya.print_name()
