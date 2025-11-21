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
        self.default_img_width = self.board_img.get_width()
        self.default_img_height = self.board_img.get_height()
        self.warped_board_img = self.board_img
        self.yellow_game_board = YellowGameBoard(screen, self.x, self.y)
        self.current_scale = 1

    def draw(self):
        r = 25
        """
        pygame.draw.rect(self.screen, "grey", 
                         pygame.Rect(self.x, self.y, self.width, self.height),
                         border_top_left_radius=r, border_top_right_radius=r, border_bottom_left_radius=r, border_bottom_right_radius=r)
        """
        scale = self.screen.get_width()/1440
        if(scale!=self.current_scale):
            self.warped_board_img = pygame.transform.scale(self.board_img, (self.default_img_width*scale, self.default_img_height*scale))
            self.current_scale = scale
        self.screen.blit(self.warped_board_img, ((self.x+9)*scale, (self.y+178)*scale))
        self.yellow_game_board.draw()
        
    def check_mouse(self, mouse):
        self.yellow_game_board.check_mouse(mouse)

    def check_dice(self, dicebox):
        self.yellow_game_board.check_dice(dicebox)