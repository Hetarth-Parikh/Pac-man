from CONSTANT import *


class Button:
    def __init__(self, color, x, y, width, height, size, text='',textcolor=(255,255,255)):
        self.color = color
        self.textcolor=textcolor
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.size = size
        self.draw(size)

    def draw(self, size):
        pygame.draw.rect(SCREEN, self.color, (self.x, self.y, self.width, self.height), border_radius=30)
        if self.text != '':
            font = pygame.font.SysFont('rockwell', size, italic=False, bold=False)
            text = font.render(self.text, True, self.textcolor)
            SCREEN.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        if self.x < pos[0] + 10 < self.x + self.width:
            if self.y < pos[1] + 10 < self.y + self.height:
                return True
        return False

MUSICON=1