
# I've now made this object obsolete, rest in piss (2025-2025)

import pygame
from button import *
from constants import *

class DiceButton(Button): # a modified button object meant to be used for the dice box
    # the "info button" was made later than this one and would probably make more sense to use, but I can't be bothered
    # jesus christ im realising just how awfully this is made
    def __init__(self, *args, **kwargs):
        super(DiceButton, self).__init__(*args, **kwargs)
        self.select_state = 0 
        # 0 - not selected
        # 1 - selected as main
        # 2 - selected as lesser
        # (the main dice is the one you'd use to mark something on the board and the lesser ones will move to the dice plate)
        self.number = 0
        self.Font=pygame.font.SysFont('timesnewroman',  90)
        self.num_to_txt = {1 : self.Font.render("1", False, "black"),
                        2 : self.Font.render("2", False, "black"),
                        3 : self.Font.render("3", False, "black"),
                        4 : self.Font.render("4", False, "black"),
                        5 : self.Font.render("5", False, "black"),
                        6 : self.Font.render("6", False, "black")}
    
    def draw(self, screen):
        r = 5
        if(self.visible):
            if(self.select_state == 0):
                pygame.draw.rect(self.screen, self.colour, pygame.Rect(self.x, self.y, self.width, self.height), border_radius=r)
            if(self.select_state == 1): # adds a red border
                pygame.draw.rect(self.screen, self.colour, pygame.Rect(self.x, self.y, self.width, self.height), border_radius=r)
                pygame.draw.rect(self.screen, "red", pygame.Rect(self.x, self.y, self.width, self.height), border_top_left_radius=r, width=3)
            if(self.select_state == 2): # dims the colour
                pygame.draw.rect(self.screen, DIMMED_COLOURS_MAP[self.colour], pygame.Rect(self.x, self.y, self.width, self.height), border_radius=r)
        x = 15
        y = 0
        screen.blit(self.num_to_txt[self.number], (self.x + x, self.y + y))
    
    def set_number(self, n):
        self.number = n

    def select_main(self): 
        self.select_state = 1

    def select_lesser(self):
        self.select_state = 2
    
    def wipe_select(self):
        self.select_state = 0

    def check_mouse(self, mouse, dicebox): # modifying the button function so it will use the function I want
        pressed = mouse.get_pressed()[0]
        mouse_pos = mouse.get_pos()

        if(pressed and self.active):
            if(mouse_pos[0]>self.x and mouse_pos[0]<self.x+self.width and
                mouse_pos[1]>self.y and mouse_pos[1]<self.y+self.width and 
                not self.was_pressed):
                dicebox.pick_dice(self.colour)
            self.was_pressed = 1
        else:
            self.was_pressed = 0