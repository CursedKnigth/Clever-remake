import pygame
import random
from button import *

class InfoButton(Button):
    def __init__(self, screen, colour, x, y, width, height, r=0, border_width=0, border_colour=0, text=0, surface=0, func=0, info=0, empty=0):
        super().__init__(screen, colour, x, y, width, height, r=r, border_width=border_width, border_colour=border_colour, text=text, surface=surface, func=func, empty=empty)
        self.info = info

    def button_func(self, button): # this is here just to test empty buttons
        col = ["red", "green", "blue"]
        button.set_colour(random.choice(col))

    def get_info(self):
        return self.info
    
    def set_info(self, x):
        self.info = x
    
    def check_mouse(self, mouse): # function for checking if the button is pressed and running the associated function
        scale = self.screen.get_width()/1440
        if(not self.func):
            self.func = self.button_func
        mouse_pos = mouse.get_pos()

        if(self.active):
            if(mouse_pos[0]>self.x*scale and mouse_pos[0]<(self.x+self.width)*scale and
                mouse_pos[1]>self.y*scale and mouse_pos[1]<(self.y+self.width)*scale):
                self.func(self)