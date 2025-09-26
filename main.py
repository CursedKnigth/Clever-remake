import pygame
from movingobject import *
from button import *

# set up pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# initiate objects
obj = MovingGameObject(screen, "green", screen.get_width() / 2, screen.get_height() / 2, 50, 100)
butn = Button(screen, "blue", 50, screen.get_height() / 2, 100, 50)


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    obj.draw()
    butn.draw()

    #get needed events for controll
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse

    obj.move(keys, dt)
    butn.check_pressed(mouse)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()