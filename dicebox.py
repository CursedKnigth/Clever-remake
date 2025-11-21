import pygame
import random
from infobutton import *
from constants import *

class DiceBox(): # this oject will manage all of the dice and make sure that they're placed properly
    def __init__(self, screen):
        self.screen = screen
        self.x1 = 5
        self.y1 = 10
        self.width = screen.get_width() / 11 * 5 - self.x1
        self.height = 102
        self.x2 = screen.get_width() / 11 * 6
        self.y2 = self.y1
        self.active_player = 1
        self.current_scale = 1

        self.Font=pygame.font.SysFont('timesnewroman',  90)
        self.num_to_txt = {1 : self.Font.render("1", False, "black"),
                        2 : self.Font.render("2", False, "black"),
                        3 : self.Font.render("3", False, "black"),
                        4 : self.Font.render("4", False, "black"),
                        5 : self.Font.render("5", False, "black"),
                        6 : self.Font.render("6", False, "black")}
        
        # mapping the colours to dice
        self.dice_objects = {YELLOW : InfoButton(self.screen, YELLOW, 0, 0, self.height, self.height, info = YELLOW, r = 5, func = self.pick_dice),
                             BLUE : InfoButton(self.screen, BLUE, 0, 0, self.height, self.height, info = BLUE, r = 5, func = self.pick_dice),
                             GREEN : InfoButton(self.screen, GREEN, 0, 0, self.height, self.height, info = GREEN, r = 5, func = self.pick_dice),
                             PURPLE : InfoButton(self.screen, PURPLE, 0, 0, self.height, self.height, info = PURPLE, r = 5, func = self.pick_dice),
                             ORANGE : InfoButton(self.screen, ORANGE, 0, 0, self.height, self.height, info = ORANGE, r = 5, func = self.pick_dice),
                             WHITE : InfoButton(self.screen, WHITE, 0, 0, self.height, self.height, info = WHITE, r = 5, func = self.pick_dice)}
        self.reset_dice()

    def draw(self): #centering the dice over the board
        scale = self.screen.get_width()/1440
        if(scale!=self.current_scale):
            self.Font=pygame.font.SysFont('timesnewroman',  int(90*scale))
            self.num_to_txt = {1 : self.Font.render("1", False, "black"),
                            2 : self.Font.render("2", False, "black"),
                            3 : self.Font.render("3", False, "black"),
                            4 : self.Font.render("4", False, "black"),
                            5 : self.Font.render("5", False, "black"),
                            6 : self.Font.render("6", False, "black")}
            self.current_scale = scale

        dice_count = len(self.active_dice)
        if(self.active_player==1):
            dice_x_start = self.x1 + (self.width - (self.height+5)*dice_count)/2
            i = 0
            for dice in self.active_dice:
                self.dice_objects[dice[1]].set_pos(dice_x_start + i*(self.height+5), self.y1)
                self.dice_objects[dice[1]].draw()
                i += 1

    def roll_dice(self): 
        tem = []
        for i in self.active_dice:
            self.dice_objects[i[1]].set_colour(i[1])
            self.dice_objects[i[1]].set_border(0, "red")
            tem.append([random.randint(1, 6), i[1]])
        self.active_dice = sorted(tem, reverse=1)
        for i in self.active_dice:
            self.dice_objects[i[1]].set_text(self.num_to_txt[i[0]])
        self.picked_dice = [0, 0]
    
    def reset_dice(self):
        self.active_dice = [[0, YELLOW], [0, BLUE], [0, GREEN], [0, PURPLE], [0, ORANGE], [0, WHITE]]
        for i in self.dice_objects.values():
            i.activate()
        self.roll_dice()
    
    def pick_dice(self, dice):
        for i in self.active_dice:
            self.dice_objects[i[1]].set_colour(i[1])
            self.dice_objects[i[1]].set_border(0, "red")
            if(i[1]==dice.get_info()):
                self.picked_dice = i
            
        self.dice_objects[dice.get_info()].set_border(3, "red")
        for i in self.active_dice:
            if(i[0]<self.picked_dice[0]):
                self.dice_objects[i[1]].set_colour(DIMMED_COLOURS_MAP[i[1]])
    
    def get_picked_dice(self):
        return self.picked_dice 
    
    def confirm_pick(self):
        tem = []
        for i in self.active_dice:
            if(i[0]>=self.picked_dice[0] and self.picked_dice[1]!=i[1]):
                tem.append(i)
            else:
                self.dice_objects[i[1]].deactivate()
        self.active_dice = tem
        self.roll_dice()

    def check_mouse(self, mouse):
       for i in self.dice_objects.values():
           i.check_mouse(mouse)