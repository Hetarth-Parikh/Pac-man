from Button import *
from Enemy import *
from Points import *
from pygame import mixer


class Pacman:
    def __init__(self):
        pygame.init()
        self.up = 0
        self.down = 0
        self.flag = 1
        self.counter = 0
        self.last_flag = []
        self.due_to_mouse_start = False
        self.due_to_mouse_setting = False
        self.due_to_mouse_quit = False
        self.SCORE = 0
        self.START = Button((0, 0, 0), 340, 420, 320, 70, 40, 'PLAY')
        self.SETTING = Button((0, 0, 0), 340, 500, 320, 70, 40, 'OPTIONS')
        self.QUIT = Button((0, 0, 0), 340, 580, 320, 70, 40, 'QUIT')
        self.GAMEOVER = Button((0, 0, 0), 400, 440, 200, 100, 70, 'Game Over!', (255, 255, 51))
        self.AGAIN = Button((0, 0, 0), 460, 550, 100, 100, 35, 'Press enter to restart...', (51, 255, 255))
        self.SCOREBUTTON = Button((0, 0, 0), 0, 0, 100, 100, 35, 'Score')
        self.ENEMY = [Enemy(0), Enemy(1), Enemy(2)]
        self.ENEMY2 = [Enemy(0), Enemy(1), Enemy(2), Enemy(0), Enemy(1)]
        self.ENEMY3 = [Enemy(0), Enemy(1), Enemy(2), Enemy(0), Enemy(1), Enemy(2), Enemy(0)]
        self.POINTS = []
        self.generate_maze()
        self.intialize_points()
        self.LEVEL1 = Button((0, 128, 0), 60, 350, 900, 70, 30, 'Level 1                         Difficulty : Easy')
        self.LEVEL2 = Button((255, 165, 0), 60, 450, 900, 70, 30,
                             '     Level 2                         Difficulty : Medium')
        self.LEVEL3 = Button((255, 0, 0), 60, 550, 900, 70, 30, 'Level 3                         Difficulty : Hard')
        self.MUSIC = Button((0, 0, 0), 260, 350, 100, 100, 40, 'Music')
        self.ON = Button((0, 128, 0), 610, 375, 80, 50, 30, 'ON')
        self.OFF = Button((0, 0, 0), 690, 375, 80, 50, 30, 'OFF')
        self.QUALITY = Button((0, 0, 0), 260, 450, 100, 100, 40, 'Quality')
        self.LOW = Button((0, 0, 0), 500, 475, 100, 50, 30, 'Low')
        self.MEDIUM = Button((0, 128, 0), 610, 475, 150, 50, 30, 'Medium')
        self.HIGH = Button((0, 0, 0), 770, 475, 100, 50, 30, 'High')
        self.BACK = Button((0, 0, 0), 450, 575, 100, 100, 30, 'Press ESC To Return Back')
        # self.generate_coordinates()

    def set_size_buttons(self, start, setting, quit):
        self.START.draw(start)
        self.SETTING.draw(setting)
        self.QUIT.draw(quit)

    def set_size_buttons_level(self, lvl1, lvl2, lvl3):
        self.LEVEL1 = Button((0, 128, 0), 60, 350, 900 + lvl1, 70 + lvl1, 30 + lvl1,
                             'Level 1                         Difficulty : Easy')
        self.LEVEL2 = Button((255, 165, 0), 60, 450, 900 + lvl2, 70 + lvl2, 30 + lvl2,
                             '     Level 2                         Difficulty : Medium')
        self.LEVEL3 = Button((255, 0, 0), 60, 550, 900 + lvl3, 70 + lvl3, 30 + lvl3,
                             'Level 3                         Difficulty : Hard')

    def change_state_key_bord(self):
        if self.down == 1 and self.up == 1:
            self.set_size_buttons(60, 40, 40)
        elif self.down == 2 and self.up == 2:
            self.set_size_buttons(40, 60, 40)
        elif self.down == 3 and self.up == 3:
            self.set_size_buttons(40, 40, 60)

    def change_state_mouse(self):
        if self.START.isOver(pygame.mouse.get_pos()):
            self.set_size_buttons(60, 40, 40)
            self.due_to_mouse_start = True
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif self.SETTING.isOver(pygame.mouse.get_pos()):
            self.set_size_buttons(40, 60, 40)
            self.due_to_mouse_setting = True
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif self.QUIT.isOver(pygame.mouse.get_pos()):
            self.set_size_buttons(40, 40, 60)
            self.due_to_mouse_quit = True
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            if self.due_to_mouse_start or self.due_to_mouse_setting or self.due_to_mouse_quit:
                self.set_size_buttons(40, 40, 40)
                self.due_to_mouse_start = False
                self.due_to_mouse_setting = False
                self.due_to_mouse_quit = False
                self.up = 0
                self.down = 0
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def change_state_level_mouse(self):
        if self.LEVEL1.isOver(pygame.mouse.get_pos()):
            self.set_size_buttons_level(10, 0, 0)
            self.due_to_mouse_start = True
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif self.LEVEL2.isOver(pygame.mouse.get_pos()):
            self.set_size_buttons_level(0, 10, 0)
            self.due_to_mouse_setting = True
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif self.LEVEL3.isOver(pygame.mouse.get_pos()):
            self.set_size_buttons_level(0, 0, 10)
            self.due_to_mouse_quit = True
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            if self.due_to_mouse_start or self.due_to_mouse_setting or self.due_to_mouse_quit:
                self.set_size_buttons_level(0, 0, 0)
                self.due_to_mouse_start = False
                self.due_to_mouse_setting = False
                self.due_to_mouse_quit = False
                self.up = 0
                self.down = 0
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def change_state_level_key_board(self):
        if self.down == 1 and self.up == 1:
            self.set_size_buttons_level(10, 0, 0)
        elif self.down == 2 and self.up == 2:
            self.set_size_buttons_level(0, 10, 0)
        elif self.down == 3 and self.up == 3:
            self.set_size_buttons_level(0, 0, 10)

    def change_state_mouse_option(self):
        if self.ON.isOver(pygame.mouse.get_pos()):
            self.due_to_mouse_start = True
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif self.OFF.isOver(pygame.mouse.get_pos()):
            self.due_to_mouse_setting = True
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif self.LOW.isOver(pygame.mouse.get_pos()):
            self.due_to_mouse_setting = True
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif self.MEDIUM.isOver(pygame.mouse.get_pos()):
            self.due_to_mouse_setting = True
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif self.HIGH.isOver(pygame.mouse.get_pos()):
            self.due_to_mouse_setting = True
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            if self.due_to_mouse_start or self.due_to_mouse_setting or self.due_to_mouse_quit:
                self.due_to_mouse_start = False
                self.due_to_mouse_setting = False
                self.due_to_mouse_quit = False
                self.up = 0
                self.down = 0
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def press_down(self):
        self.down += 1
        if self.down == 4:
            self.down = 1
        self.up += 1
        if self.up == 4:
            self.up = 1

    def press_up(self):
        self.down -= 1
        if self.down == 0:
            self.down = 3
        self.up -= 1
        if self.up == 0:
            self.up = 3

    def play_sound(self):
        if MUSICON == 0:
            mixer.music.stop()
            self.last_flag.clear()
            return
        if self.flag in self.last_flag:
            return
        if self.flag == 1 or self.flag == 2 or self.flag == 3:
            mixer.music.stop()
            mixer.init()
            try:
                mixer.music.load("sounds\Intro.mp3")
            except:
                mixer.music.load("sounds\Intro.wav")
            mixer.music.set_volume(0.7)
            mixer.music.play(-1)
            self.last_flag = [1, 2, 3]
        elif self.flag == 4 or self.flag == 5 or self.flag == 6:
            mixer.init()
            try:
                mixer.music.load("sounds\Chomp.mp3")
            except:
                mixer.music.load("sounds\Chomp.wav")
            mixer.music.set_volume(0.4)
            mixer.music.play(-1)
            self.last_flag = [4, 5, 6]
        else:
            mixer.init()
            try:
                mixer.music.load("sounds\Death.mp3")
            except:
                mixer.music.load("sounds\Death.wav")
            mixer.music.set_volume(0.7)
            mixer.music.play()
            self.last_flag = [7]

    def run(self):
        global PLAYERX
        global PLAYERY
        global PLAYER_VELOCITY
        global MUSICON
        global QUALITY
        global FPS
        while True:
            self.play_sound()
            if self.flag == 1:  # Start Page
                self.draw_start_screen()
                self.change_state_key_bord()
                self.change_state_mouse()
            elif self.flag == 2:  # Play Page
                self.counter = min(self.counter + 1, 2)
                self.draw_level_screen()
                self.change_state_level_key_board()
                self.change_state_level_mouse()
            elif self.flag == 3:  # Control Page
                self.change_state_mouse_option()
                self.draw_option_screen()
            elif self.flag == 4:  # Level - 1
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
                self.draw_main_screen_level_1()
                self.draw_points()
                if self.isColide(1) or self.SCORE == 101:
                    self.flag = 7
            elif self.flag == 5:  # Level - 2
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
                self.draw_main_screen_level_2()
                self.draw_points()
                if self.isColide(2) or self.SCORE == 101:
                    self.flag = 7
            elif self.flag == 6:  # Level - 3
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
                self.draw_main_screen_level_3()
                self.draw_points()
                if self.isColide(3) or self.SCORE == 101:
                    self.flag = 7
            else:
                self.draw_game_over()

            for event in pygame.event.get():
                if event.type == QUIT or (self.flag == 1 and event.type == MOUSEBUTTONDOWN and self.QUIT.isOver(
                        pygame.mouse.get_pos())) or (
                        self.flag == 1 and event.type == KEYDOWN and self.up == 3 and self.down == 3 and event.key == K_RETURN):
                    pygame.quit()
                    sys.exit()
                if (self.flag == 1 and event.type == MOUSEBUTTONDOWN and self.START.isOver(pygame.mouse.get_pos())) or (
                        self.flag == 1 and event.type == KEYDOWN and self.up == 1 and self.down == 1 and event.key == K_RETURN):
                    self.flag = 2
                    self.counter = 1
                    self.up = 0
                    self.down = 0
                    self.due_to_mouse_start = False
                    self.due_to_mouse_setting = False
                    self.due_to_mouse_quit = False
                if (self.flag == 1 and event.type == MOUSEBUTTONDOWN and self.SETTING.isOver(
                        pygame.mouse.get_pos())) or (
                        self.flag == 1 and event.type == KEYDOWN and self.up == 2 and self.down == 2 and event.key == K_RETURN):
                    self.flag = 3
                    self.down = 0
                    self.due_to_mouse_start = False
                    self.due_to_mouse_setting = False
                    self.due_to_mouse_quit = False

                if (self.counter == 2 and self.flag == 2 and event.type == MOUSEBUTTONDOWN and self.LEVEL1.isOver(
                        pygame.mouse.get_pos())) or (
                        self.flag == 2 and event.type == KEYDOWN and self.up == 1 and self.down == 1 and event.key == K_RETURN):
                    self.flag = 4

                if (self.counter == 2 and self.flag == 2 and event.type == MOUSEBUTTONDOWN and self.LEVEL2.isOver(
                        pygame.mouse.get_pos())) or (
                        self.flag == 2 and event.type == KEYDOWN and self.up == 2 and self.down == 2 and event.key == K_RETURN):
                    self.flag = 5

                if (self.counter == 2 and self.flag == 2 and event.type == MOUSEBUTTONDOWN and self.LEVEL3.isOver(
                        pygame.mouse.get_pos())) or (
                        self.flag == 2 and event.type == KEYDOWN and self.up == 3 and self.down == 3 and event.key == K_RETURN):
                    self.flag = 6

                if self.flag == 1:
                    pygame.key.set_repeat(0, 0)
                    if event.type == KEYDOWN and event.key == K_DOWN:
                        self.press_down()
                    if event.type == KEYDOWN and event.key == K_UP:
                        self.press_up()
                elif self.flag == 2:
                    pygame.key.set_repeat(0, 0)
                    if event.type == KEYDOWN and event.key == K_DOWN:
                        self.press_down()
                    if event.type == KEYDOWN and event.key == K_UP:
                        self.press_up()
                    if event.type == KEYDOWN and event.key == K_ESCAPE:
                        self.flag = 1

                elif self.flag == 3:
                    pygame.key.set_repeat(0, 0)
                    if event.type == MOUSEBUTTONDOWN and self.ON.isOver(pygame.mouse.get_pos()):
                        MUSICON = 1
                    if event.type == MOUSEBUTTONDOWN and self.OFF.isOver(pygame.mouse.get_pos()):
                        MUSICON = 0
                    if event.type == MOUSEBUTTONDOWN and self.LOW.isOver(pygame.mouse.get_pos()):
                        QUALITY = 1
                        FPS = 30
                    if event.type == MOUSEBUTTONDOWN and self.MEDIUM.isOver(pygame.mouse.get_pos()):
                        QUALITY = 2
                        FPS = 40
                    if event.type == MOUSEBUTTONDOWN and self.HIGH.isOver(pygame.mouse.get_pos()):
                        QUALITY = 3
                        FPS = 50
                    if event.type == KEYDOWN and event.key == K_ESCAPE:
                        self.flag = 1

                elif self.flag in (4, 5, 6):
                    keys = pygame.key.get_pressed()
                    pygame.key.set_repeat(10, 50)
                    if keys[K_DOWN]:
                        if self.Valid(PLAYERX, PLAYERY + PLAYER_VELOCITY):
                            PLAYERY = PLAYERY + PLAYER_VELOCITY
                    if keys[K_UP]:
                        if self.Valid(PLAYERX, PLAYERY - PLAYER_VELOCITY):
                            PLAYERY = PLAYERY - PLAYER_VELOCITY
                    if keys[K_LEFT]:
                        if self.Valid(PLAYERX - PLAYER_VELOCITY, PLAYERY):
                            PLAYERX = PLAYERX - PLAYER_VELOCITY
                    if keys[K_RIGHT]:
                        if self.Valid(PLAYERX + PLAYER_VELOCITY, PLAYERY):
                            PLAYERX = PLAYERX + PLAYER_VELOCITY

                else:
                    keys = pygame.key.get_pressed()
                    if keys[K_RETURN]:
                        self.clear()

            FPSCLOCK.tick(FPS)
            pygame.display.update()

    def clear(self):
        self.flag = 1
        global PLAYERX, PLAYERY, VERTICALID, HORIZONTALID
        PLAYERX = 245
        PLAYERY = 310
        VERTICALID = 0
        HORIZONTALID = 0
        self.up = 0
        self.down = 0
        self.due_to_mouse_start = False
        self.due_to_mouse_setting = False
        self.due_to_mouse_quit = False
        self.SCORE = 0
        for ind in range(3):
            self.ENEMY[ind].X = ENEMYX[ind]
            self.ENEMY[ind].Y = ENEMYY[ind]
            self.ENEMY[ind].direction = 'UP'
            self.ENEMY[ind].flag = self.ENEMY[ind].set_flag(ind)
        for ind in range(5):
            self.ENEMY2[ind].X = ENEMYX[ind % 3]
            self.ENEMY2[ind].Y = ENEMYY[ind % 3]
            self.ENEMY2[ind].direction = 'UP'
            self.ENEMY2[ind].flag = self.ENEMY2[ind].set_flag(ind % 3)
        for ind in range(7):
            self.ENEMY3[ind].X = ENEMYX[ind % 3]
            self.ENEMY3[ind].Y = ENEMYY[ind % 3]
            self.ENEMY3[ind].direction = 'UP'
            self.ENEMY3[ind].flag = self.ENEMY3[ind].set_flag(ind % 3)
        for point in self.POINTS:
            point.flag = True
        pygame.event.clear()

    def draw_start_screen(self):
        SCREEN.fill((0, 0, 0))
        SCREEN.blit(BACKGROUND, (BACKGROUNDX, BACKGROUNDY))
        self.START.draw(40)
        self.SETTING.draw(40)
        self.QUIT.draw(40)

    def draw_option_screen(self):
        SCREEN5.fill((0, 0, 0))
        SCREEN5.blit(OPTIONIMG, (OPTIONIMGX, OPTIONIMGY))
        self.MUSIC.draw(40)
        self.QUALITY.draw(40)
        self.ON = Button((0, (128 if MUSICON == 1 else 0), 0), 610, 375, 80, 50, 30, 'ON')
        self.OFF = Button((0, (128 if MUSICON == 0 else 0), 0), 690, 375, 80, 50, 30, 'OFF')
        self.LOW = Button((0, (128 if QUALITY == 1 else 0), 0), 500, 475, 100, 50, 30, 'Low')
        self.MEDIUM = Button((0, (128 if QUALITY == 2 else 0), 0), 610, 475, 150, 50, 30, 'Medium')
        self.HIGH = Button((0, (128 if QUALITY == 3 else 0), 0), 770, 475, 100, 50, 30, 'High')
        self.BACK = Button((0, 0, 0), 450, 575, 100, 100, 30, 'Press ESC To Return Back')

    def draw_main_screen_level_1(self):
        SCREEN2.blit(GAME, (GAMEX, GAMEY))
        SCREEN2.blit(PLAYER, (PLAYERX, PLAYERY))
        self.SCOREBUTTON = Button((0, 0, 0), 100, 0, 100, 45, 35, 'SCORE : ' + str(self.SCORE))
        for enemy in self.ENEMY:
            enemy.draw()
            for i in range(2):
                enemy.move()

    def draw_main_screen_level_2(self):
        SCREEN2.blit(GAME, (GAMEX, GAMEY))
        SCREEN2.blit(PLAYER, (PLAYERX, PLAYERY))
        self.SCOREBUTTON = Button((0, 0, 0), 100, 0, 100, 45, 35, 'SCORE : ' + str(self.SCORE))
        for enemy in self.ENEMY2:
            enemy.draw()
            for i in range(2):
                enemy.move()

    def draw_main_screen_level_3(self):
        SCREEN2.blit(GAME, (GAMEX, GAMEY))
        SCREEN2.blit(PLAYER, (PLAYERX, PLAYERY))
        self.SCOREBUTTON = Button((0, 0, 0), 100, 0, 100, 45, 35, 'SCORE : ' + str(self.SCORE))
        for enemy in self.ENEMY3:
            enemy.draw()
            for i in range(2):
                enemy.move()

    def draw_game_over(self):
        SCREEN3.fill((0, 0, 0))
        SCREEN3.blit(GAME_OVER_IMG, (GAME_OVER_X, GAME_OVER_Y))
        YOUR_SCORE = Button((0, 0, 0), 400, 325, 200, 100, 55,
                            'Your Score is ' + str(self.SCORE) + '/' + str(len(POINTS)))
        YOUR_SCORE.draw(55)
        text = 'Game Over!' if self.SCORE < 101 else 'Level Cleared,Congrats!'
        self.GAMEOVER = Button((0, 0, 0), 400, 440, 200, 100, 70, text, (255, 255, 51))
        self.AGAIN.draw(35)

    def Valid(self, X, Y):
        global PLAYERX
        global PLAYERY
        if X > 910:
            PLAYERX = 50
        if X < 50:
            PLAYERX = 910
        for x in range(X, X + PLAYERWIDTH + 1):
            for y in range(Y, Y + PLAYERHEIGHT + 1):
                if MAZE[x][y] == '1':
                    return False
        return True

    def generate_coordinates(self):
        im = Image.open(r'images\Maze.jpg')
        im = im.convert('RGB')
        coor = open('coordinates.txt', 'w')
        for i in range(1000):
            for j in range(700):
                temp = int(im.getpixel((i, j)) > (100, 100, 100))
                st = str(temp) + ' '
                coor.write(st)
            coor.write('\n')
        coor.close()

    def generate_maze(self):
        global MAZE
        maze = open('coordinates.txt', 'r')
        for line in maze:
            line.strip()
            MAZE.append(line.split())

    def intialize_points(self):
        for (x, y) in POINTS:
            self.POINTS.append(Points(x, y))

    def draw_points(self):
        for points in self.POINTS:
            if points.flag:
                points.draw()

    def isColide(self, LEVEL):
        for x in range(PLAYERX, PLAYERX + PLAYERWIDTH):
            for y in range(PLAYERY, PLAYERY + PLAYERHEIGHT):
                for point in self.POINTS:
                    if point.flag == True and point.X == x and point.Y == y:
                        point.flag = False
                        self.SCORE += 1
        if LEVEL == 1:
            for enemy in self.ENEMY:
                for x in range(enemy.X, enemy.X + ENEMYWIDTH + 1):
                    for y in range(enemy.Y, enemy.Y + ENEMYHEIGHT + 1):
                        if PLAYERX <= x <= PLAYERX + PLAYERWIDTH and PLAYERY <= y <= PLAYERY + PLAYERHEIGHT:
                            return True
        elif LEVEL == 2:
            for enemy in self.ENEMY2:
                for x in range(enemy.X, enemy.X + ENEMYWIDTH + 1):
                    for y in range(enemy.Y, enemy.Y + ENEMYHEIGHT + 1):
                        if PLAYERX <= x <= PLAYERX + PLAYERWIDTH and PLAYERY <= y <= PLAYERY + PLAYERHEIGHT:
                            return True
        else:
            for enemy in self.ENEMY3:
                for x in range(enemy.X, enemy.X + ENEMYWIDTH + 1):
                    for y in range(enemy.Y, enemy.Y + ENEMYHEIGHT + 1):
                        if PLAYERX <= x <= PLAYERX + PLAYERWIDTH and PLAYERY <= y <= PLAYERY + PLAYERHEIGHT:
                            return True
        return False

    def draw_level_screen(self):
        SCREEN4.fill((0, 0, 0))
        SCREEN4.blit(LEVELIMG, (LEVELIMG_X, LEVELIMG_Y))
        self.LEVEL1 = Button((0, 128, 0), 60, 350, 900, 70, 30, 'Level 1                         Difficulty : Easy')
        self.LEVEL2 = Button((255, 165, 0), 60, 450, 900, 70, 30,
                             '     Level 2                         Difficulty : Medium')
        self.LEVEL3 = Button((255, 0, 0), 60, 550, 900, 70, 30, 'Level 3                         Difficulty : Hard')
        self.BACK = Button((0, 0, 0), 450, 640, 100, 50, 25, 'Press ESC To Return Back')
