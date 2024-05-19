import sys
from time import sleep
import pygame
from Setting import Setting
from GameStats import GameStats
from Scoreboard import Scoreboard
from Button import Button
from ship import Ship
from bullet import bullet
from Alien import Alien



class AlienInvasion:
    """ Overall class to manage game assets and behaviour"""
    def __init__(self):
        """initiate the game and its resources"""
        pygame.init()
        self.Setting = Setting()

        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.Setting.screen_width = self.screen.get_rect().width
        self.Setting.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("AlienInvasion")

        # Create a instance to store game stats and a scoreboard
        self.stats= GameStats(self)
        self.sb = Scoreboard(self)


        #DECLARE A SHIP CLASS
        self.ship= Ship(self)
        self.bullet =pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()

        self._create_fleet()

        #make the play button
        self.play_button = Button(self, "play")

        #set the background color
        self.bg_color=self.Setting.bg_color

    def run_game(self):
        """ Starts the main Loop for the game"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self.bullet.update()
                self._update_bullet()
                self._update_aliens()
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
            elif event.type== pygame.MOUSEBUTTONDOWN:
                mouse_pos =pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)




    def _check_play_button(self, mouse_pos):
        """ start A  NEW GAME WHEN THE PLAYER CLICKS ON PLAY"""

        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #reset the game settings
            self.Setting.initialize_dynamic_Setting()

            #reset the game statistics
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()


            #get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullet.empty()

            #create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            #hide the mouse cursor
            pygame.mouse.set_visible(False)
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

            self._check_bullet_alien_collisions()

        #check for any bullets that have hit any aliens.
        #if so get the rid of bullet and alien


    def _check_bullet_alien_collisions(self):
        """ Respond to bullet alien collisions"""
        # remove any bullets from the ship that did'nt collided with aliens
        collisions = pygame.sprite.groupcollide(self.bullet,self.aliens,True,True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.Setting.alien_points*len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # destroy exisiting bullet and create a new fleet.
            self.bullet.empty()
            self._create_fleet()
            self.Setting.increase_speed()

            #increase level
            self.stats.level +=1
            self.sb.prep_level()




    def _update_aliens(self):
        """ update the positions of the aliens of the fleet"""
        self._check_fleet_edges()
        self.aliens.update()

        #look for alien -ship collisions.
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()

        #look for aliens hitting the bottom of the screen
        self._check_alien_bottom()


    def _ship_hit(self):
        """ Respond to ship hit by the aliens and decrement ships left"""
        if self.stats.ships_left >0:
            # decrement the ship left
            self.stats.ships_left -=1
            self.sb.prep_ships()

            # get rid of the remaining aliens and bullets.
            self.aliens.empty()
            self.bullet.empty()

            # create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            #pause
            sleep(0.5)
        else:
            self.stats.game_active=False
            pygame.mouse.set_visible(True)


    def _check_alien_bottom(self):
        """ check if the aliens have reached the bottom of the screen """
        screen_rect =self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # treat this the same as if the ship got hit
                self._ship_hit()
                break







    def _create_fleet(self):
        """" create the fleet of aliens"""
        # make an alien and find the numvbers of alien u can fit ina  row
        #spacing of alien is equal to one alien width
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        available_space_x= self.Setting.screen_width-(2*alien_width)
        number_aliens_x =available_space_x // (2*alien_width)


        #Determine the number of rows of rows of aliens u can fit in a screen
        ship_height =self.ship.rect.height
        available_space_y = (self.Setting.screen_height- (2 * alien_height)-ship_height)
        number_rows = available_space_y //(2 * alien_height)


        #create a first row of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self,alien_number,row_number):
        """ create an alIEN AND PLACE IT IN A ROW"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x =alien_width + 2* alien_width * alien_number
        alien.rect.x=alien.x
        alien.rect.y = alien_height+2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """ Respond appropriately if alien has reached the end of the screen"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break




    def _change_fleet_direction(self):
        """ Drop the fleet and then change the direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.Setting.fleet_drop_speed
        self.Setting.fleet_direction *= -1

    def _update_screen(self):
        # redraw the screen during each pass through the loop.
        self.screen.fill(self.Setting.bg_color)
        self.ship.blitme()
        for bullet in self.bullet.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #draw the score information
        self.sb.show_score()

        #draw the play button if the game is Inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
        # make the most recent drawn screen visible
        pygame.display.flip()



if __name__== '__main__':
    # make the game instance and run the game
    ai = AlienInvasion()
    ai.run_game()





