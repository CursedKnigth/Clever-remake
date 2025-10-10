import pygame

class GameObject: # base object
    def __init__(self, screen, colour, x, y, width, height):
        self.screen = screen
        self.x = x
        self.y = y
        self.colour = colour
        self.height = height
        self.width = width
        self.visible = 1

    def draw(self):
        if(self.visible):
            pygame.draw.rect(self.screen, self.colour, pygame.Rect(self.x, self.y, self.width, self.height))

    def hide(self):
        self.visible = 0
    
    def show(self):
        self.visible = 1
    
    def set_pos(self, x, y):
        self.x = x
        self.y = y