from CONSTANT import *


class Enemy:
    def __init__(self, Id):
        self.Id = Id
        self.flag=self.set_flag(self.Id)
        self.E = ENEMY[Id]
        self.X = ENEMYX[Id]
        self.Y = ENEMYY[Id]
        self.direction = 'UP'

    def set_flag(self,Id):
        if Id==0 or Id==2:
            return True
        return False

    def draw(self):
        SCREEN2.blit(self.E, (self.X, self.Y))

    def move(self):
        if self.flag and self.Id == 0 and self.X < ENEMYX[self.Id+1]:
            if self.Valid(self.X+ENEMY_VELOCITY,self.Y):
                self.move_right()

        elif self.flag and self.Id == 2 and self.X  > ENEMYX[self.Id-1]:
            if self.Valid(self.X-ENEMY_VELOCITY,self.Y):
                self.move_left()
        else:
            self.flag=False
            self.original_move()

    def original_move(self):
        if not (self.Valid(self.X + DX[CH[self.direction]] * ENEMY_VELOCITY, self.Y + DY[CH[self.direction]]*ENEMY_VELOCITY)):
            if self.direction == 'UP' or self.direction == 'DOWN':
                global HORIZONTALID
                self.direction = HORIZONTAL[HORIZONTALID]
                HORIZONTALID += 1
                HORIZONTALID %= 2
            else:
                global VERTICALID
                self.direction = VERTICAL[VERTICALID]
                VERTICALID += 1
                VERTICALID %= 2
        else:
            if self.direction == 'UP':
                self.move_up()
            if self.direction == 'DOWN':
                self.move_down()
            if self.direction == 'LEFT':
                self.move_left()
            if self.direction == 'RIGHT':
                self.move_right()

    def move_right(self):
        self.X = self.X + ENEMY_VELOCITY

    def move_up(self):
        self.Y = self.Y - ENEMY_VELOCITY

    def move_down(self):
        self.Y = self.Y + ENEMY_VELOCITY

    def move_left(self):
        self.X = self.X - ENEMY_VELOCITY

    def Valid(self, X, Y):
        if X < 50 or X > 910:
            return False
        for x in range(X, X + ENEMYWIDTH + 1):
            for y in range(Y, Y + ENEMYHEIGHT + 1):
                if MAZE[x][y] == '1':
                    return False
        return True
