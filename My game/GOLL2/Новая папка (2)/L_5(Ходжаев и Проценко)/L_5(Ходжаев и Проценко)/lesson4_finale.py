import pygame
from colors import *
import os

winposx = 50
winposy = 50
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (winposx, winposy)


blue_sky = "textures\\blue_sky.png"
wall = "textures\\wall.png"
coin = "textures\\coin2.png"
hero = "textures\\hero6.png"
air = "textures\\air.png"






chest = '4'
solidblocks = '23'
gravity = 0.981


class block(pygame.sprite.Sprite):
	def __init__(self, x = 0, y = 0, textures = air):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(textures)
		self.image.convert()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class player(pygame.sprite.Sprite):
	def __init__(self, x, y, score = 95):
		pygame.sprite.Sprite.__init__(self)
		self.score = score
		self.image_right = pygame.image.load(hero)
		self.image_left = pygame.transform.flip(self.image_right, True, False)
		self.image = self.image_right
		self.image.convert()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.up = self.left = self.right = False
		self.gor_speed = self.vert_speed = 0
		self.run_speed = 10
		self.jump_power = 19
		self.collided = False
		self.on_ground = False

	def update(self, hardBlocks, lootblocks):



		# if not self.left and not self.right and not self.up:
		# 	self.image = self.image_idle
		if self.right:
			self.image = self.image_right
		elif self.left:
			self.image = self.image_left

		if self.up and self.on_ground:
			self.vert_speed -= self.jump_power
		if self.collided == False:
			self.vert_speed += gravity
		self.rect.y += self.vert_speed
		self.vert_collide(self.vert_speed, hardBlocks, lootblocks)

		if self.left:
			self.gor_speed = -self.run_speed
		if self.right:
			self.gor_speed = +self.run_speed
		if (not self.left and not self.right) or (self.left and self.right):
			self.gor_speed = 0
		self.rect.x += self.gor_speed
		self.gor_collide(self.gor_speed, hardBlocks, lootblocks)

	def vert_collide(self, vert_speed, hardBlocks, lootblocks):
		self.collided = False
		self.on_ground = False
		for block in hardBlocks:
			if pygame.sprite.collide_rect(self, block):
				self.collided = True
				self.vert_speed = 0
				self.on_ground = True
				if vert_speed > 0:
					self.rect.bottom = block.rect.top
				if vert_speed < 0:
					self.rect.top = block.rect.bottom
					self.on_ground = False
		for block in lootblocks:
			if pygame.sprite.collide_rect(self, block):
				block.kill()
				self.score += 1


	def gor_collide(self, gor_speed, hardBlocks, lootblocks):
		for block in hardBlocks:
			if pygame.sprite.collide_rect(self, block):
				if gor_speed > 0:
					self.rect.right = block.rect.left
				if gor_speed < 0:
					self.rect.left = block.rect.right
		for block in lootblocks:
			if pygame.sprite.collide_rect(self, block):
				block.kill()
				self.score += 1









