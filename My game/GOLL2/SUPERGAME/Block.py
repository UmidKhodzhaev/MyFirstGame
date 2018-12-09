import pygame
from constants import *
class Block(pygame.sprite.Sprite):
	def __init__(self, x = 0, y = 0, texture = BLUE_SKY):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(texture["texture"])
		if texture["rect"] != 0:
			self.image = self.image.subsurface(texture["rect"])
		# self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
		self.image.convert()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y 