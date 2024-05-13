class Setting:
    """"A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialise the game setting"""
        #screen setting
        self.screen_width =1200
        self.screen_height =800
        self.bg_color=(255,250,240)

        # ship setting
        self.ship_speed= 5
        self.ship_limit =3

        # Bullet setting
        self.bullet_speed= 1.0
        self.bullet_width= 3.0
        self.bullet_height = 20
        self.bullet_color =(60,60,60)
        self.bullet_allowed =3

        #alien setting
        self.alien_speed = .5
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right; -1 represent -1
        self.fleet_direction = 1