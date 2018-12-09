import pygame
import os
from constants import *
from colors import *


os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (WIN_POS_X, WIN_POS_Y) # (!) установить окно в точку (WIN_POS_X, WIN_POS_Y)

class player(pygame.sprite.Sprite):
	def __init__(self,coords = (96, 912), health = 3):
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
		for key in self.images.keys():
			self.images[key] = pygame.transform.scale(self.images[key], (TILE_SIZE, int(TILE_SIZE * 1.5))) # (!) растянуть картинку до размера (TILE_SIZE, int(TILE_SIZE * 1.5))
		self.image = self.images['rstand']
		self.rect = self.image.get_rect()
		self.score = 0
		self.coords = coords
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
		self.speed = 8
		self.jumpPower = 17
		self.collided = False
		self.prev_collided = False
		self.on_ground = False
		

	def update(self, blocks, loot, enemy, heal_block):
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
		if self.rect.x < 0:
			self.rect.x = 0

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
				self.new(self.coords)
				self.health -= 1
		for block in heal_block:
			if pygame.sprite.collide_rect(self, block):
				if self.health < self.max_hp:
					self.health += 1
					block.kill()

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
		self.image.convert()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class game:
	def __init__(self, width, height, fps):
		pygame.init()
		self.map = 'level1'
		self.playtime = 0.0
		self.counter = 1
		self.m_counter = 0
		self.screen = pygame.display.set_mode((width, height))
		self.fps = fps
		self.font = pygame.font.SysFont("comicsansms", int(TILE_SIZE/5*4))
		self.clock = pygame.time.Clock()

		self.playtime = 0.0
		self.player = player()
		self.allBlocks = pygame.sprite.Group()
		self.solidBlocks = pygame.sprite.Group()
		self.lootBlocks = pygame.sprite.Group()
		self.enemy = pygame.sprite.Group()
		self.heal = pygame.sprite.Group()

	def load_map(self):
		counter = str(self.counter)
		for letter in counter:
			self.map = MAP_level[letter]
		file = open(self.map, 'r')
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
					if letter in HEAL_BLOCKS:
						block_temp.add(self.heal)

				if letter == 's':
					self.starting_point = (j * TILE_SIZE, i * TILE_SIZE)
		self.m_counter = self.counter
		self.BACKGROUND = background_key[str(self.m_counter)]
		self.background = pygame.image.load(self.BACKGROUND["texture"])
		self.background = pygame.transform.scale(self.background, self.screen.get_size())
		self.background.convert()





	def health_draw(self):
		heart = pygame.sprite.Group()
		health = int(self.player.health)
		j = 1100
		k = 30
		i = 1
		while i <= health:
			i += 1
			j -= 50
			heart1 = block(j, k, HEART_FULL)
			heart1.add(heart)
		heart.draw(self.screen)





	def get_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.menu()
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
		if not self.lootBlocks:
			self.running = False
			my_file = open("some.txt", "a")
			my_file.write(str("{0:.2f}".format(self.playtime)) + '\n')
			my_file.close()
			self.counter += 1
			if self.counter < MAP_level_max:
				self.menu()
			else:
				self.win_menu()
		if self.player.health == 0:
			self.running = False
			self.deth_menu()
		self.playtime += self.clock.tick(self.fps) / 1000 # (!) добавить время текущего кадра ко времени всего раунда
		self.player.update(self.solidBlocks, self.lootBlocks, self.enemy, self.heal)
		pygame.display.set_caption("FPS: " + str(int(self.clock.get_fps()))) # (!) выведите в заголовок окна текущий ФПС
	def draw(self):
		self.screen.blit(self.background, (0, 0))
		
		text = "SCORE: " + str(self.player.score) + ", playtime: " + "{0:.2f}".format(self.playtime)
		self.render_text(text, 0, 0)
		self.health_draw()

		self.allBlocks.draw(self.screen) # (!) нарисовать все блоки

		pygame.display.update() # (!) обновить экран

	def render_text(self, text, x, y):
		surface = self.font.render(text, True, Color.Black) # (!) создайте "бумажку" с заданным текстом чёрного цвета в заданной координате
		self.screen.blit(surface, (x, y))

	def play(self):
		self.running = True
		while self.running:
			self.get_events()
			self.update()
			self.draw()
		for block in self.allBlocks: # (!) уничтожьте все блоки, они нам больше не нужны
			block.kill()
		self.playtime = float("{0:.2f}".format(self.playtime))

	def menu_update(self):
		self.clock.tick(self.fps)
		pygame.display.set_caption("FPS: " + str(int(self.clock.get_fps()))) # (!) выведите в заголовок окна текущий ФПС
		self.BACKGROUND = background_key[str(self.m_counter)]
		self.background = pygame.image.load(self.BACKGROUND["texture"])
		self.background = pygame.transform.scale(self.background, self.screen.get_size())
		self.background.convert()

	def menu_get_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					exit()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_p:
					self.load_map()
					self.player.new(self.starting_point) # (!) установите игроку начальные параметры
					self.player.add(self.allBlocks)
					self.play()


	def menu_deth_draw(self):
		self.counter = 1
		self.m_counter = "d"
		self.player.score = 0
		self.playtime = 0.0
		for block in self.allBlocks: # (!) уничтожьте все блоки, они нам больше не нужны
			block.kill()
		self.player.health = 3
		self.screen.blit(self.background, (0, 0))
		self.render_text("Press P to play or Escape to Exit", 0, 0)
		text = "Game Over"
		self.render_text(text, 450, 300)

		pygame.display.update()

	def menu_draw(self):
		for block in self.allBlocks: # (!) уничтожьте все блоки, они нам больше не нужны
			block.kill()
		self.screen.blit(self.background, (0, 0))
		if self.counter == 1:
			self.render_text("Press P to play or Escape to Exit", 0, 0)
		else:
			self.render_text("Press P to continue or Escape to Exit", 0, 0)


		pygame.display.update()

	def menu_deth_get_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					exit()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_p:
					self.load_map()
					self.player.new(self.starting_point) # (!) установите игроку начальные параметры
					self.player.add(self.allBlocks)
					self.play()




	def win_menu(self):
		self.running = False
		self.win_menu_running = True
		while self.win_menu_running:
			self.menu_update()
			self.win_menu_draw()
			self.menu_deth_get_events()


	def win_menu_draw(self):
		self.counter = 1
		self.m_counter = "w"
		self.player.score = 0
		self.playtime = 0.0
		for block in self.allBlocks: # (!) уничтожьте все блоки, они нам больше не нужны
			block.kill()
		self.player.health = 3
		self.screen.blit(self.background, (0, 0))
		self.render_text("Press P to restart or Escape to Exit", 0, 0)
		text = "YOU WIN !!!"
		self.render_text(text, 450, 300)

		pygame.display.update()



	def menu(self):
		self.menu_running = True
		while self.menu_running:
			self.menu_update()
			self.menu_draw()
			self.menu_get_events()


	def deth_menu(self):
		self.menu_death_running = True
		while self.menu_death_running:
			self.menu_update()
			self.menu_deth_draw()
			self.menu_deth_get_events()

if __name__ == "__main__":
	game(WIN_WIDTH, WIN_HEIGHT, FPS).menu() # (!) запустите меню игры