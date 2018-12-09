import pygame
from pygame import *
import pyganim
import os
from colors import*
from constants import*


os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (winposx, winposy)

class block(pygame.sprite.Sprite):
	def __init__(self, x = 0, y = 0, textures = bottom):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(textures)
		self.image.convert()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

#class NPC(block):
#	def __init__(self, x = 0, y = 0, textures = coin):
#		block.__init__(self, x = 200, y = 200, textures = coin)
		

class player(pygame.sprite.Sprite):
	def __init__(self, coords = (0, 0)):
		pygame.sprite.Sprite.__init__(self)
		self.image = Surface((50,120))
		self.image.fill(Color(COLOR))
		self.image.set_colorkey(Color(COLOR))

		boltAnim = []
		for anim in ANIMATION_RIGHT:
		   boltAnim.append((anim, ANIMATION_DELAY))
		self.boltAnimRight = pyganim.PygAnimation(boltAnim)
		self.boltAnimRight.play()  

		boltAnim = []
		for anim in ANIMATION_LEFT:
		   boltAnim.append((anim, ANIMATION_DELAY))
		self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
		self.boltAnimLeft.play()

		boltAnim = []
		for anim in ANIMATION_STAY_LEFT:
			boltAnim.append((anim, ANIMATION_DELAY))
		self.boltAnimStayLeft = pyganim.PygAnimation(boltAnim)
		self.boltAnimStayLeft.play()

		boltAnim = []
		for anim in ANIMATION_STAY_RIGHT:
			boltAnim.append((anim, ANIMATION_DELAY))
		self.boltAnimStayRight = pyganim.PygAnimation(boltAnim)
		self.boltAnimStayRight.play()
		        
		boltAnim = []
		for anim in ANIMATION_START_JUMP_LEFT:
			boltAnim.append((anim, ANIMATION_DELAY_JUMP))
		self.boltAnimStartJumpLeft= pyganim.PygAnimation(boltAnim)
		self.boltAnimStartJumpLeft.play()

		boltAnim = []
		for anim in ANIMATION_CLOSE_JUMP_LEFT:
			boltAnim.append((anim, ANIMATION_DELAY_JUMP))
		self.boltAnimCloseJumpLeft = pyganim.PygAnimation(boltAnim)
		self.boltAnimCloseJumpLeft.play()
		        
		boltAnim = []
		for anim in ANIMATION_START_JUMP_RIGHT:
			boltAnim.append((anim, ANIMATION_DELAY_JUMP))
		self.boltAnimStartJumpRight = pyganim.PygAnimation(boltAnim)
		self.boltAnimStartJumpRight.play()

		boltAnim = []
		for anim in ANIMATION_CLOSE_JUMP_RIGHT:
			boltAnim.append((anim, ANIMATION_DELAY_JUMP))
		self.boltAnimCloseJumpRight = pyganim.PygAnimation(boltAnim)
		self.boltAnimCloseJumpRight.play()

		self.image_health_full = pygame.image.load(health_full)
		self.image_health_empty = pygame.image.load(health_empty)
		self.image_health_half = pygame.image.load(health_half)

		self.image = pygame.transform.scale(self.image,(80, 85)).convert()

		self.health_image = self.image_health_full
		self.health_image2 = self.image_health_full
		self.health_image3 = self.image_health_full

		self.rect = self.image.get_rect()
		self.starting_point = (0, 0)
		self.new(coords)
		self.max_coins = 0
		self.death = False

	def new(self, coords):
		self.health_image1 = self.image_health_full
		self.image_health_full1 = pygame.image.load(health_full)
		self.image_health_full2 = pygame.image.load(health_full)
		self.spawn_xy = coords
		self.rect.x = self.spawn_xy[0]
		self.rect.y = self.spawn_xy[1]
		self.up = self.left = self.right = False
		self.hor_speed = self.vert_speed = 0
		self.speed = 7
		self.jump_power = 22
		self.collided = False
		self.on_ground = False
		self.coins = coins = 0
		self.dir = 'right'
		self.hp = 6

	def respawn(self, coords):
		self.spawn_xy = coords
		self.rect.x = self.spawn_xy[0]
		self.rect.y = self.spawn_xy[1]


	def update(self, hardBlocks, lootBlocks, killerBlocks, kitBlocks):
###
		health = {'1': self.image_health_full,
					'2': self.image_health_half,
					'3': self.image_health_empty}
		if self.hp == 1:
			self.health_image = health['2']
			self.health_image2 = health['3']
			self.health_image3 = health['3']
		if self.hp == 2:
			self.health_image = health['1']
			self.health_image2 = health['3']
			self.health_image3 = health['3']
		if self.hp == 3:
			self.health_image = health['1']
			self.health_image2 = health['2']
			self.health_image3 = health['3']
		if self.hp == 4:
			self.health_image = health['1']
			self.health_image2 = health['1']
			self.health_image3 = health['3']
		if self.hp == 5:
			self.health_image = health['1']
			self.health_image2 = health['1']
			self.health_image3 = health['2']
		if self.hp == 6:
			self.health_image = health['1']
			self.health_image2 = health['1']
			self.health_image3 = health['1']
