import pygame
# ПАРАМЕТРЫ ОКНА
FPS = 60
TILE_SIZE = 48
WIN_WIDTH = 1000
WIN_HEIGHT = 800
WIN_POS_X = 50
WIN_POS_Y = 50
COLOR = (255, 255, 255)


# ТЕКСТУРЫ КАРТЫ
# rect обозначает, что картинку нужно взять не всю, а только маленький квадратик
# но если rect = 0, то надо взять всю
# подробнее смотрите в описании класса block
BLUE_SKY = {"texture": "textures\\tiles.png",
            "rect": (2 * 16, 24 * 16, 16, 16)}
GRASS = {"texture": "textures\\Fan\\1.png",
         "rect": 0}
Door1 = {"texture": "textures\\Doors\\Door.png",
         "rect": 0}
Door2 = {"texture": "textures\\Doors\\Door2.png",
         "rect": 0}
SOUL = {"texture": "textures\\money\\m.png",
         "rect": 0}
# PLATFORM = {"texture": "textures\\tile2s.bmp",
#             "rect": (2 * 16, 16 * 16, 16, 16)}
PLATFORM = {"texture": "textures\\Fan\\4.png",
            "rect": 0}
PLATFORM2 = {"texture": "textures\\solid\\3.bmp",
            "rect": 0}
BRIDGE = {"texture": "textures\\Fan\\0.png",
            "rect": 0}
HALF_BRIDGE = {"texture": "textures\\solid\\n.png",
            "rect": 0}
HALF2_BRIDGE = {"texture": "textures2\\Block_k.png",
            "rect": 0}
WALL = {"texture": "textures\\tile2s.bmp",
        "rect": (2 * 16, 20 * 16, 16, 16)}
COIN = {"texture": "textures\\money\\m.png",
        "rect": 0}
WOOD = {"texture": "textures\\solid\\2.bmp",
        "rect": 0}
WATER_SPIKES= {'texture': "textures\\solid\\w.png",
          'rect': 0}
BACKGROUND_level1 = {"texture": "textures\\Background.bmp",
              "rect": 0}
SPIKES = {'texture': "textures\\enemy_b\\t.png",
          'rect': 0}
BEAM = {'texture': "textures\\solid\\g.png",
          'rect': 0}
LEAF_SPIKES = {'texture': "textures\\solid\\l.png",
          'rect': 0}
HHH = {'texture': "textures\\mosney\\н.png",
          'rect': 0}
MMM = {'texture': "textures\\money\\м.png",
          'rect': 0}
YYY = {'texture': "textures\\Fan\\y.png",
          'rect': 0}
UUU = {'texture': "textures\\Fan\\u.png",
          'rect': 0}
CCC = {'texture': "textures\\Fan\\c.png",
          'rect': 0}
NINE = {'texture': "textures\\Fan\\9.png",
          'rect': 0}


HEART_FULL = {'texture': "textures\\Hp.png",
          'rect': 0}

# ТЕКСТУРЫ ИГРОКА

JIIINGO = {"texture": "textures2\\Jiiingo.png",
            "rect": 0}

HEAL = {'texture': "textures2\\Block_h.png",
          'rect': 0}

MAP_level = {'1': 'level1',
             }
MAP_level_max = 2
MAP_RIGHT = 41*TILE_SIZE
MAP_BOTTOM = 58*TILE_SIZE


TOP_SPIKES = {"texture": "textures\\LR\\x.png",
            "rect": 0}
ROOF_SPIKES = {"texture": "textures\\solid\\r.png",
            "rect": 0}
KORM2 = {"texture": "textures\\solid\\e.png",
            "rect": 0}
WAL = {"texture": "textures\\enemy_b\\d.png",
            "rect": 0}
KORM = {"texture": "textures\\Fan\\i.png",
            "rect": 0}
KORM3 = {"texture": "textures\\LR\\z.png",
            "rect": 0}
PLAT = {"texture": "textures\\enemy_b\\v.png",
            "rect": 0}
STONE = {"texture": "textures\\solid\\q.png",
            "rect": 0}
Scale4 = {"texture": "textures\\Scale4.png",
            "rect": 0}
Scale2 = {"texture": "textures\\Scale2.png",
            "rect": 0}
Scale3 = {"texture": "textures\\Scale3.png",
            "rect": 0}
Scale5 = {"texture": "textures\\Scale5.png",
            "rect": 0}
Scale1 = {"texture": "textures\\Scale1.png",
            "rect": 0}
Key1 = {"texture": "textures\\Keys\\Key.png",
            "rect": 0}
Npc1 = {"texture": "textures\\Npc\\Npc1.png",
            "rect": 0}

SCALE_KEY ={'1':Scale1,
            '2':Scale2,
            '3':Scale3,
            '4':Scale4,
            '5':Scale5
}


