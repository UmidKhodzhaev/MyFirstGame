import pygame
from colors import *
import os

solidblocks = '0'

blue_sky = "textures\\blue_sky.png"
wall = "textures\\wall.png"
coin = "textures\\coin2.png"
hero = "textures\\hero6.png"
air = "textures\\air.png"


class block(pygame.sprite.Sprite):
	def __init__(self, x = 0, y = 0):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(textures)
		self.image.convert()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y



class GameScreen():
	def __init__(self):
		pygame.init()
		self.tile_size = 50
		self.allBlocks = pygame.sprite.Group()
		self.hardBlocks = pygame.sprite.Group()
		self.lootblocks = pygame.sprite.Group()
		self.load_map()
		# self.background.convert()		

		self.fps = fps
		self.clock = pygame.time.Clock()
		self.playtime = 0.0


	def load_map(self):
		file = open("map", 'r')
		for i, line in enumerate(file): # y
			for j, letter in enumerate(line): # x
				if letter == '0':
					block_temp = block(j*self.tile_size, i*self.tile_size) 
					block_temp.add(self.allBlocks)
					if letter in solidblocks:
						block_temp.add(self.hardBlocks)



	def run(self):
		print(self.hardBlocks.x)



if __name__ == "__main__":
	# game_screen.Menu()
	GameScreen().run()


