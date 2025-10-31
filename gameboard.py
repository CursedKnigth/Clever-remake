import pygame
import images
from yellowboard import *

class GameBoard(): # this is going to act as the page youd get in the physical game
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = self.screen.get_width() / 11 * 5 - 5
        self.height = self.screen.get_height()-self.y-5
        self.board_img = images.board

    def draw(self):
        r = 25
        """
        pygame.draw.rect(self.screen, "grey", 
                         pygame.Rect(self.x, self.y, self.width, self.height),
                         border_top_left_radius=r, border_top_right_radius=r, border_bottom_left_radius=r, border_bottom_right_radius=r)
        """
        self.screen.blit(self.board_img, (self.x+9, self.y+178))
        