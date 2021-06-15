from CONSTANT import *


class Points:
    def __init__(self, x, y):
        self.flag = True
        self.X = x
        self.Y = y
        self.color = (255,128,0)

    def draw(self):
        pygame.draw.circle(SCREEN2, self.color, (self.X, self.Y), 6)
