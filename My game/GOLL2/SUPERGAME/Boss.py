from pygame import *
import os
from constants import *
from colors import *
from Npc import *
import pyganim


 
WIDTH = 384
HEIGHT = 384
class Boss(Npc):
	def __init__(self, x = 30, y = 30):
		Npc.__init__(self)	
		self.image = Surface((WIDTH,HEIGHT))
		self.rect = Rect(x, y, WIDTH, HEIGHT) # прямоугольный объект
		self.image.fill(COLOR) 
		self.image.set_colorkey(COLOR) # делаем фон прозрачным
		self.boltAnimStay = pyganim.PygAnimation(ANIMATION_BOSS)
		self.boltAnimStay.play()
		self.g_x = 0
		self.g_y = 0
		self.right = True
		self.speed = 0
		self.hor_speed = 0
		self.vert_speed = 0
		self.collided = False
		self.prev_collided = False
		self.on_ground = False




	def respawn(self):
		self.rect.x = self.start_x
		self.rect.y = self.start_y
		


	def update(self, blocks, loot, enemy, heal_block):
		if self.right:
			self.image.fill(COLOR)
			self.boltAnimStay.blit(self.image, (0, 0))



		self.physics(blocks, loot, enemy, heal_block)

	def collideG(self, hor_speed, blocks):
		for block in blocks:
			if pygame.sprite.collide_rect(self, block):
				if hor_speed > 0:
					self.rect.right = block.rect.left
					self.speed = -self.speed
				if hor_speed < 0:
					self.rect.left = block.rect.right
					self.speed = -self.speed