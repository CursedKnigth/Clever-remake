import pygame
import random
from dicebutton import *
from constants import *

class DiceBox(): # this oject will manage all of the dice and make sure that they're placed properly
    def __init__(self, screen):
        self.screen = screen
        self.x1 = 5
        self.y1 = 10
        self.width = screen.get_width() / 11 * 5 - self.x1
        self.height = 105
        self.x2 = screen.get_width() / 11 * 6
        self.y2 = self.y1
        self.active_player = 1
        
        # mapping the colours to dice
        self.dice_objects = {YELLOW : DiceButton(self.screen, YELLOW, 0, 0, self.height, self.height),
                             BLUE : DiceButton(self.screen, BLUE, 0, 0, self.height, self.height),
                             GREEN : DiceButton(self.screen, GREEN, 0, 0, self.height, self.height),
                             PURPLE : DiceButton(self.screen, PURPLE, 0, 0, self.height, self.height),
                             ORANGE : DiceButton(self.screen, ORANGE, 0, 0, self.height, self.height),
                             WHITE : DiceButton(self.screen, WHITE, 0, 0, self.height, self.height)}
        self.reset_dice()

    def draw(self, screen): #centering the dice over the board
        dice_count = len(self.active_dice)
        if(self.active_player==1):
            dice_x_start = self.x1 + (self.width - (self.height+5)*dice_count)/2
            i = 0
            for dice in self.active_dice:
                self.dice_objects[dice[1]].set_pos(dice_x_start + i*(self.height+5), self.y1)
                self.dice_objects[dice[1]].draw(screen)
                i += 1

    def roll_dice(self): 
        tem = []
        for i in self.active_dice:
            self.dice_objects[i[1]].wipe_select()
            tem.append([random.randint(1, 6), i[1]])
        self.active_dice = sorted(tem, reverse=1)
        for i in self.active_dice:
            self.dice_objects[i[1]].set_number(i[0])
        self.picked_dice = [0, 0]
    
    def reset_dice(self):
        self.active_dice = [[0, YELLOW], [0, BLUE], [0, GREEN], [0, PURPLE], [0, ORANGE], [0, WHITE]]
        self.roll_dice()
    
    def pick_dice(self, dice_colour):
        for i in self.active_dice:
            self.dice_objects[i[1]].wipe_select()
            if(i[1]==dice_colour):
                self.picked_dice = i
        self.dice_objects[dice_colour].select_main()
        for i in self.active_dice:
            if(i[0]<self.picked_dice[0]):
                self.dice_objects[i[1]].select_lesser()
    
    def get_picked_dice(self):
        return self.picked_dice 
    
    def confirm_pick(self):
        tem = []
        for i in self.active_dice:
            if(i[0]>=self.picked_dice[0] and self.picked_dice[1]!=i[1]):
                tem.append(i)
        self.active_dice = tem
        self.roll_dice()

    def check_mouse(self, mouse):
       for i in self.dice_objects.values():
           i.check_mouse(mouse, self)