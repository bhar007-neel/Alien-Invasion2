import pygame
import self
from pygame.sprite import Sprite

class Alien(Sprite):
    """ Initialise the alien and set it starting positions"""
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.Setting = ai_game.Setting


        #LOAD THE ALIEN IMAGE AND ITS RECT ATTRIBUTE
        self.image =pygame.image.load('images/alien.bmp')
        self.rect =self.image.get_rect()


        #start each aliern near the top left of the screen
        self.rect.x =self.rect.width
        self.rect.y = self.rect.height

        #store the alien exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Returns true if the alien hits the edge of the screen """
        screen_rect= self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """ Move the alien to the right"""
        self.x += (self.Setting.alien_speed * self.Setting.fleet_direction)
        self.rect.x = self.x

