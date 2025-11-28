import pygame
from constants import *
from movingobject import *
from object import *
from button import *
from gameboard import *
from dicebox import *
from constants import *

class Game:
    def __init__(self, screen, mouse):
        self.gamestate = GAME_RUNNING
        self.screen = screen
        self.mouse = mouse

        self.line1 = GameObject(self.screen, "red", self.screen.get_width() / 11 * 5, 0, 1, self.screen.get_height()) # right now most of this is temporary
        self.line2 = GameObject(self.screen, "red", self.screen.get_width() / 11 * 6, 0, 1, self.screen.get_height())
        self.line_top = GameObject(self.screen, "red", self.screen.get_width() / 2, self.screen.get_height() / 2, 50, 100)
        self.dicebox = DiceBox(self.screen)
        self.gameboard = GameBoard(self.screen, 5, 125, self.dicebox)
        self.butn = Button(self.screen, "blue", 950, self.screen.get_height() / 2, 100, 50, func=self.dicebox.roll_dice)
        self.butn2 = Button(self.screen, "red", 1100, self.screen.get_height() / 2, 100, 50, func=self.dicebox.confirm_pick)
        self.butn3 = Button(self.screen, "green", 1250, self.screen.get_height() / 2, 100, 50, func=self.dicebox.reset_dice)
    
    def tick(self, keys):
        self.line1.draw()
        self.line2.draw()
        self.gameboard.draw()
        self.butn.draw()
        self.butn2.draw()
        self.butn3.draw()
        self.dicebox.draw()

        self.gameboard.check_dice()
    
    def check_mouse(self, event):
        self.butn.check_mouse(self.mouse, event)
        self.butn2.check_mouse(self.mouse, event)
        self.butn3.check_mouse(self.mouse, event)
        self.dicebox.check_mouse(self.mouse, event)
        self.gameboard.check_mouse(self.mouse, event)
