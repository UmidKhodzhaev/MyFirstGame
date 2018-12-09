import pygame
pygame.init()

#		 RED GREEN BLUE
BLACK  = (  0, 	 0,	  0)
WHITE  = (255, 255, 255) # 255_10 = 11111111_2
RED    = (255,   0,   0)
PURPLE = (148,   0, 211)

WINDOW_SIZE = (640, 480)
screen = pygame.display.set_mode(WINDOW_SIZE) # создание окна

clock = pygame.time.Clock()
FPS = 1000
playtime = 0.0
running = True

while running:
	# СОБЫТИЯ
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # событие закрытия окна
			running = False

	# ДЕЙСТВИЯ
	milliseconds = clock.tick(FPS)
	playtime += milliseconds / 1000.0
	text = "FPS: " + str(FPS) + " playtime " + str(playtime)
	pygame.display.set_caption(text)

	# ОТРИСОВКА
	background = pygame.Surface(screen.get_size())
	background.fill(PURPLE)
	background = background.convert()

	screen.blit(background, (0, 0))



	pygame.display.flip()

