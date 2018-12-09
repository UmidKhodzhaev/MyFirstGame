import pygame
from colors import *

class Screen():
	def __init__(self, width, height, fps):
		pygame.init()
		self.width = width
		self.height = height
		self.window_size = (width, height)
		self.screen = pygame.display.set_mode(self.window_size, pygame.DOUBLEBUF)


		self.fps = fps
		self.clock = pygame.time.Clock()
		self.playtime = 0.0

	def run(self):
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						running = False

			self.background = pygame.Surface(self.screen.get_size())
			self.background.fill(get_random_color())
			self.background.convert()		
			self.screen.blit(self.background, (0, 0))
			pygame.display.flip()

if __name__ == "__main__":
	Screen(640, 480, 30).run()