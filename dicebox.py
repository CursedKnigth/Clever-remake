import pygame
import random
from button import *

class DiceBox(): # this oject will manage all of the dice and make sure that theyre placed properly
    def __init__(self, screen):
        self.screen = screen
        self.x1 = 5
        self.y1 = 5
        self.w = screen.get_width() / 11 * 5 - self.x1
        self.h = 115
        self.x2 = screen.get_width() / 11 * 6
        self.y2 = 5
        self.active_player = 1
        self.picked_dice = 0
        self.reset_dice()

    def draw(self):
        dice_box_width = len(self.active_dice)*120
        if(self.active_player==1):
            i = 0
            for dice in self.active_dice:

    def roll_dice(self):
        tem = []
        for i in self.active_dice:
            tem.append([random.randint(1, 6), i[1]])
        self.active_dice = sorted(tem, reverse=1)
    
    def reset_dice(self):
        self.active_dice = [[0, "yellow"], [0, "blue"], [0, "green"], [0, "purple"], [0, "orange"]]
        self.roll_dice()
    
    def get_picked_dice(self):
        return self.picked_dice 
    
    def pick_dice(self, dice):
        self.picked_dice = dice
    
    def confirm_pick(self):
        i = self.active_dice.find(self.picked_dice)
        self.active_dice = self.active_dice[0:i]
        self.picked_dice = 0