import pygame.font
from pygame.sprite import Group
from ship import Ship
class Scoreboard:
    """ A class to report scorebord information"""
    def __init__(self,ai_game):
        self.ai_game=ai_game
        self.screen=ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.setting = ai_game.Setting
        self.stats = ai_game.stats


        #font setting for score information
        self.text_color=(30,30,30)
        self.font = pygame.font.SysFont(None,48)


        #prepare to initialise score images

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_ships(self):
        """show how many ships are left"""
        self.ships= Group()
        for ship_number in range(self.stats.ships_left):
            ship =Ship(self.ai_game)
            ship.rect.x = 5.0 + ship_number * ship.rect.width
            ship.rect.y = 5.0
            self.ships.add(ship)




    def prep_level(self):
        """ turn the level into the rounded image"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.setting.bg_color)

        # display the score at the top right of the screen
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom +10
    def prep_high_score(self):
        high_score = round(self.stats.score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.setting.bg_color)

        # display the score at the top right of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def prep_score(self):
        """ TURN THE SCORE IN THE RENDERED IMAGE"""
        rounded_score= round(self.stats.score,-1)
        score_str= "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.setting.bg_color)


        #display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -20
        self.score_rect.top = 20

    def show_score(self):
        """draw the score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()