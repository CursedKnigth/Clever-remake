import pygame
from object import *

class Button(GameObject):
    def button_func(self):
        self.x += 10

    def check_pressed(self, mouse, func=0):
        if(not func):
            func = self.button_func()
        pressed = mouse.get_pressed()
        mouse_pos = mouse.get_pos()

        if(pressed.button1 and 
           mouse_pos.x>self.x and mouse_pos.x<self.x+self.width and
           mouse_pos.y>self.y and mouse_pos.y<self.y+self.width):
               func()