import pygame
import os

winposx = 50
winposy = 50
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (winposx, winposy)

BACKGROUND 		 = "textures\\background.bmp"
PLAYER_WALK 	 = "textures\\player_walk.png"
PLAYER_STAND 	 = "textures\\player_stand.png"
PLAYER_JUMP  	 = "textures\\player_jump.png"

class player_image(pygame.sprite.Sprite):
	def __init__(self, x = 100, y = 100):
		pygame.sprite.Sprite.__init__(self)
		self.left = self.right = self.up = False
		self.image_right = pygame.image.load(PLAYER_WALK)
		self.image_left = pygame.transform.flip(self.image_right, True, False)
		self.image_jump = pygame.image.load(PLAYER_JUMP)
		self.image_idle = pygame.image.load(PLAYER_STAND)
		self.image = self.image_right

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def update(self):
		if not self.left and not self.right and not self.up:
			self.image = self.image_idle
		elif self.up:
			self.image = self.image_jump
		elif self.right:
			self.image = self.image_right
		elif self.left:
			self.image = self.image_left

		

class GameScreen():
	def __init__(self, width, height, fps):
		pygame.init()
		self.screen = pygame.display.set_mode((width, height)) 
		self.background = pygame.image.load(BACKGROUND)
		self.background = pygame.transform.scale(self.background, self.screen.get_size())
		self.background.convert()
		self.fps = fps
		self.clock = pygame.time.Clock()
		self.playtime = 0.0
		self.player = player_image()
		self.allBlocks = pygame.sprite.Group()
		self.player.add(self.allBlocks)

	def update(self):
		self.clock.tick(self.fps)
		self.allBlocks.update()
		pygame.display.set_caption("FPS: "+str(int(self.clock.get_fps())))

	def get_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.running = False
				if event.key == pygame.K_w:
					self.player.up = True
				if event.key == pygame.K_d:
					self.player.right = True
				if event.key == pygame.K_a:
					self.player.left = True
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w:
					self.player.up = False
				if event.key == pygame.K_d:
					self.player.right = False
				if event.key == pygame.K_a:
					self.player.left = False

	def draw(self):
		self.screen.blit(self.background, (0, 0))
		self.allBlocks.draw(self.screen)
		pygame.display.flip()

	def run(self):
		self.running = True
		while self.running:
			self.get_events()
			self.update()
			self.draw()


if __name__ == "__main__":
	game_screen = GameScreen(50*24, 50*14, 60)
	game_screen.run()