# ОБОЗНАЧЕНИЯ ЭЛЕМЕНТОВ КАРТЫ
# удобно для загрузки карты
MAP_KEYS = {'0': BRIDGE,
            '1': GRASS,
            '2': WOOD,
            '3': PLATFORM2,
            '4': PLATFORM,
            't': SPIKES,
            'c': CCC,
            '9': NINE,
            'n': HALF_BRIDGE,
            'w': WATER_SPIKES,
            'l': LEAF_SPIKES,
            'k': HALF2_BRIDGE,
            'g': BEAM,
            'h': HEAL,
            'u': UUU,
            'y': YYY,
            'н': HHH,
            'M': MMM,
            'x': TOP_SPIKES,
            'd': WAL,
            'm': COIN,
            'v': PLAT,
            'i': KORM,
            'e': KORM2,
            'q': STONE,
            'r': ROOF_SPIKES,
            'z': KORM3,
            'D': Door1,
            '7': Door2,
            'K': Key1,
            'N': Npc1}


BACKGROUND_D = {"texture": "textures\\Dmenu_background.bmp",
              "rect": 0}
BACKGROUND_M = {"texture": "textures\\menu_background.bmp",
              "rect": 0}
BACKGROUND_W = {"texture": "textures\\Wmenu_background.bmp",
              "rect": 0}



background_key = {'0' : BACKGROUND_M,
                  '1' : BACKGROUND_level1,
                  'd' : BACKGROUND_D,
                  'w' : BACKGROUND_W}

Tabl1 = {"texture": "textures\\Tabl\\Tabl_1.png",
            "rect": 0}
Tabl2 = {"texture": "textures\\Tabl\\Tabl_2.png",
            "rect": 0}
Tabl3 = {"texture": "textures\\Tabl\\Tabl_3.png",
            "rect": 0}
Tabl4 = {"texture": "textures\\Tabl\\Tabl_4.png",
            "rect": 0}
Tabl5 = {"texture": "textures\\Tabl\\Tabl_5.png",
            "rect": 0}
Tabl6 = {"texture": "textures\\Tabl\\Tabl_6.png",
            "rect": 0}
Tabl7 = {"texture": "textures\\Tabl\\Tabl_7.png",
            "rect": 0}
Tabl8 = {"texture": "textures\\Tabl\\Tabl_8.png",
            "rect": 0}
Tabl9 = {"texture": "textures\\Tabl\\Tabl_9.png",
            "rect": 0}

Tabl_keys = {'0' : Tabl1,
             '1' : Tabl2,
             '2' : Tabl3,
             '3' : Tabl4,
             '4' : Tabl5,
             '5' : Tabl6,
             '6' : Tabl7,
             '7' : Tabl8,
             '8' : Tabl9}



SOLID_BLOCKS = '236nkfuNgliqyezcyw7qкrxD'
LOOT_BLOCKS = 'mMн'
Enemy = 'tvdJ'
HEAL_BLOCKS = "h"
DOORS = 'D7'
KEYS = 'K'
NPC = 'N'

# ПАРАМЕТРЫ МИРА
GRAVITY = 1

PLAYER_STAND = {"texture": "textures\\UNNAME.png",
                "rect": 0}
PLAYER_JUMP = {"texture": "textures\\UNNAME_JUMP_V1.png",
               "rect": 0}
PLAYER_WALK_R1 = {"texture": "textures\\UNNAME_WALK_V1.png",
               "rect": 0}

ANIMATION_DELAY = 0.1 # скорость смены кадров
ANIMATION_RIGHT = [("textures\\Unname\\UNNAME_WALK_1.png"),
                   ("textures\\Unname\\UNNAME_WALK_2.png"),
                   ("textures\\Unname\\UNNAME_WALK_3.png"),
                   ("textures\\Unname\\UNNAME_WALK_4.png")]
ANIMATION_STAY = [("textures\\Unname\\UNNAME.png"),
                  ("textures\\Unname\\UNNAME_2.png"),
                  ("textures\\Unname\\UNNAME_3.png"),
                  ("textures\\Unname\\UNNAME_4.png")]
ANIMATION_LEFT =[("textures\\Unname\\UNNAME_WALK_L1.png"),
                  ("textures\\Unname\\UNNAME_JUMP_V2.png"),
                  ("textures\\Unname\\UNNAME_JUMP_V3.png"),
                  ("textures\\Unname\\UNNAME_JUMP_V4.png")]
ANIMATION_JUMP = [("textures\\UNNAME_JUMP_V1.png", 0.1)]
ANIMATION_JUMP_LEFT = [("textures\\UNNAME_JUMP_L1.png", 0.1)]
ANIMATION_JUMP_RIGHT = [("textures\\UNNAME_JUMP_V1.png", 0.1)]
