import random
class Hangman():

	def __init__(self):
		self.health = 10
		self.words = ["lightning" , "programm", "batman", "book", 'confusing', 'conscience','moral', 'right', 'conscious', 'responding', 'surroundings', 'adjective', 'once', 'clear', 'hurdle', 'sure', 'that', 'science', 'appearance', 'your', 'spell']
		self.word=self.words[random.randrange(21)]
		self.len_word=len(self.word)
		self.test = False
		self.used_letters = ""
		self.win_word = []

		for i in range(len(self.word)):
			self.win_word += "_"
		

	def print_mas(mas):	
		str = ""
		for sym in self.mas:
			str +=sym
		print(str)

	def Menu(self):
		print("print <<play>> to Play\nprint <<exit>> to Quit" )
		self.choice = input()
		if self.choice == "play":
			Hangman().run()
		elif self.choice == "exit":
			exit(0)
		pass

	def run(self):
		print(self.win_word)
		while self.len_word != 0 and self.health != 0:
			self.test = False
			while True:
				letter = input("\nwrite your letter ")
				if letter in self.used_letters or len(letter)>1:
					print("\nUsed or longer than 1 symbol, try again!")
				else:
					self.used_letters += letter
					break
			count=0
			for i in self.word:
				if letter in i:
					self.len_word -= 1
					self.test=True
					self.win_word[count]=letter
				count+=1
				
			if not self.test:
				self.health -= 1
				print("WRONG")
				print(self.win_word)
			else:
				print("RIGHT")
				print(self.win_word)
			if self.health == 9:
				print("\n   |     |\n___|_____|___")
			elif self.health == 8:
				print("\n   _______\n   |     |\n___|_____|___") 
			elif self.health == 7:
				print("\n      |      \n      |      \n      |      \n      |      \n   ___|___         \n   |     |\n___|_____|___")
			elif self.health == 6:
				print("\n ______________\n|     |\n|     |\n      |      \n      |      \n      |      \n      |      \n   ___|___         \n   |     |\n___|_____|___")
			elif self.health == 5:
				print("\n_________________\n|     |         |\n|     |         |\n      |         |\n      |         |\n      |      \n      |      \n      |      \n      |      \n   ___|___         \n   |     |\n___|_____|___")
			elif self.health == 4:
				print("\n_________________\n|     |         |\n|     |         |\n      |         |\n      |       {*_*}\n      |      \n      |      \n      |      \n   ___|___         \n   |     |\n___|_____|___")
			elif self.health == 3:
				print("\n_________________\n|     |         |\n|     |         |\n      |         |\n      |       {*_*}\n      |        | |\n      |       |   |\n      |      |_____|\n   ___|___         \n   |     |\n___|_____|___")
			elif self.health == 2:
				print("\n_________________\n|     |         |\n|     |         |\n      |         |\n      |       {*_*}\n      |        | |\n      |  #----|   |----#\n      |      |_____|\n   ___|___         \n   |     |\n___|_____|___")
			elif self.health == 1:
				print("\n_________________\n|     |         |\n|     |         |\n      |         |\n      |       {*_*}\n      |        | |\n      |  #----|   |----#\n      |      |_____|\n   ___|___    |   \n   |     |    |   \n___|_____|___ ^   ")

		if(self.len_word == 0):
			print("\nWINNER!!! WORD WAS", self.word.upper())
			print("Your health = ", self.health)
		else:
			print("\nYOU LOSE! TRY AGAIN!")
			print("Your health = ", self.health)
			print("\n_________________\n|     |         |\n|     |         |\n      |         |\n      |       {*_*}\n      |        | |\n      |  #----|   |----#\n      |      |_____|\n   ___|___    |   |\n   |     |    |   |\n___|_____|___ ^   ^")





if __name__ == '__main__':
	Hangman().Menu()
	input("press anything to exit")