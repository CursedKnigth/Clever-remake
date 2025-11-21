import pygame

class GameObject: # base object
    def __init__(self, screen, colour, x, y, width, height, r=0, border_width=0, border_colour=0, text=0, surface=0, empty=0):
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
        self.og_text = text
        self.text = text
        self.surface = surface
        self.empty = empty
        self.cross_offset1 = 0
        self.cross_offset2 = 0
        self.cross_colour = 0
        self.current_scale = 1

    def draw(self):
        scale = self.screen.get_width()/1440
        if(self.visible):
            if(not self.empty):
                pygame.draw.rect(self.screen, self.colour, pygame.Rect(int(self.x*scale), int(self.y*scale), int(self.width*scale), int(self.height*scale)), border_radius=int(self.r*scale))
            
            if(self.border_width!=0):
                pygame.draw.rect(self.screen, self.border_colour, pygame.Rect(int(self.x*scale), int(self.y*scale), int(self.width*scale), int(self.height*scale)), width=int(self.border_width*scale), border_radius=int(self.r*scale))
            
            if(self.text!=0):
                self.screen.blit(self.text, (int(self.x*scale), int(self.y*scale)))
            
            if(self.cross_colour):
                pygame.draw.polygon(self.screen, self.cross_colour, (((self.x+self.cross_offset1)*scale, (self.y+self.cross_offset2)*scale), 
                                                                     ((self.x+self.cross_offset2)*scale, (self.y+self.cross_offset1)*scale), 
                                                                     ((self.x+self.width-self.cross_offset1)*scale, (self.y+self.height-self.cross_offset2)*scale), 
                                                                     ((self.x+self.width-self.cross_offset2)*scale, (self.y+self.height-self.cross_offset1)*scale)))
                
                pygame.draw.polygon(self.screen, self.cross_colour, (((self.x+self.width-self.cross_offset1)*scale, (self.y+self.cross_offset2)*scale), 
                                                                     ((self.x+self.width-self.cross_offset2)*scale, (self.y+self.cross_offset1)*scale), 
                                                                     ((self.x+self.cross_offset1)*scale, (self.y+self.height-self.cross_offset2)*scale), 
                                                                     ((self.x+self.cross_offset2)*scale, (self.y+self.height-self.cross_offset1)*scale)))

    def hide(self):
        self.visible = 0
    
    def show(self):
        self.visible = 1
    
    def set_pos(self, x, y):
        self.x = x
        self.y = y
    
    def set_colour(self, colour):
        self.colour = colour
    
    def set_border(self, width, colour):
        self.border_width = width
        self.border_colour = colour

    def set_text(self, text):
        self.text = text

    def set_empty(self, x):
        self.empty = x
    
    def set_cross(self, offset1, offset2, colour):
        self.cross_offset1 = offset1
        self.cross_offset2 = offset2
        self.cross_colour = colour