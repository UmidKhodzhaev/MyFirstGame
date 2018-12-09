from pygame import *
import pyganim
from constants import *
import os
from colors import *

		

ANIMATION_Stay = [("textures\\Money\\1.1.png"),
                   ("textures\\Money\\1.2.png"),
                   ("textures\\Money\\1.3.png"),
                   ("textures\\Money\\1.4.png"),
                   ("textures\\Money\\1.5.png"),
                   ("textures\\Money\\1.6.png")]

WIDTH = 15
HEIGHT = 30
class Money(pygame.sprite.Sprite):
	def __init__(self, x = 0, y = 0):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((WIDTH,HEIGHT))
		self.rect = Rect(x, y, WIDTH, HEIGHT) # прямоугольный объект
		self.image.fill(COLOR) 
		self.image.set_colorkey(COLOR) # делаем фон прозрачным
		def make_boltAnim(anim_list, delay):
			boltAnim = []
			for anim in anim_list:
				boltAnim.append((anim, delay))
			Anim = pyganim.PygAnimation(boltAnim)
			return Anim
		self.boltAnimStay = make_boltAnim(ANIMATION_Stay, ANIMATION_DELAY)
		self.boltAnimStay.play()
	def drw(self):
		self.image.fill(COLOR)
		self.boltAnimStay.blit(self.image, (0, 0))
	def respawn(self):
		pass