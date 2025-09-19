import pygame

class GameObject:
    def __init__(self, screen, pos, colour, size):
        self.screen = screen
        self.pos = pos
        self.colour = colour
        self.size = size

    def draw(self):
        pygame.draw.circle(self.screen, self.colour, self.pos, self.size)