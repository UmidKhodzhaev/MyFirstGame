import pygame
import os
from constants import *
from colors import *
from Npc import *

 
class Monster(Npc):
	def __init__(self, x = 30, y = 30, texture = JIIINGO):
		Npc.__init__(self)
		# self.image = pygame.image.load(texture["texture"])
		# if texture["rect"] != 0:
		# 	self.image = self.image.subsurface(texture["rect"])
		# self.image.convert()
		# self.rect = self.image.get_rect()	
		self.images = {}
		self.images['rstand'] = pygame.image.load(texture["texture"])
		self.images['lstand'] = pygame.transform.flip(self.images['rstand'], True, False)
		self.image = self.images['rstand']
		self.rect = self.image.get_rect()
		self.start_x = x
		self.start_y = y
		self.g_x = 0
		self.g_y = 0
		self.right = True
		self.left = False
		self.speed = 8
		self.hor_speed = 0
		self.vert_speed = 0
		self.collided = False
		self.prev_collided = False
		self.on_ground = False



	def respawn(self):
		self.rect.x = self.start_x
		self.rect.y = self.start_y
		


	def update(self, blocks, loot, enemy, heal_block):
		if self.left:
			self.hor_speed = -self.speed
			self.dir = 'left'


		if self.right:
			self.hor_speed = self.speed
			self.dir = 'right'


		if self.dir == 'left':
			self.image = self.images['rstand']
		else:
			self.image = self.images['lstand']


		self.physics(blocks, loot, enemy, heal_block)

	def collideG(self, hor_speed, blocks):
		for block in blocks:
			if pygame.sprite.collide_rect(self, block):
				if hor_speed > 0:
					self.rect.right = block.rect.left
					self.right = False
					self.left = True
				if hor_speed < 0:
					self.rect.left = block.rect.right
					self.right = True
					self.left = False