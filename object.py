import pygame

class GameObject: # base object
    def __init__(self, screen, colour, x, y, width, height, r=0, border_width=0, border_colour=0):
        self.screen = screen
        self.x = x
        self.y = y
        self.colour = colour
        self.height = height
        self.width = width
        self.visible = 1
        self.r = r
        self.border_width = border_width
        self.border_colour = border_colour

    def draw(self):
        if(self.visible):
            pygame.draw.rect(self.screen, self.colour, pygame.Rect(self.x, self.y, self.width, self.height), border_radius=self.r)
            if(self.border_width!=0):
                pygame.draw.rect(self.screen, self.border_colour, pygame.Rect(self.x, self.y, self.width, self.height), width=self.border_width, border_radius=self.r)

    def hide(self):
        self.visible = 0
    
    def show(self):
        self.visible = 1
    
    def set_pos(self, x, y):
        self.x = x
        self.y = y