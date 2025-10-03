import pygame
import random
from object import *

class Button(GameObject): # base button object
    def __init__(self, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)
        self.was_pressed = 0

    def button_func(self): # this is here just to test empty buttons
        col = ["red", "green", "blue"]
        self.colour = random.choice(col)

    def check_mouse(self, mouse, was_pressed, func=0): 
        if(not func):
            func = self.button_func
        pressed = mouse.get_pressed()[0]
        mouse_pos = mouse.get_pos()

        if(pressed):
            if(mouse_pos[0]>self.x and mouse_pos[0]<self.x+self.width and
                mouse_pos[1]>self.y and mouse_pos[1]<self.y+self.width and 
                not was_pressed):
                func()
            return 1
        return 0 
    
