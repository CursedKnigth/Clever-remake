import pygame
from button import *

class DiceButton(Button): # a modified button object meant to be used for the dice box
    def __init__(self, *args, **kwargs):
        super(DiceButton, self).__init__(*args, **kwargs)
        self.select_state = 0 
        self.number = 0
        # 0 - not selected
        # 1 - selected as main
        # 2 - selected as lesser
        # (the main dice is the one you'd use to mark something on the board and the lesser ones will move to the dice plate)

    
    def draw(self, surface):
        dimmed_colours = {"yellow" : "gold3", "blue" : "darkblue", "green" : "green3", "purple" : "purple4", "orange" : "orange3", "white" : "grey80"}
        r = 5
        if(self.visible):
            if(self.select_state == 0):
                pygame.draw.rect(self.screen, self.colour, pygame.Rect(self.x, self.y, self.width, self.height),
                                border_top_left_radius=r, border_top_right_radius=r, border_bottom_left_radius=r, border_bottom_right_radius=r)
            if(self.select_state == 1): # adds a red border
                pygame.draw.rect(self.screen, self.colour, pygame.Rect(self.x, self.y, self.width, self.height),
                                border_top_left_radius=r, border_top_right_radius=r, border_bottom_left_radius=r, border_bottom_right_radius=r)
                pygame.draw.rect(self.screen, "red", pygame.Rect(self.x, self.y, self.width, self.height),
                                border_top_left_radius=r, border_top_right_radius=r, border_bottom_left_radius=r, border_bottom_right_radius=r,
                                width=3)
            if(self.select_state == 2): # dims the colour
                pygame.draw.rect(self.screen, dimmed_colours[self.colour], pygame.Rect(self.x, self.y, self.width, self.height),
                                border_top_left_radius=r, border_top_right_radius=r, border_bottom_left_radius=r, border_bottom_right_radius=r)
        # idk how ill write the number
        a = 10
        b = 10
        #pygame.freetype.Font.render_to(surface, (self.x + a, self.y + b), str(self.number))
    
    def set_number(self, n):
        self.number = n

    """
    def select_main(): 

    def select_lesser():
    
    def wipe_select():
    """