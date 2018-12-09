import pygame
from Tkinter import
root = Tk()
canvas.pack()
root.mainloop()
pygame.init()


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
PURPLE= (148,   0, 211)

WINDOW_SIZE = (640, 480)
screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)

running = True


clock = pygame.time.Clock()
FPS = 30


playtime = 0.0


while running:







	#СОБЫТИЯ
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False	


			#ДЕЙСТВИЯ
		millisecond = clock.tick(FPS)
		playtime += millisecond/1000.0
		text = "FPS: " + str(FPS) + " playtime " + str(playtime)
		pygame.display.set_caption(text)

		square = canvas.create_rectangle(80,80,220,220, fill=Green)




			#ОТРИСОВКА
	background = pygame.Surface(screen.get_size())
	background.fill(PURPLE)
	background = background.convert()
	screen.blit(background, (0, 0))



	pygame.display.flip()
