import pygame
from pygame.sprite import Sprite

class bullet(Sprite):
    """ A class to fire bullets from the ship """
    def __init__(self, ai_game):
        """ Creating a bullet object at the current position of the ship"""
        super().__init__()
        self.screen = ai_game.screen
        self.Setting = ai_game.Setting
        self.color = self.Setting.bullet_color

        # create a bullet rect at(0,0) and then set current position
        self.rect= pygame.Rect(0,0, self.Setting.bullet_width, self.Setting.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #store the buttle's postition at a decimal value
        self.y = float (self.rect.y)

    def update(self):
        """ Move the the bullet the up the screen"""
        # update the decimal position of the bullet
        self.y -= self.Setting.bullet_speed

        #update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw the bullet on the screen """
        pygame.draw.rect(self.screen, self.color, self.rect)




