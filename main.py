import pygame
from movingobject import *
from object import *
from button import *
from gameboard import *

# set up pygame
pygame.init()
screen = pygame.display.set_mode((1440, 920))
clock = pygame.time.Clock()
running = True
button_pressed = 0
dt = 0

# initiate objects
#obj = MovingGameObject(screen, "green", screen.get_width() / 2, screen.get_height() / 2, 50, 100)
butn = Button(screen, "blue", 50, screen.get_height() / 2, 100, 50)
line1 = GameObject(screen, "red", screen.get_width() / 11 * 5, 0, 1, screen.get_height())
line2 = GameObject(screen, "red", screen.get_width() / 11 * 6, 0, 1, screen.get_height())
line_top = GameObject(screen, "red", screen.get_width() / 2, screen.get_height() / 2, 50, 100)
gameboard = GameBoard(screen, 5, 125)


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray15")

    #obj.draw()
    butn.draw()
    line1.draw()
    line2.draw()
    gameboard.draw()

    #get needed events for controll
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse

    #obj.move(keys, dt)
    button_pressed = butn.check_mouse(mouse, button_pressed)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.display.quit()