BLUE = (0, 0, 255)
class window():
	def load_map(self):
		file = open("map", 'r')
		for i, line in enumerate(file): # y
			for j, letter in enumerate(line): # x
				if letter == '1':
					paper = pygame.Surface((self.tile_size, self.tile_size))
					paper.fill(BLUE)
					self.background.blit(paper, (j*self.tile_size, i*self.tile_size))
				if letter == ' ':
					pass

			


window.load_map()