# -*- coding:utf-8 -*-

import pygame
from Player import Player
from Platforms import Platform
from Buttons import Button

SIZE = (640, 480)

# создаем окно
window = pygame.display.set_mode(SIZE)
# создаем рабочую поверхность (игровой экран)
screen = pygame.Surface(SIZE)

# создаем героя
hero = Player(55, 55)
left = right = up = False

# создание уровня
level = [
    '---------------E',
    '-              -',
    '-              -',
    '-     ---      -',
    '-              -',
    '-              -',
    '-       ---    -',
    '-              -',
    '- --           -',
    '-     LBR      -',
    '-              -',
    '----------------']

sprite_group = pygame.sprite.Group()
sprite_group.add(hero)
platfroms = []
btnGroup = pygame.sprite.Group()

x = 0
y = 0
for row in level:
    for col in row:
        if col == '-':
            pl = Platform(x, y)
            sprite_group.add(pl)
            platfroms.append(pl)
        if col == 'B':
            btn = Button(x, y, 40, 40, text='B')
            btnGroup.add(btn)
            platfroms.append(btn)
        if col == 'L':
            btnL = Button(x, y, 40, 40, text='L')
            btnGroup.add(btnL)
            platfroms.append(btnL)
        if col == 'R':
            btnR = Button(x, y, 40, 40, text='R')
            btnGroup.add(btnR)
            platfroms.append(btnR)
        if col == 'E':
            btnE = Button(x, y, 40, 40, text='E', color=(150, 50, 50))
            btnGroup.add(btnE)
            platfroms.append(btnE)
        x += 40
    y += 40
    x = 0

# открываем игровой цикл
done = True
timer = pygame.time.Clock()
while done:
    # блок управления событиями
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                left = True
            if e.key == pygame.K_RIGHT:
                right = True
            if e.key == pygame.K_UP:
                up = True

        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                left = False
            if e.key == pygame.K_RIGHT:
                right = False
            if e.key == pygame.K_UP:
                up = False

    if pygame.mouse.get_pressed() == (1, 0, 0):
        mouse_click = True
    else:
        mouse_click = False

    # закрашиваем рабочую поверхность
    screen.fill((10, 120, 10))

    # отображение героя
    hero.update(left, right, up, platfroms)
    sprite_group.draw(screen)

    # отображение кнопок
    btnGroup.update()
    btnGroup.draw(screen)
    if btn.onClick(mouse_click):
        hero.yvel = -10
    if btnL.onClick(mouse_click):
        left = True
    else:
        left = False
    if btnR.onClick(mouse_click):
        right = True
    else:
        right = False
    if btnE.onClick(mouse_click):
        done = False


    # отображаем рабочую поверхность в окне
    window.blit(screen,(0, 0))
    # обновляем окно
    pygame.display.flip()
    timer.tick(60)