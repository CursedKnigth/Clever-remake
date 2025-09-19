import pygame
from movingobject import *

# set up pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
circle = 0
dt = 0

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    if(not circle):
       circle = MovingGameObject(screen, pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2), "green", 50)

    circle.draw()

    keys = pygame.key.get_pressed()

    circle.move(keys, dt)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()