###
		if not self.collided:
			self.vert_speed += gravity
		if self.up and self.on_ground:
			self.vert_speed = -self.jump_power
		if self.left:
			self.dir = 'left'
			self.hor_speed = -self.speed
		if self.right:
			self.dir = 'right'
			self.hor_speed = self.speed

		if not self.right and not self.left:
			self.hor_speed = 0

		self.rect.y += self.vert_speed
		self.vert_collide(self.vert_speed, hardBlocks)

		self.rect.x += self.hor_speed
		self.hor_collide(self.hor_speed, hardBlocks)
		self.image.fill(Color(COLOR))
		if self.vert_speed != 0 or self.vert_speed == 0 and not self.on_ground and not self.prev_collided:
			if self.dir == 'left':
				if self.vert_speed <= 0:
					self.boltAnimStartJumpLeft.blit(self.image, (0, 0))
				elif self.vert_speed > 0:
					self.boltAnimCloseJumpLeft.blit(self.image, (0, 0))
			else:
				if self.vert_speed <= 0:
					self.boltAnimStartJumpRight.blit(self.image, (0, 0))
				elif self.vert_speed > 0:
					self.boltAnimCloseJumpRight.blit(self.image, (0, 0))
		else:
			if self.hor_speed != 0:	
				if self.dir == 'left':
					self.boltAnimLeft.blit(self.image, (0, 0))
				else:
					self.boltAnimRight.blit(self.image, (0, 0))
			else:
				if self.dir == 'left':
					self.boltAnimStayLeft.blit(self.image, (0, 0))
				else:
					self.boltAnimStayRight.blit(self.image, (0, 0))
		self.prev_collided = self.collided
		for block in lootBlocks:
			if pygame.sprite.collide_rect(self, block):
				self.coins += 1
				block.kill()
		for block in killerBlocks:
			if pygame.sprite.collide_rect(self, block):
				self.hp -= 1
				self.respawn((100,100))
		for block in kitBlocks:
			if pygame.sprite.collide_rect(self, block):
				if self.hp < 6:
					self.hp += 1
					block.kill()
				


	def vert_collide(self, vert_speed, hardBlocks):
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
		

	def hor_collide(self, hor_speed, hardBlocks):
		for block in hardBlocks:
			if pygame.sprite.collide_rect(self, block):
				if hor_speed > 0:
					self.rect.right = block.rect.left
				if hor_speed < 0:
					self.rect.left = block.rect.right



