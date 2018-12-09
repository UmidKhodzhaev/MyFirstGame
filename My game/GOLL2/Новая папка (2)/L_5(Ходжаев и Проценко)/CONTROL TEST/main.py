import pygame
import os
from constants import *
from colors import *


winposx = 50
winposy = 50
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (winposx, winposy)



class player(pygame.sprite.Sprite):
	def __init__(self, health = 3, coords = (180, 500)):
		pygame.sprite.Sprite.__init__(self)
		self.health = health
		self.coords = coords
		self.images = {}
		self.images['rstand'] = pygame.image.load(PLAYER_STAND["texture"])
		self.images['lstand'] = pygame.transform.flip(self.images['rstand'], True, False)
		self.images['rjump'] = pygame.image.load(PLAYER_JUMP["texture"])
		self.images['ljump'] = pygame.transform.flip(self.images['rjump'], True, False)
		self.images['rwalk'] = pygame.image.load(PLAYER_WALK["texture"])
		self.images['lwalk'] = pygame.transform.flip(self.images['rwalk'], True, False)
		for key in self.images.keys():
			self.images[key] = pygame.transform.scale(self.images[key], (TILE_SIZE, int(TILE_SIZE * 1.5))) # (!) растянуть картинку до размера (TILE_SIZE, int(TILE_SIZE * 1.5))
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
		self.gor_speed = 0
		self.vert_speed = 0
		self.speed = 30
		self.jumpPower = 60
		self.collided = False
		self.prev_collided = False
		self.on_ground = False
		self.score = 0

	def update(self, blocks, loot, enemy, running):
		if not self.collided:
			self.vert_speed += GRAVITY
		if self.up and self.on_ground:
			self.vert_speed = -self.jumpPower
		if self.left:
			self.dir = 'left'
			self.gor_speed = -self.speed
		if self.right:
			self.dir = 'right'
			self.gor_speed = self.speed

		if not self.right and not self.left:
			self.gor_speed = 0

		self.rect.y += self.vert_speed
		self.collideV(self.vert_speed, blocks)

		self.rect.x += self.gor_speed
		self.collideG(self.gor_speed, blocks)

		if self.vert_speed != 0 or self.vert_speed == 0 and not self.on_ground and not self.prev_collided:
			if self.dir == 'left':
				self.image = self.images['ljump']
			else:
				self.image = self.images['rjump']
		else:
			if self.dir == 'right':
				self.image = self.images['rwalk']
			else:
				self.image = self.images['lwalk']

			# (!) в зависимости от направления движения, текущей скорости
			# (!) установить текстуру для движения влево и вправо  
			# (!) и простоя влево и вправо по аналогии

		self.prev_collided = self.collided

		
		for block in loot:
			if pygame.sprite.collide_rect(self, block):
				block.kill()
				self.score += 1
		for block in enemy:
			if pygame.sprite.collide_rect(self, block):
				self.new(self.coords)
				self.health -= 1
			elif self.health == 0:
				self.running = False

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
				
					if pygame.sprite.collide_rect(self, block):
						block.kill()
						self.score += 1


	def collideG(self, gor_speed, blocks):
		for block in blocks:
			if pygame.sprite.collide_rect(self, block):
				if gor_speed > 0:
					self.rect.right = block.rect.left
				if gor_speed < 0:
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

class Game:
	def __init__(self, width, height, fps):
		pygame.init()
		self.screen = pygame.display.set_mode((width, height))
		self.background = pygame.image.load(BACKGROUND["texture"])
		self.background = pygame.transform.scale(self.background, self.screen.get_size())
		self.background.convert()
		self.fps = fps
		self.font = pygame.font.SysFont("comicsansms", int(TILE_SIZE/5*4))
		self.clock = pygame.time.Clock()
		self.running = False

		self.playtime = 0.0
		self.allBlocks = pygame.sprite.Group()
		self.solidBlocks = pygame.sprite.Group()
		self.lootBlocks = pygame.sprite.Group()
		self.enemy = pygame.sprite.Group()

		self.player = player()

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
					if letter in Enemy:
						block_temp.add(self.enemy)

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
		self.playtime += self.clock.tick(self.fps) / 1000
		 # (!) добавить время текущего кадра ко времени всего раунда
		self.player.update(self.solidBlocks, self.lootBlocks, self.enemy, self.running)
		 # (!) выведите в заголовок окна текущий ФПС
		pygame.display.set_caption("FPS: "+str(int(self.clock.get_fps())))

		if not self.lootBlocks:
			self.running = False
		

	def draw(self):
		self.screen.blit(self.background, (0, 0))
		text = "SCORE: " + str(self.player.score) + ", playtime: " + "{0:.2f}".format(self.playtime)
		self.render_text(text, 0, 0)

		self.allBlocks.draw(self.screen)
		 # (!) нарисовать все блоки
		pygame.display.update()
		 # (!) обновить экран

	def render_text(self, text, x, y):
		self.x = x
		self.y = y
		self.text = text
		font = pygame.font.Font(None , TILE_SIZE)
		text1 = font.render(self.text, 1 , (0, 0, 0))
		self.screen.blit(text1, (self.x , self.y))

		 # (!) создайте "бумажку" с заданным текстом чёрного цвета
		# self.screen.blit(surface, (self.x, self.y))

	def play(self):
		self.running = True
		self.playtime = 0.0
		while self.running:
			self.get_events()
			self.update()
			self.draw()
		if self.running == False:
			for block in self.allBlocks:
				block.kill()
		 # (!) уничтожьте все блоки, они нам больше не нужны
			
		self.playtime = float("{0:.2f}".format(self.playtime))

	def menu_update(self):
		self.clock.tick(self.fps)
		pygame.display.set_caption("FPS: "+str(int(self.clock.get_fps())))
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
					self.player.new(self.player.coords)
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
	game = Game(WIN_WIDTH, WIN_HEIGHT, FPS)
	game.menu()
	 # (!) запустите меню игры