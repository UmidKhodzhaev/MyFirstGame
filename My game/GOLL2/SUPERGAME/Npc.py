import pygame
import os
from Block import *
from constants import *
from colors import *
class Npc(Block):
	def __init__(self):
		Block.__init__(self)
		self.hor_speed = 0
		self.vert_speed = 0
		self.collided = False
		self.prev_collided = False
		self.on_ground = False
		self.g_col = False
	def physics(self,blocks, loot, enemy, heal_block):
		if not self.collided:
			self.vert_speed += GRAVITY

		self.rect.y += self.vert_speed
		self.collideV(self.vert_speed, blocks)

		self.rect.x += self.hor_speed
		self.collideG(self.hor_speed, blocks)
 

	def collideV(self, vert_speed, blocks):
		self.collided = False
		self.on_ground = False
		for block in blocks:
			if pygame.sprite.collide_rect(self, block):
				self.collided = True
				self.vert_speed = 0
				self.on_ground = True
				if vert_speed >= 0:
					self.rect.bottom = block.rect.top
				elif vert_speed < 0:
					self.rect.top = block.rect.bottom
					self.on_ground = False

	def collideG(self, hor_speed, blocks):
		for block in blocks:
			if pygame.sprite.collide_rect(self, block):
				if hor_speed > 0:
					self.rect.right = block.rect.left
				if hor_speed < 0:
					self.rect.left = block.rect.right
		