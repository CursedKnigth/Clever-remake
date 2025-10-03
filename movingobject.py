import pygame
from object import *

class MovingGameObject(GameObject): # this was just me testing pygame, probably not important for this project
    def move(self, keys, dt):
        if keys[pygame.K_w]:
            self.y -= 300 * dt
        if keys[pygame.K_s]:
            self.y += 300 * dt
        if keys[pygame.K_a]:
            self.x -= 300 * dt
        if keys[pygame.K_d]:
            self.x += 300 * dt