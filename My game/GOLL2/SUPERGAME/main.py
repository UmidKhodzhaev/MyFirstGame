import pygame
import os
from constants import *
from colors import *


 # (!) установить окно в точку (WIN_POS_X, WIN_POS_Y)

class player(pygame.sprite.Sprite):
	def __init__(self, coords = (0, 0)):
		pygame.sprite.Sprite.__init__(self)
		self.images = {}
		self.images['rstand'] = pygame.image.load(PLAYER_STAND["texture"])
		self.images['lstand'] =  # (!) развернуть self.images['rstand'] по горизонтали
		self.images['rjump'] = pygame.image.load(PLAYER_JUMP["texture"])
		self.images['ljump'] =  # (!) аналогично
		self.images['rwalk'] = pygame.image.load(PLAYER_WALK["texture"])
		self.images['lwalk'] =  # (!) аналогично
		for key in self.images.keys():
			self.images[key] =  # (!) растянуть картинку до размера (TILE_SIZE, int(TILE_SIZE * 1.5))
		self.image = self.images['rstand']
		self.rect = self.image.get_rect()
		self.new(coords)

	def new(self, coords):
		self.spawn_coords = coords
		self.dir = 'right'
		self.image = self.images['rstand']
		self.rect.x = self.spawn_coords[0]
		self.rect.y = self.spawn_coords[1]
		self.up = self.left = self.right = False
		self.hor_speed = 0
		self.vert_speed = 0
		self.speed = 10
		self.jumpPower = 19
		self.collided = False
		self.prev_collided = False
		self.on_ground = False
		self.score = 0

	def update(self, blocks, loot):
		if not self.collided:
			self.vert_speed += GRAVITY
		if self.up and self.on_ground:
			self.vert_speed = -self.jumpPower
		if self.left:
			self.dir = 'left'
			self.hor_speed = -self.speed
		if self.right:
			self.dir = 'right'
			self.hor_speed = self.speed

		if not self.right and not self.left:
			self.hor_speed = 0

		self.rect.y += self.vert_speed
		self.collideV(self.vert_speed, blocks)

		self.rect.x += self.hor_speed
		self.collideG(self.hor_speed, blocks)

		if self.vert_speed != 0 or self.vert_speed == 0 and not self.on_ground and not self.prev_collided:
			if self.dir == 'left':
				self.image = self.images['ljump']
			else:
				self.image = self.images['rjump']
		else:
			# (!) в зависимости от направления движения, текущей скорости
			# (!) установить текстуру для движения влево и вправо  
			# (!) и простоя влево и вправо по аналогии

		self.prev_collided = self.collided

		for block in loot:
			if  # (!) если сталкиваемся с блоком
				 # (!) то количество очков увеличивается
				 # (!) и блок исчезает

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

class block(pygame.sprite.Sprite):
	def __init__(self, x = 0, y = 0, texture = BLUE_SKY):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(texture["texture"])
		if texture["rect"] != 0:
			self.image = self.image.subsurface(texture["rect"])
		self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
		self.image.convert() # CHECK
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class game:
	def __init__(self, width, height, fps):
		pygame.init()
		self.screen = pygame.display.set_mode((width, height))
		self.background = pygame.image.load(BACKGROUND["texture"])
		self.background = pygame.transform.scale(self.background, self.screen.get_size())
		self.background.convert()
		self.fps = fps
		self.font = pygame.font.SysFont("comicsansms", int(TILE_SIZE/5*4))
		self.clock = pygame.time.Clock()

		self.playtime = 0.0
		self.player = player()
		self.allBlocks = pygame.sprite.Group()
		self.solidBlocks = pygame.sprite.Group()
		self.lootBlocks = pygame.sprite.Group()

	def load_map(self):
		file = open("level1", 'r')
		for i, line in enumerate(file):  # y
			for j, letter in enumerate(line):  # x
				if letter in MAP_KEYS.keys():
					block_temp = block(j * TILE_SIZE, i * TILE_SIZE, MAP_KEYS[letter])
					block_temp.add(self.allBlocks)
					if letter in SOLID_BLOCKS:
						block_temp.add(self.solidBlocks)
					if letter in LOOT_BLOCKS:
						block_temp.add(self.lootBlocks)

				if letter == 's':
					self.starting_point = (j * TILE_SIZE, i * TILE_SIZE)

	def get_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.running = False
				if event.key == pygame.K_w:
					self.player.up = True
				if event.key == pygame.K_a:
					self.player.left = True
				if event.key == pygame.K_d:
					self.player.right = True
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w:
					self.player.up = False
				if event.key == pygame.K_a:
					self.player.left = False
				if event.key == pygame.K_d:
					self.player.right = False

	def update(self):
		 # (!) добавить время текущего кадра ко времени всего раунда
		self.player.update(self.solidBlocks, self.lootBlocks)
		 # (!) выведите в заголовок окна текущий ФПС
		if not self.lootBlocks:
			self.running = False

	def draw(self):
		self.screen.blit(self.background, (0, 0))
		
		text = "SCORE: " + str(self.player.score) + ", playtime: " + "{0:.2f}".format(self.playtime)
		self.render_text(text, 0, 0)

		 # (!) нарисовать все блоки

		 # (!) обновить экран

	def render_text(self, text, x, y):
		 # (!) создайте "бумажку" с заданным текстом чёрного цвета
		self.screen.blit(surface, (x, y))

	def play(self):
		self.running = True
		self.playtime = 0.0
		while self.running:
			self.get_events()
			self.update()
			self.draw()
		 # (!) уничтожьте все блоки, они нам больше не нужны
			
		self.playtime = float("{0:.2f}".format(self.playtime))

	def menu_update(self):
		self.clock.tick(self.fps)
		 # (!) выведите в заголовок окна текущий ФПС

	def menu_get_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.menu_running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.menu_running = False
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_p:
					self.load_map()
					 # (!) установите игроку начальные параметры
					self.player.add(self.allBlocks)
					self.play()

	def menu_draw(self):
		self.screen.blit(self.background, (0, 0))
		self.render_text("Press P to play or Escape to Exit", 0, 0)
		text = "Last time you beat it in " + str(self.playtime) + " seconds"
		self.render_text(text, 0, TILE_SIZE)

		pygame.display.update()

	def menu(self):
		self.menu_running = True
		while self.menu_running:
			self.menu_get_events()
			self.menu_update()
			self.menu_draw()

if __name__ == "__main__":
	 # (!) запустите меню игры