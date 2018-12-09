# ПАРАМЕТРЫ ОКНА
FPS = 60
TILE_SIZE = 48
WIN_WIDTH = 16 * TILE_SIZE
WIN_HEIGHT = 12 * TILE_SIZE
WIN_POS_X = 50
WIN_POS_Y = 50


# ТЕКСТУРЫ КАРТЫ
# rect обозначает, что картинку нужно взять не всю, а только маленький квадратик
# но если rect = 0, то надо взять всю
# подробнее смотрите в описании класса block
BLUE_SKY = {"texture": "textures\\tiles.png",
            "rect": (2 * 16, 24 * 16, 16, 16)}
GRASS = {"texture": "textures2\\Block_1.bmp",
         "rect": 0}
# PLATFORM = {"texture": "textures\\tile2s.bmp",
#             "rect": (2 * 16, 16 * 16, 16, 16)}
PLATFORM = {"texture": "textures2\\Block_4.png",
            "rect": 0}
PLATFORM2 = {"texture": "textures2\\Block_6.bmp",
            "rect": 0}
BRIDGE = {"texture": "textures2\\Block_0.png",
            "rect": 0}
HALF_BRIDGE = {"texture": "textures2\\Block_n.png",
            "rect": 0}
HALF2_BRIDGE = {"texture": "textures2\\Block_k.png",
            "rect": 0}
WALL = {"texture": "textures\\tile2s.bmp",
        "rect": (2 * 16, 20 * 16, 16, 16)}
COIN = {"texture": "textures2\\Block_m.png",
        "rect": 0}
WOOD = {"texture": "textures2\\Block_2.bmp",
        "rect": 0}
WATER_SPIKES= {'texture': "textures2\\Block_w.png",
          'rect': 0}
BACKGROUND_level1 = {"texture": "textures2\\800x500.bmp",
              "rect": 0}
BACKGROUND_level2 = {"texture": "textures2\\800x500.bmp",
              "rect": 0}
SPIKES = {'texture': "textures2\\Block_8.png",
          'rect': 0}
BEAM = {'texture': "textures2\\Block_f.png",
          'rect': 0}
LEAF_SPIKES = {'texture': "textures2\\Block_l.png",
          'rect': 0}
HEART_FULL = {'texture': "textures\\Hp.png",
          'rect': 0}

# ТЕКСТУРЫ ИГРОКА
PLAYER_STAND = {"texture": "textures\\UNNAME.png",
                "rect": 0}
PLAYER_JUMP = {"texture": "textures\\UNNAME_JUMP_V1.png",
               "rect": 0}
PLAYER_WALK = {"texture": "textures\\UNNAME_WALK_V1.png",
               "rect": 0}

Jiiingo = {"texture": "textures2\\Jiiingo.png",
            "rect": 0}

HEAL = {'texture': "textures2\\Block_h.png",
          'rect': 0}

MAP_level = {'1': 'level1',
            '2': 'level2'
             }
MAP_level_max = 3


TOP_SPIKES = {"texture": "textures2\\Block_s.png",
            "rect": 0}
ROOF_SPIKES = {"texture": "textures2\\Block_r.png",
            "rect": 0}
KORM2 = {"texture": "textures2\\Block_г.png",
            "rect": 0}
WAL = {"texture": "textures2\\Block_б.png",
            "rect": 0}
KORM = {"texture": "textures2\\Block_ж.png",
            "rect": 0}
KORM3 = {"texture": "textures2\\Block_д.png",
            "rect": 0}
PLAT = {"texture": "textures2\\Block_в.png",
            "rect": 0}
STONE = {"texture": "textures2\\Block_к.png",
            "rect": 0}
Scale4 = {"texture": "textures\\Scale4.png",
            "rect": 0}
Scale2 = {"texture": "textures\\Scale2.png",
            "rect": 0}
Scale3 = {"texture": "textures\\Scale3.png",
            "rect": 0}
Scale5 = {"texture": "textures\\Scale5.png",
            "rect": 0}

SCALE_KEY ={'2':Scale2,
            '3':Scale3,
            '4':Scale4,
            '5':Scale5
}


# ОБОЗНАЧЕНИЯ ЭЛЕМЕНТОВ КАРТЫ
# удобно для загрузки карты
MAP_KEYS = {'0': BRIDGE,
            '1': GRASS,
            '2': WOOD,
            '4': PLATFORM,
            '6': PLATFORM2,
            '8': SPIKES,
            'n': HALF_BRIDGE,
            'w': WATER_SPIKES,
            'l': LEAF_SPIKES,
            'k': HALF2_BRIDGE,
            'f': BEAM,
            'm': COIN,
            'h': HEAL,
            'g': TOP_SPIKES,
            'u': WAL,
            'y': PLAT,
            'i': KORM,
            'e': KORM2,
            'q': STONE,
            'r': ROOF_SPIKES,
            'z': KORM3}


BACKGROUND_D = {"texture": "textures\\Dmenu_background.bmp",
              "rect": 0}
BACKGROUND_M = {"texture": "textures\\menu_background.bmp",
              "rect": 0}
BACKGROUND_W = {"texture": "textures\\Wmenu_background.bmp",
              "rect": 0}



background_key = {'0' : BACKGROUND_M,
                  '1' : BACKGROUND_level1,
                  '2':  BACKGROUND_level2,
                  'd' : BACKGROUND_D,
                  'w' : BACKGROUND_W}





SOLID_BLOCKS = '01246nkfuiqyezqк'
LOOT_BLOCKS = 'm'
Enemy = '8wlrJ'
HEAL_BLOCKS = "h"
SPAWN = 's'
JIIINGO = 'Jj'

# ПАРАМЕТРЫ МИРА
GRAVITY = 1
