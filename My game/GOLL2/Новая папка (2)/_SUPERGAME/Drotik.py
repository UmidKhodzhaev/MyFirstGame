import pygame
import os
from constants import *
from colors import *
from Npc import *


class Drotik(Npc):
	def __init__(self, x = 30, y = 30, texture = JIIINGO):
		Npc.__init__(self)
		# self.image = pygame.image.load(texture["texture"])
		# if texture["rect"] != 0:
		# 	self.image = self.image.subsurface(texture["rect"])
		# self.image.convert()
		# self.rect = self.image.get_rect()	
		self.images = {}
		self.images['rstand'] = pygame.image.load(texture["texture"])
		self.image = self.images['rstand']
		self.rect = self.image.get_rect()
		self.start_x = x
		self.start_y = y
		self.right = True
		self.left = False
		self.speed = 8
		self.hor_speed = 0
		self.vert_speed = 0
		self.collided = False
		self.prev_collided = False
		self.on_ground = False

	def update(self, blocks, loot, enemy, heal_block):
		if self.left:
			self.hor_speed = -self.speed
		if self.right:
			self.hor_speed = self.speed
		if self.g_col:
			for block in blocks:
					if pygame.sprite.collide_rect(self, block):
						self.speed = -self.speed
			
		# if self.rect.x != self.start_x:
		# 	self.rect.x += self.vert_speed
		# else:
		# 	if self.rect.x != self.start_x + 5 * TILE_SIZE:
		# 		self.rect.x -= self.vert_speed
		# if self.collided:
		# 		self.vert_speed = -self.vert_speed


		self.physics(blocks, loot, enemy, heal_block)
