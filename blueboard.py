from infobutton import *
from constants import *

class BlueGameBoard():
    def __init__(self, screen, x, y, dicebox):
        self.screen = screen
        self.x = x
        self.y = y
        self.dicebox = dicebox

        self.board_arrangememt = [[0, 2, 3, 4], 
                                   [5, 6, 7, 8], 
                                   [9, 10, 11, 12]]
        x0 = 350.5
        y0 = 259
        dx = 55.9
        dy = 52.7
        bh = 44.5
        br = 10
        self.button_objects = [[InfoButton(screen, "white", self.x+j*dx+x0, self.y+i*dy+y0, bh, bh, r = br, info = self.board_arrangememt[i][j], empty=self.board_arrangememt[i][j]!=0, border_colour="red", border_width=4, func=self.confirm_pick)
                                for j in range(4)] for i in range(3)]
        self.button_objects[0][0].hide()
        self.button_objects[0][0].deactivate()
        self.hide_n_deactivate()
    
    def draw(self):
        for i in range(3):
            for j in range(4):
                self.button_objects[i][j].draw()
    
    def check_mouse(self, mouse):
        for i in range(3):
            for j in range(4):
                self.button_objects[i][j].check_mouse(mouse)

    def hide_n_deactivate(self):
        for i in range(3):
            for j in range(4):
                if(self.button_objects[i][j].get_info()!=0):
                    self.button_objects[i][j].hide()
                self.button_objects[i][j].deactivate()
    
    def check_dice(self):
        self.hide_n_deactivate()
        dice = self.dicebox.get_picked_dice()
        if(dice[1]==BLUE or dice[1]==WHITE):
            x = self.dicebox.get_dice_val(BLUE) + self.dicebox.get_dice_val(WHITE)
            for i in range(3):
                for j in range(4):
                    if(self.button_objects[i][j].get_info()==x):
                        self.button_objects[i][j].show()
                        self.button_objects[i][j].activate()
    
    def confirm_pick(self, dice):
        dice.set_border(0, "white")
        dice.set_cross(6, 9, "black")
        dice.set_info(0)
        dice.set_empty(0)
        self.dicebox.confirm_pick()