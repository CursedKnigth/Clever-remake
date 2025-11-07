from infobutton import *

class YellowGameBoard():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y

        self.button_arrangememt = [[3, 6, 5, 0], 
                                   [2, 1, 0, 5], 
                                   [1, 0, 2, 4], 
                                   [0, 3, 4, 6]]
        x0 = 50
        y0 = 50
        dx = 100
        dy = 100
        bh = 75
        br = 5
        self.button_objects = [[InfoButton(screen, pygame.Color(50, 50, 50, 200), self.x+j*dx+x0, self.y+i*dy+y0, bh, bh, r = br, info = self.button_arrangememt[i][j])
                                for j in range(4)] for i in range(4)]
    
    def draw(self):
        for i in range(4):
            for j in range(4):
                self.button_objects[i][j].draw()
    