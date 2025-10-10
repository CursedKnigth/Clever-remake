import pygame
import random
from dicebutton import *

class DiceBox(): # this oject will manage all of the dice and make sure that theyre placed properly
    def __init__(self, screen):
        self.screen = screen
        self.x1 = 5
        self.y1 = 10
        self.width = screen.get_width() / 11 * 5 - self.x1
        self.height = 105
        self.x2 = screen.get_width() / 11 * 6
        self.y2 = self.y1
        self.active_player = 1
        self.picked_dice = 0
        
        # mapping the colours to dice
        self.dice_objects = {"yellow" : DiceButton(self.screen, "yellow", 0, 0, self.height, self.height),
                             "blue" : DiceButton(self.screen, "blue", 0, 0, self.height, self.height),
                             "green" : DiceButton(self.screen, "green", 0, 0, self.height, self.height),
                             "purple" : DiceButton(self.screen, "purple", 0, 0, self.height, self.height),
                             "orange" : DiceButton(self.screen, "orange", 0, 0, self.height, self.height),
                             "white" : DiceButton(self.screen, "white", 0, 0, self.height, self.height)}
        self.reset_dice()

    def draw(self, surface): #centering the dice over the board
        dice_count = len(self.active_dice)
        if(self.active_player==1):
            dice_x_start = self.x1 + (self.width - (self.height+5)*dice_count)/2
            i = 0
            for dice in self.active_dice:
                self.dice_objects[dice[1]].set_pos(dice_x_start + i*(self.height+5), self.y1)
                self.dice_objects[dice[1]].draw(surface)
                i += 1

    def roll_dice(self): 
        tem = []
        for i in self.active_dice:
            tem.append([random.randint(1, 6), i[1]])
        self.active_dice = sorted(tem, reverse=1)
        for i in self.active_dice:
            self.dice_objects[i[1]].set_number(i[0])
    
    def reset_dice(self):
        self.active_dice = [[0, "yellow"], [0, "blue"], [0, "green"], [0, "purple"], [0, "orange"], [0, "white"]]
        self.roll_dice()
    
    def get_picked_dice(self):
        return self.picked_dice 
    
    def pick_dice(self, dice):
        self.picked_dice = dice
    
    def confirm_pick(self):
        i = self.active_dice.find(self.picked_dice)
        self.active_dice = self.active_dice[0:i]
        self.picked_dice = 0