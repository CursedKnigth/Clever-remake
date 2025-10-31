import pygame
import random
from object import *

class Button(GameObject): # base button object
    def __init__(self, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)
        self.was_pressed = 0
        self.active = 1

    def button_func(self): # this is here just to test empty buttons
        col = ["red", "green", "blue"]
        self.colour = random.choice(col)

    def check_mouse(self, mouse, func=0): # function for checking if the button is pressed and running the associated function
        if(not func):
            func = self.button_func
        pressed = mouse.get_pressed()[0]
        mouse_pos = mouse.get_pos()

        if(pressed and self.active):
            if(mouse_pos[0]>self.x and mouse_pos[0]<self.x+self.width and
                mouse_pos[1]>self.y and mouse_pos[1]<self.y+self.width and 
                not self.was_pressed):
                func()
            self.was_pressed = 1
        else:
            self.was_pressed = 0

    def deactivate(self):
        self.active = 0
    
    def activate(self):
        self.active = 1
    
