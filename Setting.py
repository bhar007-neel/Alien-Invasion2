class Setting:
    """"A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialise the game setting"""
        #screen setting
        self.screen_width =1200
        self.screen_height =800
        self.bg_color=(255,250,240)

        # ship setting
        self.ship_speed= 1.5


        # Bullet setting
        self.bullet_speed= 1.0
        self.bullet_width= 3.0
        self.bullet_height = 20
        self.bullet_color =(60,60,60)
        self.bullet_allowed =3

        #alien setting
        self.fleet_drop_speed=10

        #how quickly the game speeds up
        self.speed_scale=1.1

        # how quickly the alien score increases
        self.score_scale = 1.5

        self.initialize_dynamic_Setting()

    def initialize_dynamic_Setting(self):
        """ initialising setting that change throughout the game"""
        self.ship_limit=3
        self.bullet_speed =3.0
        self.alien_speed =1.0

        #fleet direction of 1 represents right; -1 represents left
        self.fleet_direction=1

        #scoring
        self.alien_points = 50


    def increase_speed(self):
        """ increase speed setting """
        self.ship_speed *= self.speed_scale
        self.bullet_speed *= self.speed_scale
        self.alien_speed *= self.speed_scale

        self.alien_points= int(self.alien_points * self.score_scale)



