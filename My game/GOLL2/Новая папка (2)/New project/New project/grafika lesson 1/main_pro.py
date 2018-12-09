import pygame
from colors import *

class kvadratik():
	def __init__(self, some_color, small_rect):
		self.some_color = (255, 0 , 0)
		self.small_rect = (300, 300, 300 , 30)

class Screen():
	def __init__(self, width, height, fps):
		pygame.init()
		self.width = width
		self.height = height
		self.window_size = (width, height)
		self.screen = pygame.display.set_mode(self.window_size, pygame.DOUBLEBUF)
		
		self.kvadratik = kvadratik()

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

			self.kvadratik = pygame.Surface(self.screen.get_size())
			self.screen.blit(self.kvadratik, (100, 200))
			self.kvadratik.fill(self.some_color, self.small_rect)
			self.kvadratik.convert()


if __name__ == "__main__":
	Screen(640, 480, 30, kvadratik((255, 0 , 0), (300, 300, 300, 30))).run()