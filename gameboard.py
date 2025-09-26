import pygame

class GameBoard():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.w = self.screen.get_width() / 11 * 5 - 5
        self.h = self.screen.get_height()-self.y-5

    def draw(self):
        r = 25
        pygame.draw.rect(self.screen, "grey", 
                         pygame.Rect(self.x, self.y, self.w, self.h),
                         border_top_left_radius=r, border_top_right_radius=r, border_bottom_left_radius=r, border_bottom_right_radius=r)
        