class GameScreen():
	def __init__(self, width, height, fps):
		pygame.init()
		self.map = 'map1'
		self.lvl = 1
		self.counter = 1
		self.finish = False
		self.screen = pygame.display.set_mode((width, height))
		self.men = pygame.image.load(menu)
		self.men = pygame.transform.scale(self.men, self.screen.get_size())
		self.background = pygame.image.load(BACKGROUND)
		self.background.convert()
		self.rect_bg = self.background.get_rect()
		self.rect_bg.x = 0
		self.rect_bg.y = 0
		self.fps = fps
		self.font = pygame.font.SysFont("Fixedsys", int(tile_size/5*4))
		self.clock = pygame.time.Clock()
		self.playtime = 0.0
		self.player = player()
		self.enemies = pygame.sprite.Group()
		self.allBlocks = pygame.sprite.Group()
		self.hardBlocks = pygame.sprite.Group()
		self.lootBlocks = pygame.sprite.Group()
		self.center_x = pygame.sprite.Group()
		self.center_y = pygame.sprite.Group()
		self.left_up_for_bg = pygame.sprite.Group()
		self.killerBlocks = pygame.sprite.Group()
		self.craiR = pygame.sprite.Group() 
		self.craiL = pygame.sprite.Group() 
		self.moveR = pygame.sprite.Group() 
		self.moveL = pygame.sprite.Group() 
		self.kitBlocks = pygame.sprite.Group()
		self.camera_hor = self.camera_vert = False
		self.camera_hor_speed = self.camera_vert_speed = 7
		self.R=True
		self.L=False
		self.enemies_speed = 5
		self.cam_x=0
		self.cam_y=0

	def load_map(self):
		if self.player.coins != self.player.max_coins:
			self.counter = 1
		self.map = level[str(self.counter)]
		self.lvl = self.counter
		file = open(self.map, 'r')
		for i, line in enumerate(file): # y
			for j, letter in enumerate(line): # x
				if letter == '1':
					block_temp = block(j*tile_size, i*tile_size, nothing) 
					block_temp.add(self.allBlocks)
					if letter in solidblocks:
						block_temp.add(self.hardBlocks)
				if letter == '2':
					block_temp = block(j*tile_size, i*tile_size, bottom) 
					block_temp.add(self.allBlocks)
					if letter in solidblocks:
						block_temp.add(self.hardBlocks)
				if letter == '3':
					block_temp = block(j*tile_size, i*tile_size, bottom1) 
					block_temp.add(self.allBlocks)
					if letter in solidblocks:
						block_temp.add(self.hardBlocks)
				if letter == '0':
				 	block_temp = block(j*tile_size, i*tile_size, bricks) 
				 	block_temp.add(self.allBlocks)
				 	if letter in solidblocks:
				 		block_temp.add(self.hardBlocks)
				if letter == '5':
					block_temp = block(j*tile_size, i*tile_size, coin)
					block_temp.add(self.allBlocks)
					if letter in coins:
						block_temp.add(self.lootBlocks)
						self.player.max_coins += 1
				if letter == "*":
					block_temp = block(j*tile_size, i*tile_size, nothing)
					block_temp.add(self.allBlocks)
					if letter in killerblocks:
						block_temp.add(self.killerBlocks)
				if letter == "+":
					block_temp = block(j*tile_size, i*tile_size, kit)
					block_temp.add(self.allBlocks)
					if letter in kitblocks: 
						block_temp.add(self.kitBlocks)
				if letter == ">":
					block_temp = block(j*tile_size, i*tile_size, nothing)
					block_temp.add(self.allBlocks)
					if letter in points:
						block_temp.add(self.craiR)
					if letter in solidblocks:
				 		block_temp.add(self.hardBlocks)
				if letter == "<":
					block_temp = block(j*tile_size, i*tile_size, nothing)
					block_temp.add(self.allBlocks)
					if letter in points:
						block_temp.add(self.craiL)
					if letter in solidblocks:
				 		block_temp.add(self.hardBlocks)
				if letter == "i":
					block_temp = block(j*tile_size, i*tile_size, nothing)
					block_temp.add(self.allBlocks)
					if letter in points:
						block_temp.add(self.center_x)
					if letter in solidblocks:
				 		block_temp.add(self.hardBlocks)
				if letter == "o":
					block_temp = block(j*tile_size, i*tile_size, nothing)
					block_temp.add(self.allBlocks)
					if letter in points:
						block_temp.add(self.center_y)
					if letter in solidblocks:
				 		block_temp.add(self.hardBlocks)
				if letter == "e":
					block_temp = block(j*tile_size, i*tile_size, enemy)
					block_temp.add(self.allBlocks)
					if letter in enemies:
						block_temp.add(self.enemies)
					if letter in killerblocks:
						block_temp.add(self.killerBlocks)
				if letter == "-":
					block_temp = block(j*tile_size, i*tile_size, nothing)
					block_temp.add(self.allBlocks)
					if letter in move:
						block_temp.add(self.moveL)
				if letter == "=":
					block_temp = block(j*tile_size, i*tile_size, nothing)
					block_temp.add(self.allBlocks)
					if letter in move:
						block_temp.add(self.moveR)
				if letter == "B":
					block_temp = block(j*tile_size, i*tile_size, nothing)
					block_temp.add(self.allBlocks)
					if letter in points:
						block_temp.add(self.left_up_for_bg)
					if letter in solidblocks:
				 		block_temp.add(self.hardBlocks)
				if letter == 'H':	
					self.player.starting_point = (j*tile_size, i*tile_size)

	def game_buttons(self):
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
					self.player.right = False
				if event.key == pygame.K_d:
					self.player.right = True
					self.player.left = False
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w:
					self.player.up = False
				if event.key == pygame.K_a:
					self.player.left = False
				if event.key == pygame.K_d:
					self.player.right = False

	def camera(self):
		self.camera_update()
		"""
		self.cam_x+=self.player.hor_speed
		self.cam_y+=self.player.vert_speed
		if self.player.death == True:
			for b in self.allBlocks:
				b.rect.x+=self.cam_x
				b.rect.y+=self.cam_y
			self.cam_x=0
			self.cam_y=0
			self.player.death = False
		"""
		if self.player.rect.y > height/2:
			for b in self.allBlocks:
				b.rect.y-=self.camera_vert_speed
		if self.player.rect.y < height/2-tile_size:
			for b in self.allBlocks:
				b.rect.y+=self.camera_vert_speed
		if self.player.rect.x > width/2:
			for b in self.allBlocks:
				b.rect.x-=self.camera_hor_speed
		if self.player.rect.x < width/2:
			for b in self.allBlocks:
				b.rect.x+=self.camera_hor_speed
		for b in self.left_up_for_bg:
			self.rect_bg.x = b.rect.x
			self.rect_bg.y = b.rect.y

	def camera_update(self): 
		for a in self.craiL:
			if a.rect.x >= 0 and self.player.rect.x <= width/2:
				self.camera_hor = False
			else:
				self.camera_hor = True
			if self.player.rect.y > a.rect.y:
				self.player.hp-=1
				self.player.respawn((100,100))
		for y in self.center_y:
			if self.player.rect.y > y.rect.y:
				for a in self.craiL:
					if a.rect.y <= height-tile_size+10 and self.player.rect.y > height/2:
						self.camera_vert = False
					else:
						self.camera_vert = True
			else:
				for c in self.left_up_for_bg:
					if c.rect.y >= 0:
						self.camera_vert = False
					if self.player.rect.y > height/2:
						self.camera_vert = True
		for x in self.center_x:
			if self.player.rect.x >= x.rect.x:
				for a in self.craiR:
					if a.rect.x <= width-tile_size+3 and self.player.rect.x >= width/2:
						self.camera_hor = False
					else:
						self.camera_hor = True
		
		if self.camera_hor:
			self.camera_hor_speed=7
		else:
			self.camera_hor_speed=0
		if self.camera_vert:
			self.camera_vert_speed=7
		else:
			self.camera_vert_speed=0

	def enemy(self):
		for g in self.enemies:
			for b in self.moveR:
				if g.rect.x == b.rect.x:
					self.R = True
					self.L = False
		for g in self.enemies:
			for b in self.moveL:
				if g.rect.x == b.rect.x:
					self.R = False
					self.L = True
				if self.R:
					g.rect.x -= self.enemies_speed
				if self.L:
					g.rect.x += self.enemies_speed
		

	def update(self):
		self.playtime += self.clock.tick(self.fps) / 1000
		self.player.update(self.hardBlocks, self.lootBlocks, self.killerBlocks, self.kitBlocks)
		self.enemy()
		self.camera()
		pygame.display.set_caption("FPS: " + str(int(self.clock.get_fps())))
		if not self.lootBlocks or self.player.hp <= 0:
			self.running = False
			if self.player.hp > 0 and self.counter < 3:
				self.counter += 1
			else:
				self.counter = 1

	def draw(self):
		self.screen.blit(self.background, (self.rect_bg.x, self.rect_bg.y))
		self.allBlocks.draw(self.screen)
		self.screen.blit(self.player.health_image, (tile_size, 0))
		self.screen.blit(self.player.health_image2, (2*tile_size, 0))
		self.screen.blit(self.player.health_image3, (3*tile_size, 0))
		coins = "Coins " + str(self.player.coins) 
		level = "Level " + str(self.lvl) 
		time = "Time " + "{0:.2f}".format(self.playtime) 
		pos = str(self.player.rect.x) + " " + str(self.player.rect.y)
		pos_cam = str(self.cam_x) + " " + str(self.cam_y)
		self.render_text(coins, tile_size, 2*tile_size)
		self.render_text(level, tile_size, tile_size)
		self.render_text(time, tile_size, 1.5*tile_size)
		self.render_text(pos, tile_size, 2.5*tile_size)
		self.render_text(pos_cam, tile_size, 3*tile_size)
		pygame.display.update()

	def run(self):
		self.running = True
		self.playtime = 0.0
		while self.running:
			self.game_buttons()
			self.update()
			self.draw()
		for block in self.allBlocks:
			block.kill()
		self.playtime = float("{0:.2f}".format(self.playtime))

	def render_text(self, text, x, y):
		surface = self.font.render(text, True, White) 
		self.screen.blit(surface, (x, y))

	def menu_draw(self):
		self.screen.blit(self.men, (0, 0))
		self.render_text("Press ENTER to play or ESC to Exit", 0, 0)
		text = "Last time you beat it in " + str(self.playtime) + " seconds"
		self.render_text(text, 0, tile_size)
		if self.lvl==3:
			win = "You won!"
			self.render_text(win, 0, 2*tile_size)
		if self.player.hp<1:
			lose = "You lost."
			self.render_text(lose, 0, 2*tile_size)
		pygame.display.update()

	def menu_update(self):
		self.clock.tick(self.fps)
		pygame.display.set_caption("GAME | FPS: "+ str(int(self.clock.get_fps())))

	def menu_buttons(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.menu_running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.menu_running = False
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_RETURN:
					self.load_map()
					self.player.new(self.player.starting_point)
					self.player.add(self.allBlocks)
					self.run()

	def menu(self):
		self.menu_running = True
		while self.menu_running:
			self.menu_buttons()
			self.menu_update()
			self.menu_draw()

if __name__ == "__main__":
	GameScreen(width, height, fps).menu()

