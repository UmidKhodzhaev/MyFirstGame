import pygame
from constants import *
from Npc import *
class Player(Npc):
	def __init__(self, health = 1):
		pygame.sprite.Sprite.__init__(self)
		self.health = health
		self.max_hp = health
		self.images = {}
		self.images['rstand'] = pygame.image.load(PLAYER_STAND["texture"])
		self.images['lstand'] = pygame.transform.flip(self.images['rstand'], True, False) # (!) развернуть self.images['rstand'] по горизонтали
		self.images['rjump'] = pygame.image.load(PLAYER_JUMP["texture"])
		self.images['ljump'] = pygame.transform.flip(self.images['rjump'], True, False) # (!) аналогично
		self.images['rwalk'] = pygame.image.load(PLAYER_WALK["texture"])
		self.images['lwalk'] = pygame.transform.flip(self.images['rwalk'], True, False) # (!) аналогично
		self.image = self.images['rstand']
		self.rect = self.image.get_rect()
		self.score = 0
		# self.sound = pygame.mixer.Sound('Run.mp3')
		self.rect.x = 0
		self.rect.y = 0
		self.start_x = 0
		self.start_y = 0
		self.new()

	def new(self):
		self.dir = 'right'
		self.image = self.images['rstand']
		self.up = self.left = self.right = False
		self.hor_speed = 0
		self.vert_speed = 0
		self.speed = 8
		self.jumpPower = 17
		self.collided = False
		self.prev_collided = False
		self.on_ground = False
		self.npc = Npc()
		
		

	def update(self, blocks, loot, enemy, heal_block):
		# if not self.collided:
		# 	self.vert_speed += GRAVITY
		if self.up and self.on_ground:
			self.vert_speed = -self.jumpPower
		if self.left:
			self.dir = 'left'
			# self.sound.play(loops = -1)
			self.hor_speed = -self.speed
		if self.right:
			self.dir = 'right'
			self.hor_speed = self.speed

		if not self.right and not self.left:
			self.hor_speed = 0

		# self.rect.y += self.vert_speed
		# self.collideV(self.vert_speed, blocks)

		# self.rect.x += self.hor_speed
		# self.collideG(self.hor_speed, blocks)
		# if self.rect.x < 0:
		# 	self.rect.x = 0

		if self.vert_speed != 0 or self.vert_speed == 0 and not self.on_ground and not self.prev_collided:
			if self.dir == 'left':
				self.image = self.images['ljump']
			else:
				self.image = self.images['rjump']
		else:
			# (!) в зависимости от направления движения, текущей скорости
			# (!) установить текстуру для движения влево и вправо  
			# (!) и простоя влево и вправо
			if self.hor_speed != 0:
				if self.dir == 'left':
					self.image = self.images['lwalk']
				else:
					self.image = self.images['rwalk']
			else:
				if self.dir == 'left':
					self.image = self.images['lstand']
				else:
					self.image = self.images['rstand']

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
