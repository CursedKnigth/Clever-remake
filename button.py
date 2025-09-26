import pygame
from object import *

class Button(GameObject):
    def button_func(self):
        self.x += 20

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