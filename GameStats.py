class GameStats:
    """ Track statistics of alien Invasion"""
    def __init__(self,ai_game):
        """ Intialise statistics"""
        self.Setting = ai_game.Setting
        self.reset_stats()
        # START THE ALIEN INVASION IN ACTIVE STATE
        self.game_active = True

    def reset_stats(self):
        """ Intialise the stats that can change during the game"""
        self.ships_left =self.Setting.ship_limit