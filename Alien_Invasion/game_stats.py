class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self,ai_game):
        """Initialize statistics"""
        self.settings = ai_game.setting
        self.reset_status()
        # Start Alien Invasion in a inactive state
        self.game_active = False

        # High score shoudl never be reset.
        self.high_score = 0
    
    
    def reset_status(self):
        """Initialize the statistics that can change during the game."""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    
    