from pygame import *
import os
from constants import *
from colors import *
from Npc import *
import pyganim

 

WIDTH = 48
HEIGHT = 48
class Drotik(Npc):
	def __init__(self, x = 30, y = 30):
		Npc.__init__(self)
		self.image = Surface((WIDTH,HEIGHT))
		self.rect = Rect(x, y, WIDTH, HEIGHT) # прямоугольный объект
		self.image.fill(COLOR) 
		self.image.set_colorkey(COLOR) # делаем фон прозрачным
		self.boltAnimJump = pyganim.PygAnimation(ANIMATION_BULLET)
		self.boltAnimJump.play()
		self.right = True
		self.left = False
		self.speed = 8
		self.hor_speed = 0
		self.vert_speed = 0
		self.collided = False
		self.prev_collided = False
		self.on_ground = False
		self.col = False

	def update(self, blocks, loot, enemy, heal_block):
		if self.left:
			self.hor_speed = -self.speed
		if self.right:
			self.hor_speed = self.speed
			self.image.fill(COLOR)
			self.boltAnimJump.blit(self.image, (0, 0))
		self.rect.x += self.hor_speed
		for block in blocks:
			if pygame.sprite.collide_rect(self, block):
				self.col = True



			
		# if self.rect.x != self.start_x:
		# 	self.rect.x += self.vert_speed
		# else:
		# 	if self.rect.x != self.start_x + 5 * TILE_SIZE:
		# 		self.rect.x -= self.vert_speed
		# if self.collided:
		# 		self.vert_speed = -self.vert_speed
