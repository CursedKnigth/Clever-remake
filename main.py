# set up pygame
import pygame
pygame.init()
screen = pygame.display.set_mode((1440, 920), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
dt = 0
surface = pygame.Surface((screen.get_width(), screen.get_height())) # needed for displaying fonts and images
mouse = pygame.mouse

from game import *

game = Game(screen, mouse)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.check_mouse(event)
        
        if event.type == pygame.QUIT:
            running = False

    #get needed events for controll
    keys = pygame.key.get_pressed()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray15")

    game.tick(keys)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate independent physics.
    dt = clock.tick(60) / 1000

pygame.display.quit()