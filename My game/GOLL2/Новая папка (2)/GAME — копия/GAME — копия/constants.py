winposx = 50
winposy = 50
tile_size = 50
width = 24*tile_size
height = 14*tile_size
fps = 60


nothing = "textures\\nothing.png"
bottom = "textures\\bottom.png"
bottom1 = "textures\\bottom1.png"
platforms = "textures\\platform.png"
bricks = "textures\\brick.png"
coin = "textures\\coin.png"
thorns = "textures\\shit.png"
enemy = "textures\\angry_shit.png"
kit = "textures\\kit.png"
health_full = "textures\\hud_heartFull.png"
health_half = "textures\\hud_heartHalf.png"
health_empty =  "textures\\hud_heartEmpty.png"
BACKGROUND = "textures\\background.png"
menu = "textures\\menu.png"

MAP_KEYS = {'1': nothing,
            '5': coin,
            '*': nothing,
            '+': kit,
            '>': nothing,
            '<': nothing,
            'x': nothing,
            'y': nothing,
            'B': nothing}

solidblocks = '1230iB<>'
coins = '5'
killerblocks = '*'
kitblocks = '+'
center_x = 'x'
center_y = 'y'
craiR = '>'
craiL = '<'
left_up_for_bg = 'B'

gravity = 1

level = {'1': 'map1',
	   '2': 'map2',
	   '3': 'map3'}

ANIMATION_DELAY = 0.05
ANIMATION_DELAY_JUMP = 0.1

ANIMATION_RIGHT = [('anim\\RunR\\0.png'),
                   ('anim\\RunR\\1.png'),
                   ('anim\\RunR\\2.png'),
                   ('anim\\RunR\\3.png'),
                   ('anim\\RunR\\4.png'),
                   ('anim\\RunR\\5.png'),
                   ('anim\\RunR\\6.png'),
                   ('anim\\RunR\\7.png'),
                   ('anim\\RunR\\8.png'),
                   ('anim\\RunR\\9.png'),
                   ('anim\\RunR\\10.png'),
                   ('anim\\RunR\\11.png'),
                   ('anim\\RunR\\12.png'),
                   ('anim\\RunR\\13.png'),
                   ('anim\\RunR\\14.png'),
                   ('anim\\RunR\\15.png'),]
ANIMATION_LEFT = [('anim\\RunL\\0.png'),
                  ('anim\\RunL\\1.png'),
                  ('anim\\RunL\\2.png'),
                  ('anim\\RunL\\3.png'),
                  ('anim\\RunL\\4.png'),
                  ('anim\\RunL\\5.png'),
                  ('anim\\RunL\\6.png'),
                  ('anim\\RunL\\7.png'),
                  ('anim\\RunL\\8.png'),
                  ('anim\\RunL\\9.png'),
                  ('anim\\RunL\\10.png'),
                  ('anim\\RunL\\11.png'),
                  ('anim\\RunL\\12.png'),
                  ('anim\\RunL\\13.png'),
                  ('anim\\RunL\\14.png'),
                  ('anim\\RunL\\15.png'),]

ANIMATION_CLOSE_JUMP_RIGHT = [('anim\\CloseJumpR\\0.png'),
                              ('anim\\CloseJumpR\\1.png')]
ANIMATION_CLOSE_JUMP_LEFT = [('anim\\CloseJumpL\\0.png'),
			           ('anim\\CloseJumpL\\1.png')]

ANIMATION_START_JUMP_RIGHT = [('anim\\StartJumpR\\0.png'),
                              ('anim\\StartJumpR\\1.png'),
                              ('anim\\StartJumpR\\2.png')]
ANIMATION_START_JUMP_LEFT = [('anim\\StartJumpL\\0.png'),
                             ('anim\\StartJumpL\\1.png'),
                             ('anim\\StartJumpL\\2.png')]

ANIMATION_STAY_RIGHT = [('anim\\StandR\\0.png'),
                        ('anim\\StandR\\1.png'),
                        ('anim\\StandR\\2.png'),
                        ('anim\\StandR\\3.png'),
                        ('anim\\StandR\\4.png'),
                        ('anim\\StandR\\5.png'),
                        ('anim\\StandR\\6.png'),
                        ('anim\\StandR\\7.png'),
                        ('anim\\StandR\\8.png'),
                        ('anim\\StandR\\9.png'),
                        ('anim\\StandR\\10.png'),
                        ('anim\\StandR\\11.png'),
                        ('anim\\StandR\\12.png')]
ANIMATION_STAY_LEFT = [('anim\\StandL\\0.png'),
                       ('anim\\StandL\\1.png'),
                       ('anim\\StandL\\2.png'),
                       ('anim\\StandL\\3.png'),
                       ('anim\\StandL\\4.png'),
                       ('anim\\StandL\\5.png'),
                       ('anim\\StandL\\6.png'),
                       ('anim\\StandL\\7.png'),
                       ('anim\\StandL\\8.png'),
                       ('anim\\StandL\\9.png'),
                       ('anim\\StandL\\10.png'),
                       ('anim\\StandL\\11.png'),
                       ('anim\\StandL\\12.png')]

COLOR =  "#888888"
