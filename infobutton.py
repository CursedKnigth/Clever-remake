import pygame
from button import *

class InfoButton(Button):
    def __init__(self, screen, colour, x, y, width, height, r=0, border_width=0, border_colour=0, text=0, surface=0, func=0, info=0):
        super().__init__(screen, colour, x, y, width, height, r=r, border_width=border_width, border_colour=border_colour, text=text, surface=surface, func=func)
        self.info = info

    def button_func(self, button): # this is here just to test empty buttons
        col = ["red", "green", "blue"]
        button.set_colour(col)

    def get_info(self):
        return self.info
    
    def check_mouse(self, mouse): # function for checking if the button is pressed and running the associated function
        if(not self.func):
            self.func = self.button_func
        pressed = mouse.get_pressed()[0]
        mouse_pos = mouse.get_pos()

        if(pressed and self.active):
            if(mouse_pos[0]>self.x and mouse_pos[0]<self.x+self.width and
                mouse_pos[1]>self.y and mouse_pos[1]<self.y+self.width and 
                not self.was_pressed):
                self.func(self)
            self.was_pressed = 1
        else:
            self.was_pressed = 0