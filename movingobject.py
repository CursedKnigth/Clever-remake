import pygame
from object import *

class MovingGameObject(GameObject):
    def move(self, keys, dt):
        if keys[pygame.K_w]:
            self.pos.y -= 300 * dt
        if keys[pygame.K_s]:
            self.pos.y += 300 * dt
        if keys[pygame.K_a]:
            self.pos.x -= 300 * dt
        if keys[pygame.K_d]:
            self.pos.x += 300 * dt