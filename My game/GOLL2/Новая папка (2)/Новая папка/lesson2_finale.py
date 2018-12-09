# загружаем библиотеку pygame
import pygame
# загружаем отдельный файл с цветами
from colors import *

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

		# создаём доску для бумажек
		self.screen = pygame.display.set_mode(self.window_size, pygame.DOUBLEBUF) 
		# создаём бумажку с задним фоном (на всю доску)
		self.background = pygame.Surface(self.screen.get_size())

		# волшебная строка, позволяющая ускорить отрисовку. все бумажки надо конвертировать

		self.tile_size = 50
		self.load_map()
		
		self.background.convert()		
		# максимальный фпс
		self.fps = fps
		# часы для контроля фпс	
		self.clock = pygame.time.Clock()
		# переменная, которая будет хранить время, прошедшее с запуска игры
		self.playtime = 0.0

		# и добавим сюда квадратик
		self.kvadrat = Kvadratik()

		

	def load_map(self):
		file = open("Map", "r")
		for i, line in enumerate(file): #y
			for j, letter in enumerate(line): #x
				if letter == "1":
					paper = pygame.Surface((self.tile_size, self.tile_size))
					paper.fill(DarkCyan)
					self.background.blit(paper, (j*self.tile_size, i*self.tile_size))
				if letter == " ":
					paper = pygame.Surface((self.tile_size, self.tile_size))
					paper.fill(Gray)
					self.background.blit(paper, (j*self.tile_size, i*self.tile_size))
				if letter == "2":
					paper = pygame.Surface((self.tile_size, self.tile_size))
					paper.fill(Mist)
					self.background.blit(paper, (j*self.tile_size, i*self.tile_size))
				

		# загрузить карту из файла в массив
		# отрисовываете карту по тайлам в зависимости от символов
		pass

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
						self.kvadrat.up = True
					if event.key == pygame.K_s:
						self.kvadrat.down = True
					if event.key == pygame.K_a:
						self.kvadrat.left = True
					if event.key == pygame.K_d:
						self.kvadrat.right = True
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_w:
						self.kvadrat.up = False
					if event.key == pygame.K_s:
						self.kvadrat.down = False
					if event.key == pygame.K_a:
						self.kvadrat.left = False
					if event.key == pygame.K_d:
						self.kvadrat.right = False

			# ПРИМЕНИТЬ ДЕЙСТВИЯ

			# часики тикают и не позволяют тикать игре чаще, чем указанный фпс
			self.clock.tick(self.fps)
			self.kvadrat.update(self.height, self.width)

			# ВЫПОЛНЯЕМ ОТРИСОВКУ
			# залили задний фон случайным цветом
			# self.background.fill(Orange)


			# self.load_map()

			# прилепили задний фон на экран
			self.screen.blit(self.background, (0, 0)) # это 55 строка
			# и туда же квадратик прилепим
			self.kvadrat.draw(self.screen) # а это 57

			# а теперь закомментите строки 55 и 57 (строки с прилеплением заднего фона и квадратика)
			# и раскомментите вот эти
			# self.kvadrat.draw(self.background)
			# self.screen.blit(self.background, (100, 100))
			# видите? ничего не изменилось!
			# вы можете лепить одни бумажки на другие. только учитывайте, что и координаты тогда идут бумажки,
			# на которой вы рисуете, а не координаты окна


			# но всё, что мы лепили, мы лепили на заднюю часть доски. а теперь мы её переворачиваем, чтобы пользователь увидел
			# 
			# если по умному, то есть у вас переменная screen, она хранит в себе всё то, что увидит пользователь.
			# в момент вызова метода flip screen передаёт дисплею всю картинку, и дисплей уже выводит картинку.
			# без вызова метода flip (или update) на экран ничего не попадёт
			pygame.display.flip()

# а теперь создадим квадратик
# квадратик это просто бумажка, которую мы создаём здесь, а потом отдаём экрану, чтобы он её выводил
# квадратик по сути ни чем не отличается от заднего фона
class Kvadratik():
	# для бумажки нам нужно знать её размеры, координаты и цвет (далее будем делать картинками)
	def __init__(self, x = 50, y = 50, height = 200, width = 200, color = White):
		self.x = x
		self.y = y
		self.height = height
		self.width = width
		self.size = (self.width, self.height)
		self.color = color
		# создаём бумажку
		self.paper = pygame.Surface(self.size)
		self.paper.fill(Silver)
		self.speed = 10

		self.up = self.down = self.left = self.right = False

	# рисуем бумажку на том, что нам подсунут
	def draw(self, surface):
		surface.blit(self.paper, (self.x, self.y))

	def update(self, height, width):
		if self.up and self.y >= 0 + self.speed:
			self.y -= self.speed
		if self.down and self.y <= height - self.height - self.speed:
			self.y += self.speed
		if self.left and self.x >= 0 + self.speed:
			self.x -= self.speed
		if self.right and self.x <= width - self.width - self.speed:
			self.x += self.speed








if __name__ == "__main__":
	# создали экземпляр игрового экрана
	game_screen = GameScreen(800, 600, 60)
	# запустили его
	game_screen.run()


# Задания на понимание
# 1) попробуйте поменять ФПС, посмотрите что будет
# 2) найдите все ошибки у себя в коде и объясните себе, в чём вы были не правы
# 3) если вы еще не делали дз и даже не притрагивались, вот вам задание:
# 	 заставьте этот квадрат двигаться с помощью событий нажатия клавиш и изменения координат квадратика
# 4) если остались вопросы, задавайте
