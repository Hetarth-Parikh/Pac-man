from Libraries import *

SCREENWIDTH = 1000
SCREENHEIGHT = 700
FPS = 40
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Pac-man Game')

BACKGROUND = pygame.image.load(r'images\Start_Page.jpg')
BACKGROUND = pygame.transform.scale(BACKGROUND, (900, 600))
BACKGROUNDX = 50
BACKGROUNDY = 50

SCREEN2 = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GAME = pygame.image.load(r'images\Maze.jpg')
GAME = pygame.transform.scale(GAME, (1000, 700))
GAMEX = 0
GAMEY = 0

SCREEN3 = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GAME_OVER_IMG = pygame.image.load(r'images\pacman_game_over.jpg')
GAME_OVER_WIDTH = 1000
GAME_OVER_HEIGHT = 300
GAME_OVER_IMG = pygame.transform.scale(GAME_OVER_IMG, (GAME_OVER_WIDTH, GAME_OVER_HEIGHT))
GAME_OVER_X = 0
GAME_OVER_Y = 0

PLAYERWIDTH = 37
PLAYERHEIGHT = 21
PLAYER = pygame.image.load(r'images\Player.jpg')
PLAYER = pygame.transform.scale(PLAYER, (PLAYERWIDTH, PLAYERHEIGHT)).convert_alpha(SCREEN2)
PLAYERX = 245
PLAYERY = 310
PLAYER_VELOCITY = 5

MAZE = []
POINTS = [(120, 94), (185, 94), (260, 94), (325, 94), (390, 94), (455, 94), (555, 94), (620, 94), (680, 94), (740, 94),
          (815, 94), (880, 94),
          (120, 150), (185, 150), (260, 150), (325, 150), (390, 150), (455, 150), (555, 150), (620, 150), (682, 150),
          (740, 150), (815, 150), (880, 150),
          (120, 205), (185, 205), (260, 205), (390, 205), (455, 205), (555, 205), (620, 205), (740, 205), (815, 205),
          (880, 205),
          (260, 264), (390, 264), (455, 264), (555, 264), (620, 264), (740, 264),
          (120, 320), (185, 320), (325, 320), (455, 320), (555, 320), (682, 320), (740, 320), (815, 320),
          (880, 320),
          (260, 380), (390, 380), (455, 380), (555, 380), (620, 380), (740, 380),
          (120, 440), (185, 440), (260, 440), (325, 440), (390, 440), (455, 440), (555, 440), (620, 440), (682, 440),
          (740, 440), (815, 440), (880, 440),
          (120, 490), (185, 490), (260, 490), (325, 490), (390, 490), (455, 490), (555, 490), (620, 490), (682, 490),
          (740, 490), (815, 490), (880, 490),
          (120, 550), (185, 550), (260, 550), (390, 550), (455, 550), (555, 550), (620, 550), (740, 550), (815, 550),
          (880, 550),
          (120, 608), (185, 608), (260, 608), (325, 608), (390, 608), (455, 608), (555, 608), (620, 608), (682, 608),
          (740, 608), (815, 608), (880, 608)
          ]

ENEMYWIDTH = 40
ENEMYHEIGHT = 23
ENEMY_VELOCITY = 1
ENEMY = [
    pygame.transform.scale(pygame.image.load(r'images\Enemy1.jpg'),
                           (ENEMYWIDTH, ENEMYHEIGHT)).convert_alpha(SCREEN2),
    pygame.transform.scale(pygame.image.load(r'images\Enemy2.jpg'),
                           (ENEMYWIDTH, ENEMYHEIGHT)).convert_alpha(SCREEN2),
    pygame.transform.scale(pygame.image.load(r'images\Enemy3.jpg'),
                           (ENEMYWIDTH, ENEMYHEIGHT)).convert_alpha(SCREEN2)
]
ENEMYX = [428, 480, 528]
ENEMYY = [310, 310, 310]

VERTICAL = ['UP', 'DOWN']
VERTICALID = 0

HORIZONTAL = ['LEFT', 'RIGHT']
HORIZONTALID = 0

DX = [0, 0, -1, 1]
DY = [-1, 1, 0, 0]
CH = {'UP': 0, 'DOWN': 1, 'LEFT': 2, 'RIGHT': 3}

SCREEN4=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
LEVELIMGWIDTH=1000
LEVELIMGHEIGHT=300
LEVELIMG=pygame.image.load(r'images\pacman_game_over.jpg')
LEVELIMG=pygame.transform.scale(LEVELIMG,(LEVELIMGWIDTH,LEVELIMGHEIGHT))
LEVELIMG_X=0
LEVELIMG_Y=0

SCREEN5=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
OPTIONWIDTH=1000
OPTIONHEIGHT=300
OPTIONIMG=pygame.image.load(r'images\pacman_game_over.jpg')
OPTIONIMG=pygame.transform.scale(OPTIONIMG,(OPTIONWIDTH,OPTIONHEIGHT))
OPTIONIMGX=0
OPTIONIMGY=0

MUSICON=1
QUALITY=2