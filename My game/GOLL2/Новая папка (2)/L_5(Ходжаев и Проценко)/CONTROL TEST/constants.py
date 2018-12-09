# ПАРАМЕТРЫ ОКНА
FPS = 300
TILE_SIZE = 48
WIN_WIDTH = 24 * TILE_SIZE
WIN_HEIGHT = 14 * TILE_SIZE
WIN_POS_X = 50
WIN_POS_Y = 50


# ТЕКСТУРЫ КАРТЫ
# rect обозначает, что картинку нужно взять не всю, а только маленький квадратик
# но если rect = 0, то надо взять всю
# подробнее смотрите в описании класса block
BLUE_SKY = {"texture": "textures\\tiles.png",
            "rect": (2 * 16, 24 * 16, 16, 16)}
GRASS = {"texture": "textures\\tiles.png",
         "rect": (2 * 16, 4 * 16, 16, 16)}
PLATFORM = {"texture": "textures\\tiles.png",
            "rect": (2 * 16, 16 * 16, 16, 16)}
WALL = {"texture": "textures\\tiles.png",
        "rect": (2 * 16, 20 * 16, 16, 16)}
COIN = {"texture": "textures\\coin.png",
        "rect": 0}
BACKGROUND = {"texture": "textures\\background.bmp",
              "rect": 0}

ENEMY = {'texture': "textures\\spikes.png",
          'rect': 0}

# ТЕКСТУРЫ ИГРОКА
PLAYER_STAND = {"texture": "textures\\player_stand.png",
                "rect": 0}
PLAYER_JUMP = {"texture": "textures\\player_jump.png",
               "rect": 0}
PLAYER_WALK = {"texture": "textures\\player_walk.png",
               "rect": 0}


# ОБОЗНАЧЕНИЯ ЭЛЕМЕНТОВ КАРТЫ
# удобно для загрузки карты
MAP_KEYS = {'1': BLUE_SKY,
            '2': GRASS,
            '3': PLATFORM,
            '4': WALL,
            '5': COIN,
            '6': ENEMY}

SOLID_BLOCKS = '234'
LOOT_BLOCKS = '5'
Enemy = '6'

# ПАРАМЕТРЫ МИРА
GRAVITY = 9.81
