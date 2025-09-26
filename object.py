import pygame

class GameObject:
    def __init__(self, screen, colour, x, y, width, height):
        self.screen = screen
        self.x = x
        self.y = y
        self.colour = colour
        self.height = height
        self.width = width

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, pygame.Rect(self.x, self.y, self.width, self.height))