import pygame
import os
from Block import *
from constants import *
from colors import *
from Npc import *



class Npc1(Npc):
	def __init__(self, x, y, texture = PRIZRAK):
		Npc.__init__(self)
		self.images = {}
		self.images['rstand'] = pygame.image.load(texture["texture"])
		self.images['lstand'] = pygame.transform.flip(self.images['rstand'], True, False)
		self.image = self.images['rstand']
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
	def update(self):
		if self.dir == 'left':
			self.image = self.images['rstand']
		else:
			self.image = self.images['lstand']

