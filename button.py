import pygame
import random
from object import *

class Button(GameObject): # base button object
    def __init__(self, screen, colour, x, y, width, height, r=0, border_width=0, border_colour=0, text=0, surface=0, func=0, empty=0):
        super().__init__(screen, colour, x, y, width, height, r=r, border_width=border_width, border_colour=border_colour, text=text, surface=surface, empty=empty)
        self.active = 1
        self.func = func

    def button_func(self): # this is here just to test empty buttons
        col = ["red", "green", "blue"]
        self.colour = random.choice(col)

    def check_mouse(self, mouse): # function for checking if the button is pressed and running the associated function
        if(not self.func):
            self.func = self.button_func
        mouse_pos = mouse.get_pos()

        if(self.active):
            if(mouse_pos[0]>self.x and mouse_pos[0]<self.x+self.width and
                mouse_pos[1]>self.y and mouse_pos[1]<self.y+self.width):
                self.func()

    def deactivate(self):
        self.active = 0
    
    def activate(self):
        self.active = 1
    
