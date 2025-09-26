import pygame

class DiceBox():
    def __init__(self, screen):
        self.screen = screen
        self.x1 = 5
        self.y1 = 5
        self.w = screen.get_width() / 11 * 5 - 5
        self.h = 115
        self.x2 = screen.get_width() / 11 * 6
        self.y2 = 5
        self.active_player = 1
        self.active_dice = [[0, "yellow"], [0, "blue"], [0, "green"], [0, "purple"], [0, "orange"]]

    def draw(self):
        d_width = len(self.active_dice)*120
        if(self.active_player==1):
            
