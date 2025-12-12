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
        self.active_player = 1
        self.current_scale = 1

        self.dicebox = DiceBox(self.screen)
        self.gameboard1 = GameBoard(self.screen, 5, 125, self.dicebox)
        self.gameboard2 = GameBoard(self.screen, 5 + self.screen.get_width() / 11 * 6, 125, self.dicebox)

        self.Font=pygame.font.SysFont('timesnewroman',  35)
        self.butn = Button(self.screen, "lightgreen", 950, self.screen.get_height() / 5, 100, 50, func=self.dicebox.roll_dice, text=self.Font.render("roll", False, "black"))
        self.butn2 = Button(self.screen, "lightgreen", 1100, self.screen.get_height() / 5, 100, 50, func=self.dicebox.confirm_pick, text=self.Font.render("pick", False, "black"))
        self.butn3 = Button(self.screen, "lightgreen", 1250, self.screen.get_height() / 5, 100, 50, func=self.dicebox.reset_dice, text=self.Font.render("reset-d", False, "black"))
        self.butn4 = Button(self.screen, "lightgreen", 800, self.screen.get_height() / 5, 100, 50, func=self.end_turn, text=self.Font.render("switch", False, "black"))
    
    def tick(self, keys):
        scale = self.screen.get_width()/DEF_SCREEN_WIDTH
        if(scale!=self.current_scale):
            self.current_scale = scale
            self.Font=pygame.font.SysFont('timesnewroman',  int(35*scale))
            self.butn.set_text(self.Font.render("roll", False, "black"))
            self.butn2.set_text(self.Font.render("pick", False, "black"))
            self.butn3.set_text(self.Font.render("reset-d", False, "black"))
            self.butn4.set_text(self.Font.render("switch", False, "black"))

        self.gameboard1.draw()
        self.gameboard2.draw()
        self.butn.draw()
        self.butn2.draw()
        self.butn3.draw()
        self.butn4.draw()
        self.dicebox.draw()

        if(self.active_player==1):
            self.gameboard1.check_dice()
        elif(self.active_player==2):
            self.gameboard2.check_dice()
    
    def check_mouse(self, event):
        self.butn.check_mouse(self.mouse, event)
        self.butn2.check_mouse(self.mouse, event)
        self.butn3.check_mouse(self.mouse, event)
        self.butn4.check_mouse(self.mouse, event)
        self.dicebox.check_mouse(self.mouse, event)
        self.gameboard1.check_mouse(self.mouse, event)
        self.gameboard2.check_mouse(self.mouse, event)

    def end_turn(self):
        if(self.active_player==1):
            self.dicebox.set_active_player(2)
            self.gameboard1.hide_n_deactivate()
            self.active_player = 2
        else:
            self.dicebox.set_active_player(1)
            self.gameboard2.hide_n_deactivate()
            self.active_player = 1
