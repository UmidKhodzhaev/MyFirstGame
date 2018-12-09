# загружаем библиотеку pygame
import pygame
# загружаем отдельный файл с цветами
from colors import *
import os

winposx = 50
winposy = 50
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (winposx, winposy)

wall = "textures\\wall.png"
cloud = "textures\\cloud3.png"
sun = "textures\\sun.png"
blue_sky = "textures\\sky1.png"
grass = "textures\\grass.png"
air = "textures\\air4.png"
Hero = "textures\\hero4.png"
class block(pygame.sprite.Sprite):
    def __init__(self, x = 0, y = 0, textures = air):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(textures) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# описание игрового окна
class GameScreen():
	# инициализация окна
	def __init__(self, width, height, fps):
		# инициализация библиотеки pygame
		pygame.init()
		# размеры окна
		self.width = width
		self.height = height
		self.window_size = (width, height)

		self.tile_size = 100
		# создаём доску для бумажек
		self.screen = pygame.display.set_mode(self.window_size, pygame.DOUBLEBUF) 
		# создаём бумажку с задним фоном (на всю доску)
		self.background = pygame.Surface(self.screen.get_size())
		# волшебная строка, позволяющая ускорить отрисовку. все бумажки надо конвертировать
		self.allBlocks = pygame.sprite.Group()

		self.load_map()
		self.background.convert()		

		# максимальный фпс
		self.fps = fps
		# часы для контроля фпс	
		self.clock = pygame.time.Clock()
		# переменная, которая будет хранить время, прошедшее с запуска игры
		self.playtime = 0.0

		self.hetro = hetro()
		self.hetro.add(self.allBlocks)
		# и добавим сюда квадратик
		# self.kvadrat = Kvadratik()
		# self.player = Player()


	def load_map(self):
		file = open("map", 'r')
		for i, line in enumerate(file): # y
			for j, letter in enumerate(line): # x
				if letter == '1':
					block_temp = block(j*self.tile_size, i*self.tile_size, blue_sky) 
					block_temp.add(self.allBlocks)
				if letter == '2':
					block_temp = block(j*self.tile_size, i*self.tile_size, grass) 
					block_temp.add(self.allBlocks)
				if letter == ' ':
					block_temp = block(j*self.tile_size, i*self.tile_size, air) 
					block_temp.add(self.allBlocks)
				if letter == '3':
					block_temp = block(j*self.tile_size, i*self.tile_size, cloud) 
					block_temp.add(self.allBlocks)
				if letter == '4':
					block_temp = block(j*self.tile_size, i*self.tile_size, sun) 
					block_temp.add(self.allBlocks)
				if letter == "5":
					block_temp = block(j*self.tile_size, i*self.tile_size, wall) 
					block_temp.add(self.allBlocks)


	

	def run(self):
		# флаг, показывающий идёт ли игра
		running = True
		# бесконечный цикл игры
		while running:
			# ОБРАБОТКА СОБЫТИЙ
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						running = False
					if event.key == pygame.K_w:
						self.hetro.up = True
					if event.key == pygame.K_LSHIFT:
						self.hetro.acceleration = True
					if event.key == pygame.K_s:
						self.hetro.down = True
					if event.key == pygame.K_a:
						self.hetro.left = True
					if event.key == pygame.K_d:
						self.hetro.right = True
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LSHIFT:
						self.hetro.acceleration = False
					if event.key == pygame.K_w:
						self.hetro.up = False
					if event.key == pygame.K_s:
						self.hetro.down = False
					if event.key == pygame.K_a:
						self.hetro.left = False
					if event.key == pygame.K_d:
						self.hetro.right = False

			# ПРИМЕНИТЬ ДЕЙСТВИЯ


			# часики тикают и не позволяют тикать игре чаще, чем указанный фпс
			self.clock.tick(self.fps)
			
			self.hetro.update(self.height, self.width, self.hetro.speed)

			# ВЫПОЛНЯЕМ ОТРИСОВКУ
			# залили задний фон случайным цветом
			# self.background.fill(Orange)

			# прилепили задний фон на экран
			self.screen.blit(self.background, (0, 0)) # это 55 строка

			# self.player.draw(self.screen,100)
			# и туда же квадратик прилепим
			# self.player.draw(self.screen)
			

			self.allBlocks.draw(self.screen)
			# self.player.draw(self.screen) # а это 57

		
			pygame.display.flip()

