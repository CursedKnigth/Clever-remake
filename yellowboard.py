from infobutton import *
from constants import *

class YellowGameBoard():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y

        self.board_arrangememt = [[3, 6, 5, 0], 
                                   [2, 1, 0, 5], 
                                   [1, 0, 2, 4], 
                                   [0, 3, 4, 6]]
        x0 = 36
        y0 = 199
        dx = 55.9
        dy = 52.7
        bh = 44.5
        br = 10
        self.button_objects = [[InfoButton(screen, "white", self.x+j*dx+x0, self.y+i*dy+y0, bh, bh, r = br, info = self.board_arrangememt[i][j], empty=self.board_arrangememt[i][j]!=0, border_colour="red", border_width=4)
                                for j in range(4)] for i in range(4)]
        for i in range(4):
            for j in range(4):
                if(self.button_objects[i][j].get_info()==0):
                    self.button_objects[i][j].set_border(0, "white")
                    self.button_objects[i][j].set_cross(6, 9, "black")

        self.hide_n_deactivate()
    
    def draw(self):
        for i in range(4):
            for j in range(4):
                self.button_objects[i][j].draw()
    
    def check_mouse(self, mouse):
        for i in range(4):
            for j in range(4):
                self.button_objects[i][j].check_mouse(mouse)

    def hide_n_deactivate(self):
        for i in range(4):
            for j in range(4):
                if(self.button_objects[i][j].get_info()!=0):
                    self.button_objects[i][j].hide()
                    self.button_objects[i][j].deactivate()
    
    def check_dice(self, dicebox):
        dice = dicebox.get_picked_dice()
        if(dice[1]==YELLOW):
            for i in range(4):
                for j in range(4):
                    if(self.button_objects[i][j].get_info()==dice[0]):
                        self.button_objects[i][j].show()
                        self.button_objects[i][j].activate()
        else:
            self.hide_n_deactivate()