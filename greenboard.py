from infobutton import *
from constants import *

class GreenGameBoard():
    def __init__(self, screen, x, y, dicebox):
        self.screen = screen
        self.x = x
        self.y = y
        self.dicebox = dicebox

        self.board_arrangememt = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]
        x0 = 83
        y0 = 518
        dx = 49.1
        bh = 44.5
        br = 10
        self.button_objects = [InfoButton(screen, "white", self.x+i*dx+x0, self.y+y0, bh, bh, r = br, info = self.board_arrangememt[i], empty=self.board_arrangememt[i]!=0, border_colour="red", border_width=4, func=self.confirm_pick)
                                for i in range(11)]
    
    def draw(self):
        for i in range(11):
            self.button_objects[i].draw()
    
    def check_mouse(self, mouse, event):
        for i in range(11):
            self.button_objects[i].check_mouse(mouse, event)

    def hide_n_deactivate(self):
        for i in range(11):
            if(self.button_objects[i].get_info()>0):
                self.button_objects[i].hide()
            self.button_objects[i].deactivate()
    
    def check_dice(self):
        self.hide_n_deactivate()
        dice = self.dicebox.get_picked_dice()
        if(dice[1]==GREEN or dice[1]==WHITE):
            x = dice[0]
            for i in range(11):
                if(self.button_objects[i].get_info()==x):
                    self.button_objects[i].show()
                    self.button_objects[i].activate()
    
    def confirm_pick(self, dice):
        dice.set_border(0, "white")
        dice.set_cross(6, 9, "black")
        dice.set_info(0)
        dice.set_empty(0)
        self.dicebox.confirm_pick()