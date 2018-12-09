import pygame
import os
from player import *
from constants import *
from colors import *
from Block import *
from Image import *
from Monster import *



os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (WIN_POS_X, WIN_POS_Y) # (!) установить окно в точку (WIN_POS_X, WIN_POS_Y)


class game:
	def __init__(self, width, height, fps):
		pygame.init()
		self.map = 'level1'
		self.playtime = 0.0
		self.counter = 1
		self.m_counter = 0
		self.T_counter = 0
		self.screen = pygame.display.set_mode((width, height))
		self.fps = fps
		self.font = pygame.font.SysFont("comicsansms", int(TILE_SIZE/5*4))
		self.clock = pygame.time.Clock()
		self.cam_top = WIN_HEIGHT * 5/12
		self.cam_bottom = WIN_HEIGHT * 7/12
		self.cam_left = WIN_WIDTH* 5/12
		self.cam_right = WIN_WIDTH * 6/12
		self.back_x = 0
		self.back_y = 0
		self.cam_x = 0
		self.cam_y = 0
		self.start_x = 0
		self.start_y = 0
		self.i = 0

		self.playtime = 0.0
		self.g_starting_point = (0, 0)
		self.player = Player(self.start_x, self.start_y)
		self.monster = Monster(self.g_starting_point, JIIINGO)
		if self.counter == 1:
			self.player.p_y = 0
		self.allBlocks = pygame.sprite.Group()
		self.solidBlocks = pygame.sprite.Group()
		self.lootBlocks = pygame.sprite.Group()
		self.enemy = pygame.sprite.Group()
		self.heal = pygame.sprite.Group()
		self.door = pygame.sprite.Group()
		self.keys = pygame.sprite.Group()
		self.npc = pygame.sprite.Group()
		self.tabl = pygame.sprite.Group()
		self.camera_speed = self.player.speed
		self.enemy_speed = self.player.speed - 2
		# self.monster.add(self.enemy)
		self.upd_x1 = 0
		self.upd_y1 = 0
		self.upd_x2 = WIN_WIDTH
		self.upd_y2 = WIN_HEIGHT
	def load_map(self):
		counter = str(self.counter)
		for letter in counter:
			self.map = MAP_level[letter]
		file = open(self.map, 'r')
		for i, line in enumerate(file):  # y
			for j, letter in enumerate(line):  # x
				if letter in MAP_KEYS.keys():
					block_temp = Block(j * 2 * TILE_SIZE, i * 2 * TILE_SIZE, MAP_KEYS[letter])
					block_temp.add(self.allBlocks)
					if letter in SOLID_BLOCKS:
						block_temp.add(self.solidBlocks)
					if letter in LOOT_BLOCKS:
						block_temp.add(self.lootBlocks)
					if letter in Enemy:
						block_temp.add(self.enemy)
					if letter in HEAL_BLOCKS:
						block_temp.add(self.heal)
					if letter in DOORS:
						block_temp.add(self.door)
					if letter in KEYS:
						block_temp.add(self.keys)
					if letter in NPC:
						block_temp.add(self.npc)
				if letter == 'G':
					self.i += 1
					
				if letter == 's':
					self.player.start_x = j * TILE_SIZE
					self.player.start_y = i * TILE_SIZE
					self.start_x = j * TILE_SIZE
					self.start_y = i * TILE_SIZE
					self.ret()
		self.m_counter = self.counter
		self.BACKGROUND = background_key[str(self.m_counter)]
		self.background = pygame.image.load(self.BACKGROUND["texture"])
		self.background = pygame.transform.scale(self.background, (70*48,100*48))
		self.background.convert()
		

		# def render_text(self, text, x, y, color = Color.Red):
		# surface = self.font.render(text, True, color) # (!) создайте "бумажку" с заданным текстом чёрного цвета в заданной координате
		# self.screen.blit(surface, (x, y))



	def Npc(self):
		text = 'Press <<T>> to talk'
		if self.T_counter <= 10:
			if self.T_counter == 9:
				text = 'Press <<T>> to take a key of BOSS ROOM'
			for b in self.npc:
					if self.player.rect.x < b.rect.x + 144:
						if self.player.rect.x > b.rect.x - 144:
							if self.player.rect.y > b.rect.y - 144:
								if self.player.rect.y < b.rect.y + 144:
									if self.T_counter < 10:
										self.render_text(text, b.rect.x - 220, b.rect.y+48, Color.Green)
									for event in pygame.event.get():
										if event.type == pygame.QUIT:
											exit()
										if event.type == pygame.KEYDOWN:
											if event.key == pygame.K_e:
												pass
											if event.key == pygame.K_t:
												if self.T_counter < 9:
													TABL = Tabl_keys[str(self.T_counter)]
													Tabl = Image(b.rect.x, b.rect.y-48, TABL)
													Tabl.add(self.tabl)
												if self.T_counter == 9:
													self.player.b_key += 1
												if self.T_counter > 9:
													for b in self.tabl:
														b.kill()
											if event.key == pygame.K_ESCAPE:
												self.menu()
											if event.key == pygame.K_t:
												self.T_counter +=1
											if event.key == pygame.K_w:
												self.player.up = True
											if event.key == pygame.K_a:
												self.player.left = True
											if event.key == pygame.K_d:
												self.player.right = True
											if event.key == pygame.K_f:
												self.player.hit = True
										if event.type == pygame.KEYUP:
											if event.key == pygame.K_e:
												pass
											if event.key == pygame.K_w:
												self.player.up = False
											if event.key == pygame.K_a:
												self.player.left = False
											if event.key == pygame.K_d:
												self.player.right = False
					else:
						for b in self.tabl:
							b.kill()
					if self.player.rect.x > b.rect.x - 144:
						if self.player.rect.x < b.rect.x + 144:
							if self.player.rect.y < b.rect.y + 144:
								if self.player.rect.y > b.rect.y - 144:
									if self.T_counter < 8:
										self.render_text(text, b.rect.x - 220, b.rect.y+48, Color.Green)
									for event in pygame.event.get():
										if event.type == pygame.QUIT:
											exit()
										if event.type == pygame.KEYDOWN:
											if event.key == pygame.K_e:
												pass
											if event.key == pygame.K_t:
												if self.T_counter < 8:
													TABL = Tabl_keys[str(self.T_counter)]
													Tabl = Image(b.rect.x, b.rect.y-48, TABL)
													Tabl.add(self.tabl)
												if self.T_counter >= 9:
													for b in self.tabl:
														b.kill()
											if event.key == pygame.K_ESCAPE:
												self.menu()
											if event.key == pygame.K_t:
												self.T_counter +=1
											if event.key == pygame.K_w:
												self.player.up = True
											if event.key == pygame.K_a:
												self.player.left = True
											if event.key == pygame.K_d:
												self.player.right = True
											if event.key == pygame.K_f:
												self.player.hit = True
										if event.type == pygame.KEYUP:
											if event.key == pygame.K_e:
												pass
											if event.key == pygame.K_w:
												self.player.up = False
											if event.key == pygame.K_a:
												self.player.left = False
											if event.key == pygame.K_d:
												self.player.right = False
					else:
						for b in self.tabl:
							b.kill()


	def upd_d(self):
		if self.player.keys > 0:
			text = 'Press <<E>> to open'
			# self.render_text(text, 100, 100, Color.Green)
			for b in self.door:
				if self.player.rect.x < b.rect.x + 200:
					if self.player.rect.x > b.rect.x - 200:
						if self.player.rect.y > b.rect.y - 250:
							if self.player.rect.y < b.rect.y + 250:
								self.render_text(text, b.rect.x, b.rect.y+48, Color.Green)
								for event in pygame.event.get():
									if event.type == pygame.QUIT:
										exit()
									if event.type == pygame.KEYDOWN:
										if event.key == pygame.K_e:
											b.kill()
											self.player.keys -= 1
										if event.key == pygame.K_ESCAPE:
											self.menu()
										if event.key == pygame.K_w:
											self.player.up = True
										if event.key == pygame.K_a:
											self.player.left = True
										if event.key == pygame.K_d:
											self.player.right = True
										if event.key == pygame.K_f:
											self.player.hit = True
									if event.type == pygame.KEYUP:
										if event.key == pygame.K_e:
											pass
										if event.key == pygame.K_w:
											self.player.up = False
										if event.key == pygame.K_a:
											self.player.left = False
										if event.key == pygame.K_d:
											self.player.right = False

						



	def loot_draw(self):
		SCALE = SCALE_KEY[str(self.player.max_hp)]
		heart = pygame.sprite.Group()
		Scale = pygame.sprite.Group()
		health = int(self.player.health)
		soul = Image(0, 0, SOUL)
		soul.add(Scale)
		key = Image(0, 48, Key1)
		key.add(Scale)
		j = WIN_WIDTH - 48
		k = 30
		z = 48 * (self.player.max_hp + 2)
		scale = Image(WIN_WIDTH - z, k, SCALE)
		scale.add(Scale)
		i = 1
		while i <= health: 
			i += 1
			j -= 48
			heart1 = Block(j, k, HEART_FULL)
			heart1.add(heart)
		Scale.draw(self.screen)
		heart.draw(self.screen)

	def camera(self):
		# self.camera_update()
		if self.cam_y < MAP_BOTTOM -self.cam_top - self.cam_bottom:
			if self.player.rect.y > self.cam_top:
				for b in self.allBlocks:
					b.rect.y-=self.camera_speed
				self.cam_y += self.camera_speed
		if self.cam_y > 0:
			if self.player.rect.y < self.cam_bottom:
				for b in self.allBlocks:
					b.rect.y+=self.camera_speed
				self.cam_y -= self.camera_speed
		if self.cam_x < MAP_RIGHT - self.cam_right - self.cam_left - 68:
			if self.player.rect.x > self.cam_left:
				for b in self.allBlocks:
					b.rect.x-=self.camera_speed
				self.cam_x += self.camera_speed
		if self.cam_x > 0:
			if self.player.rect.x < self.cam_right:
				for b in self.allBlocks:
					b.rect.x+=self.camera_speed
				self.cam_x -= self.camera_speed


	def get_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.ret()
					self.menu()
				if event.key == pygame.K_w:
					self.player.up = True
				if event.key == pygame.K_a:
					self.player.left = True
				if event.key == pygame.K_d:
					self.player.right = True
				if event.key == pygame.K_f:
					self.player.hit = True
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w:
					self.player.up = False
				if event.key == pygame.K_a:
					self.player.left = False
				if event.key == pygame.K_d:
					self.player.right = False


	def music(self, music1 = 'Hello.ogg'):
			self.music1 = music1
			pygame.mixer.music.load(self.music1)
			pygame.mixer.music.play(loops = -1)
	def ret(self):
		for c in self.allBlocks:
			c.rect.x -= self.cam_x
			c.rect.y -= self.cam_y
		self.cam_y = 0
		self.cam_x = 0
		self.monster.rect.x = self.monster.g_x 
		self.monster.rect.y = self.monster.g_y 
		self.player.rect.x = self.player.start_x
		self.player.rect.y = self.player.start_y


	def update(self):
		if self.player.damage:
			self.player.health -= 1
			self.player.rect.y -= 144
			self.player.rect.x += 144
			self.player.damage = False
		if self.player.rect.x > MAP_RIGHT + 3*TILE_SIZE:
			self.ret()
			self.player.new()
			self.player.health -= 1
		if self.player.rect.x < - 3*TILE_SIZE:
			self.ret()
			self.player.new()
			self.player.health -= 1
		if self.player.rect.y > MAP_BOTTOM + 3* TILE_SIZE:
			self.ret()
			self.player.new()
			self.player.health -= 50
		self.back_x = -self.cam_x
		self.back_y = -self.cam_y
		file = open(self.map, 'r')
		if not self.lootBlocks:
			self.running = False
			self.player.sound.stop()
			self.counter += 1
			if self.counter < MAP_level_max:
				self.menu()
			else:
				self.win_menu()
		if self.player.health <= 0:
			self.player.sound.stop()
			self.counter = 1
			self.running = False
			self.music('Hello.ogg')
			self.deth_menu()
		self.playtime += self.clock.tick(self.fps) / 1000 # (!) добавить время текущего кадра ко времени всего раунда
		self.player.update(self.solidBlocks, self.lootBlocks, self.enemy, self.heal, self.keys)
		# self.monster.update(self.solidBlocks, self.lootBlocks, self.enemy, self.heal)
		pygame.display.set_caption("FPS: " + str(int(self.clock.get_fps()))) # (!) выведите в заголовок окна текущий ФПС
		self.camera()
	def draw(self):
		self.screen.blit(self.background, (self.back_x, self.back_y))
		self.allBlocks.draw(self.screen) # (!) нарисовать все блоки
		text =str(self.player.score) + ", playtime: " + "{0:.2f}".format(self.playtime)
		self.render_text(text, 48, 0)
		self.loot_draw()
		self.tabl.draw(self.screen)
		self.upd_d()
		self.Npc()


		pygame.display.update(self.upd_x1, self.upd_y1, self.upd_x2, self.upd_y2) # (!) обновить экран

	def render_text(self, text, x, y, color = Color.Red):
		surface = self.font.render(text, True, color) # (!) создайте "бумажку" с заданным текстом чёрного цвета в заданной координате
		self.screen.blit(surface, (x, y))

	def play(self):
		self.running = True
		self.music('F_music.ogg')
		while self.running:
			self.draw()
			self.get_events()
			self.update()
		for block in self.allBlocks: # (!) уничтожьте все блоки, они нам больше не нужны
			block.kill()
		self.playtime = float("{0:.2f}".format(self.playtime))

	def menu_update(self):
		self.clock.tick(self.fps)
		pygame.display.set_caption("FPS: " + str(int(self.clock.get_fps()))) # (!) выведите в заголовок окна текущий ФПС
		self.BACKGROUND = background_key[str(self.m_counter)]
		self.background = pygame.image.load(self.BACKGROUND["texture"])
		self.background = pygame.transform.scale(self.background, (MAP_RIGHT,MAP_BOTTOM))
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
					self.ret()
					self.load_map()
					self.player.new() # (!) установите игроку начальные параметры
					self.player.add(self.allBlocks)
					# self.monster.add(self.allBlocks)
					# self.monster.add(self.enemy)
					for b in self.allBlocks:
						b.rect.x -= 300
						b.rect.y -= 2000
					self.cam_y += 2000
					self.cam_x += 300
					self.play()


	def menu_deth_draw(self):
		self.counter = 1
		self.m_counter = "d"
		self.player.score = 0
		self.playtime = 0.0
		for block in self.allBlocks: # (!) уничтожьте все блоки, они нам больше не нужны
			block.kill()
		self.player.health = self.player.max_hp
		self.screen.blit(self.background, (self.back_x - 10*TILE_SIZE, self.back_y - 10*TILE_SIZE))
		self.render_text("Press P to play or Escape to Exit", 0, 0)
		text = "Game Over"
		self.render_text(text, 450, 300)

		pygame.display.update(self.upd_x1, self.upd_y1, self.upd_x2, self.upd_y2)

	def menu_draw(self):
		for block in self.allBlocks: # (!) уничтожьте все блоки, они нам больше не нужны
			block.kill()
		self.screen.blit(self.background, (self.back_x - 10*TILE_SIZE, self.back_y - 10*TILE_SIZE))
		if self.counter == 1:
			self.render_text("Press P to play or Escape to Exit", 0, 0)
		else:
			self.render_text("Press P to continue or Escape to Exit", 0, 0)


		pygame.display.update(self.upd_x1, self.upd_y1, self.upd_x2, self.upd_y2)

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
					self.ret()
					self.player.new() # (!) установите игроку начальные параметры
					self.player.add(self.allBlocks)
					# self.monster.add(self.allBlocks)
					# self.monster.add(self.enemy)
					for b in self.allBlocks:
						b.rect.x -= 300
						b.rect.y -= 2000
					self.cam_y += 2000
					self.cam_x += 300
					self.play()




	def win_menu(self):
		my_file = open("some.txt", "a")
		my_file.write(str("{0:.2f}".format(self.playtime)) + '\n')
		my_file.close()
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
		self.player.health = self.player.max_hp
		self.screen.blit(self.background, (self.back_x - 10*TILE_SIZE, self.back_y - 10*TILE_SIZE))
		self.render_text("Press P to restart or Escape to Exit", 0, 0)
		text = "YOU WIN !!!"
		self.render_text(text, 450, 300)

		pygame.display.update(self.upd_x1, self.upd_y1, self.upd_x2, self.upd_y2)



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