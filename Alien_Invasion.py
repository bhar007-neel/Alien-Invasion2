import sys
import pygame
from Setting import Setting
from ship import Ship
from bullet import bullet


class AlienInvasion:
    """ Overall class to manage game assets and behaviour"""
    def __init__(self):
        """initiate the game and its resources"""
        pygame.init()
        self.Setting =Setting()

        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.Setting.screen_width = self.screen.get_rect().width
        self.Setting.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("AlienInvasion")

        #DECLARE A SHIP CLASS
        self.ship= Ship(self)
        self.bullet =pygame.sprite.Group()

        #set the background color
        self.bg_color=self.Setting.bg_color

    def run_game(self):
        """ Starts the main Loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullet.update()
            self._update_bullet()
            self._update_screen()




    def _check_events(self):
        """ Responds for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)





    def _check_keydown_events(self,event):
        ''' respond to the key releases '''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()




    def _check_keyup_events(self,event):
         """ checkn for key release  """
         if event.key == pygame.K_RIGHT:
             self.ship.moving_right = False
         elif event.key == pygame.K_LEFT:
             self.ship.moving_left = False


    def _fire_bullet(self):
        """ create a new bullet and add it to the group"""
        if len(self.bullet)<self.Setting.bullet_allowed:
            new_bullet = bullet(self)
            self.bullet.add(new_bullet)

    def _update_bullet(self):
        """ Update the position of the bullet and get rid of the old bullets"""

        #update the bullet position
        # getting rid of bullets that has dissappeared
        for bullet in self.bullet.copy():
            if bullet.rect.bottom <= 0:
                self.bullet.remove(bullet)
                print(len(self.bullet))



    def _update_screen(self):
        # redraw the screen during each pass through the loop.
        self.screen.fill(self.Setting.bg_color)
        self.ship.blitme()
        for bullet in self.bullet.sprites():
            bullet.draw_bullet()

        # make the most recent drawn screen visible
        pygame.display.flip()



if __name__== '__main__':
    # make the game instance and run the game
    ai = AlienInvasion()
    ai.run_game()





