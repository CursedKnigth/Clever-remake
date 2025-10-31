# set up pygame
import pygame
pygame.init()
screen = pygame.display.set_mode((1440, 920))
clock = pygame.time.Clock()
running = True
dt = 0

#import objects
from movingobject import *
from object import *
from button import *
from gameboard import *
from dicebox import *
from constants import *

# initiate objects
surface = pygame.Surface((screen.get_width(), screen.get_height())) # needed for displaying fonts and images
#obj = MovingGameObject(screen, "green", screen.get_width() / 2, screen.get_height() / 2, 50, 100)
line1 = GameObject(screen, "red", screen.get_width() / 11 * 5, 0, 1, screen.get_height()) # right now most of this is temporary
line2 = GameObject(screen, "red", screen.get_width() / 11 * 6, 0, 1, screen.get_height())
line_top = GameObject(screen, "red", screen.get_width() / 2, screen.get_height() / 2, 50, 100)
gameboard = GameBoard(screen, 5, 125)
dicebox = DiceBox(screen)
butn = Button(screen, "blue", 950, screen.get_height() / 2, 100, 50)
butn2 = Button(screen, "red", 1100, screen.get_height() / 2, 100, 50)
butn3 = Button(screen, "green", 1250, screen.get_height() / 2, 100, 50)


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #get needed events for controll
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray15")

    #obj.draw()
    
    line1.draw()
    line2.draw()
    gameboard.draw(screen)
    butn.draw()
    butn2.draw()
    butn3.draw()
    dicebox.draw(screen)

    #obj.move(keys, dt)
    butn.check_mouse(mouse, func=dicebox.roll_dice)
    butn2.check_mouse(mouse, func=dicebox.confirm_pick)
    butn3.check_mouse(mouse, func=dicebox.reset_dice)
    dicebox.check_mouse(mouse)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate independent physics.
    dt = clock.tick(60) / 1000

pygame.display.quit()