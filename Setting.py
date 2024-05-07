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