class GameScreen():
	def __init__(self, width, height, fps):
		pygame.font.init()
		pygame.init()
		self.tile_size = 50
		self.width = width
		self.height = height
		self.window_size = (width, height)
		self.screen = pygame.display.set_mode(self.window_size, pygame.DOUBLEBUF) 
		self.background_image=pygame.image.load("background.bmp").convert()
		self.allBlocks = pygame.sprite.Group()
		self.hardBlocks = pygame.sprite.Group()
		self.lootblocks = pygame.sprite.Group()
		self.load_map()
		# self.background.convert()		

		self.fps = fps
		self.clock = pygame.time.Clock()
		self.playtime = 0.0
		self.player = player(self.coor_y, self.coor_x)
		self.player.add(self.allBlocks)
		self.ran = True

				



	def obuchenie(self):
		if self.ran:
			font2=pygame.font.Font(None,30)
			scoretext2=font2.render("      A-Left      D-Right ", 1 , (Red))
			scoretext1=font2.render(" W-Up ", 1 , (Red))
			scoretext0=font2.render(" P.s. press TAB to Hide/Appear ", 1 , (Green))
			self.screen.blit(scoretext2, (150 , 185))
			self.screen.blit(scoretext1, (240 , 150))
			self.screen.blit(scoretext0, (300 , 230))





	def load_map(self):
		file = open("map", 'r')
		for i, line in enumerate(file): # y
			for j, letter in enumerate(line): # x
				if letter == '0':
						self.coor_x = i*self.tile_size
						self.coor_y = j*self.tile_size
				if letter == '1':
					block_temp = block(j*self.tile_size, i*self.tile_size, blue_sky) 
					block_temp.add(self.allBlocks)
					if letter in solidblocks:
						block_temp.add(self.hardBlocks)
					if letter in chest:
						block_temp.add(self.lootblocks)
				if letter == '2':
					block_temp = block(j*self.tile_size, i*self.tile_size, wall) 
					block_temp.add(self.allBlocks)
					if letter in solidblocks:
						block_temp.add(self.hardBlocks)
					if letter in chest:
						block_temp.add(self.lootblocks)
				if letter == '4':
					block_temp = block(j*self.tile_size, i*self.tile_size, coin) 
					block_temp.add(self.allBlocks)
					if letter in chest:
						block_temp.add(self.lootblocks)
					if letter in solidblocks:
						block_temp.add(self.hardBlocks)

	def run(self):
		file = open("map", 'r')
		running = True
		while running:
			# ОБРАБОТКА СОБЫТИЙ
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						running = False
					if event.key == pygame.K_w:
						self.player.up = True
					if event.key == pygame.K_s:
						self.player.down = True
					if event.key == pygame.K_a:
						self.player.left = True
					if event.key == pygame.K_d:
						self.player.right = True
					if event.key == pygame.K_TAB:
						if self.ran == True:
							self.ran = False
						elif self.ran == False:
							self.ran = True
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_w:
						self.player.up = False
					if event.key == pygame.K_s:
						self.player.down = False
					if event.key == pygame.K_a:
						self.player.left = False
					if event.key == pygame.K_d:
						self.player.right = False

			# ПРИМЕНИТЬ ДЕЙСТВИЯ

			self.clock.tick(self.fps)
			if self.player.score != 100 or self.player.on_ground == False:
				self.player.update(self.hardBlocks, self.lootblocks)
			pygame.display.set_caption("FPS: "+str(int(self.clock.get_fps())))

			# ВЫПОЛНЯЕМ ОТРИСОВКУ
			self.screen.blit(self.background_image, [0,0]) # это 55 строка
			self.obuchenie()

			
			self.allBlocks.draw(self.screen)
			font=pygame.font.Font(None,30)
			scoretext=font.render(" Score: " + str(self.player.score), 1 , (Black))
			self.screen.blit(scoretext, (10 , 10))
			if self.player.score == 100:
				font=pygame.font.Font(None,100)
				WINtext = font.render(" YOU WIN ", 1 , (Green))
				self.screen.blit(WINtext, (250 , 250))
				font2=pygame.font.Font(None,30)
				P_S_text = font2.render("P.S. <<Press ESC to quit>> ", 1 , (Black))
				self.screen.blit(P_S_text, (425 , 350))



			pygame.display.flip()
			
   	
			
if __name__ == "__main__":
	game_screen = GameScreen(800, 600, 300)
	# game_screen.Menu()
	game_screen.run()
"""
Домашнее задание
1. Адаптировать квадратик с учетом новых знаний
	(пронаследовать квадратик от блока и целеком его переписать)
2. Найти красивые тексурки для игрового персонажа и карты
	playerik -> player
3. На карте должны присутствовать:
	- пол
	- стены
	- платформы
	- лут
4. Все спрайты хранятся в группе allBlocks
	Дополнительно к этому есть отдельные группы:
		hardBlocks - непроходимые блоки
		softblocks - проходимые блоки
		lootblocks - собирательные блоки
"""