# а теперь создадим квадратик
# квадратик это просто бумажка, которую мы создаём здесь, а потом отдаём экрану, чтобы он её выводил
# квадратик по сути ни чем не отличается от заднего фона
class hetro(block):
	def __init__(self, x = 0, y = 0, textures = Hero, speed = 10, width = 100, height = 22):
		pygame.sprite.Sprite.__init__(self)
		self.player = pygame.sprite.Group()
		self.image = pygame.image.load(textures) 
		self.rect = self.image.get_rect()
		self.speed = speed
		self.acceleration = self.up = self.down = self.left = self.right = False
		self.width = 22
		self.height = 100


	def load_hetro(self):
		hetro1 = hetro(22, 100, Hero)
		hetro1.add(self.player)
		self.player.draw(self.screen)

	def update(self, height, width, speed):
		if self.up and self.rect.y >= 0 + self.speed:
			self.rect.y -= self.speed
		if self.down and self.rect.y <= height - self.height - self.speed:
			self.rect.y += self.speed
		if self.left and self.rect.x >= 0 + self.speed:
			self.rect.x -= self.speed
		if self.right and self.rect.x <= width - self.width - self.speed:
			self.rect.x += self.speed
		if self.acceleration == True:
			self.speed = 25
		if self.acceleration == False:
			self.speed = 10


# class Player(block):
# 	def __init__(self, x = 0, y = 0, speed = 10, height = 100, width = 22):
# 		self.p_player = pygame.sprite.Group()
# 		self.x = x
# 		self.y = y
# 		self.speed = speed
# 		self.height = 100
# 		self.width = 22
# 		self.acceleration = self.up = self.down = self.left = self.right = False


# 	def update(self, height, width, speed):
# 		if self.up and self.y >= 0 + self.speed:
# 			self.y -= self.speed
# 		if self.down and self.y <= height - self.height - self.speed:
# 			self.y += self.speed
# 		if self.left and self.x >= 0 + self.speed:
# 			self.x -= self.speed
# 		if self.right and self.x <= width - self.width - self.speed:
# 			self.x += self.speed
# 		if self.acceleration == True:
# 			self.speed = speed * 2
# 		if self.acceleration == False:
# 			self.speed = speed


	



# class Kvadratik():
# 	# для бумажки нам нужно знать её размеры, координаты и цвет (далее будем делать картинками)
# 	def __init__(self, x = 50, y = 50, speed = 10, height = 200, width = 200, color = Orange):
# 		self.x = x
# 		self.y = y
# 		self.height = height
# 		self.width = width
# 		self.size = (self.width, self.height)
# 		self.color = color
# 		# создаём бумажку
# 		self.paper = pygame.Surface(self.size)
# 		self.paper.fill(self.color)
# 		self.speed = speed

# 		self.acceleration = self.up = self.down = self.left = self.right = False

# 	# рисуем бумажку на том, что нам подсунут
# 	def draw(self, surface):
# 		surface.blit(self.paper, (self.x, self.y))

# 	def update(self, height, width, speed):
# 		if self.up and self.y >= 0 + self.speed:
# 			self.y -= self.speed
# 		if self.down and self.y <= height - self.height - self.speed:
# 			self.y += self.speed
# 		if self.left and self.x >= 0 + self.speed:
# 			self.x -= self.speed
# 		if self.right and self.x <= width - self.width - self.speed:
# 			self.x += self.speed
# 		if self.acceleration == True:
# 			self.speed = speed * 2
# 		if self.acceleration == False:
# 			self.speed = speed

if __name__ == "__main__":
	# создали экземпляр игрового экрана
	game_screen = GameScreen(800, 600, 32)
	# запустили его
	game_screen.run()


"""
Домашнее задание
1. Адаптировать квадратик с учетом новых знаний
	(пронаследовать квадратик от блока и целеком его переписать)
2. Найти красивые тексурки для игрового персонажа и карты
	Kvadratik -> player
3. На карте должны присутствовать:
	- пол
	- стены
	- платформы
	- лут
4. Все спрайты хранятся в группе allblocks
	Дополнительно к этому есть отдельные группы:
		hardblocks - непроходимые блоки
		softblocks - проходимые блоки
		lootblocks - собирательные блоки
"""