class GameStats:
    '''track stats for alien invasion'''

    def __init__(self, ai_game):
        '''initialize stats'''
        self.settings = ai_game.settings
        self.reset_stats()
        #high score should not be reset
        self.high_score = 0

    def reset_stats(self):
        '''init stats that can change during the game'''
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1