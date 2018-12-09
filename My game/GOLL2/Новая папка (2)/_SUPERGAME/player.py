from pygame import *
import pyganim
from constants import *
from Npc import *
import os
from colors import *

		
WIDTH = 48
HEIGHT = 48



class Player(Npc):
	def __init__(self, x, y, health = 1):
		Npc.__init__(self)
		self.health = health
		self.max_hp = health
		self.keys = 0
		self.image = Surface((WIDTH,HEIGHT))
		self.rect = Rect(x, y, WIDTH, HEIGHT) # прямоугольный объект
		self.image.fill(COLOR) 
		self.image.set_colorkey(COLOR) # делаем фон прозрачным
		def make_boltAnim(anim_list, delay):
			boltAnim = []
			for anim in anim_list:
				boltAnim.append((anim, delay))
			Anim = pyganim.PygAnimation(boltAnim)
			return Anim
		
		self.score = 0
		self.sound = pygame.mixer.Sound('Run.ogg')
		self.rect.x = 0
		self.rect.y = 0
		self.start_x = 0
		self.start_y = 0
		self.new()

		self.boltAnimJump = pyganim.PygAnimation(ANIMATION_JUMP)
		self.boltAnimJump.play()

		self.boltAnimJumpLeft = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
		self.boltAnimJumpLeft.play()

		self.boltAnimJumpRight = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
		self.boltAnimJumpRight.play()

		self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
		self.boltAnimStay.play()

		self.boltAnimRight = make_boltAnim(ANIMATION_RIGHT, ANIMATION_DELAY)
		self.boltAnimRight.play()

		self.boltAnimLeft = make_boltAnim(ANIMATION_LEFT, ANIMATION_DELAY)
		self.boltAnimLeft.play()
		


	def new(self):
		self.dir = 'right'
		self.up = self.left = self.right = False
		self.hor_speed = 0
		self.vert_speed = 0
		self.speed = 8
		self.keys = 0
		self.jumpPower = 17
		self.collided = False
		self.prev_collided = False
		self.on_ground = False
		self.npc = Npc()
		
		

	def update(self, blocks, loot, enemy, heal_block, keys):
		# if not self.collided:
		# 	self.vert_speed += GRAVITY
		if self.up and self.on_ground:
			self.vert_speed = -self.jumpPower
			self.image.fill(COLOR)
			self.boltAnimJump.blit(self.image, (0, 0))
		if self.left:
			self.dir = 'left'
			self.sound.play(loops = -1)
			self.image.fill(COLOR)
			self.boltAnimLeft.blit(self.image, (0, 0))
			self.hor_speed = -self.speed
		if self.right:
			self.dir = 'right'
			self.image.fill(COLOR)
			self.boltAnimRight.blit(self.image, (0, 0))
			self.sound.play(loops = -1)
			self.hor_speed = self.speed
		# self.sound.stop()
		if not self.right and not self.left:
			self.hor_speed = 0
			self.image.fill(COLOR)
			self.boltAnimStay.blit(self.image, (0, 0))
			self.sound.stop()

		# self.rect.y += self.vert_speed
		# self.collideV(self.vert_speed, blocks)

		# self.rect.x += self.hor_speed
		# self.collideG(self.hor_speed, blocks)
		# if self.rect.x < 0:
		# 	self.rect.x = 0

		if self.vert_speed != 0 or self.vert_speed == 0 and not self.on_ground and not self.prev_collided:
			if self.dir == 'left':
				self.boltAnimJumpLeft.blit(self.image, (0, 0))
			else:
				self.boltAnimJumpRight.blit(self.image, (0, 0))

		self.prev_collided = self.collided
		for block in loot:
			if pygame.sprite.collide_rect(self, block): # (!) если сталкиваемся с блоком
				self.score += 10 # (!) то количество очков увеличивается
				block.kill() # (!) и блок исчезает
		for block in enemy:
			if pygame.sprite.collide_rect(self, block):
				self.new()
				self.health -= 1
		for block in heal_block:
			if pygame.sprite.collide_rect(self, block):
				if self.health < self.max_hp:
					self.health += 1
					block.kill()
		for block in keys:
			if pygame.sprite.collide_rect(self, block):
				self.keys += 1
				block.kill()


		self.physics(blocks, loot, enemy, heal_block)
	# def collideV(self, vert_speed, blocks):
	# 	self.collided = False
	# 	self.on_ground = False

	# 	for block in blocks:
	# 		if pygame.sprite.collide_rect(self, block):
	# 			self.collided = True
	# 			self.vert_speed = 0
	# 			self.on_ground = True
	# 			if vert_speed >= 0:
	# 				self.rect.bottom = block.rect.top
	# 			elif vert_speed < 0:
	# 				self.rect.top = block.rect.bottom
	# 				self.on_ground = False

	# def collideG(self, hor_speed, blocks):
	# 	for block in blocks:
	# 		if pygame.sprite.collide_rect(self, block):
	# 			if hor_speed > 0:
	# 				self.rect.right = block.rect.left
	# 			if hor_speed < 0:
	# 				self.rect.left = block.rect.right
		
		# self.images = {}
		# self.images['rstand'] = pygame.image.load(PLAYER_STAND["texture"])
		# self.images['lstand'] = pygame.transform.flip(self.images['rstand'], True, False) # (!) развернуть self.images['rstand'] по горизонтали
		# self.images['rjump'] = pygame.image.load(PLAYER_JUMP["texture"])
		# self.images['ljump'] = pygame.transform.flip(self.images['rjump'], True, False) # (!) аналогично
		# self.images['rwalk'] = pygame.image.load(PLAYER_WALK_R1["texture"])
		# self.images['lwalk'] = pygame.transform.flip(self.images['rwalk'], True, False) # (!) аналогично
