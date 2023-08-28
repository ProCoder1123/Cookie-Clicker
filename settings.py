import sys

class Settings: 
    """A class in which all settings for Cookie Clicker are stored and imported by the main.py file."""
    def __init__(self):
        """Initialize the settings for the game."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # Flags and counters
        self.increment = 1 # this is to tell the game how much to increase the cookies by (upgraded in-game)
        self.doubler_price = 50 # this is to tell the game how much the Doubler costs (doubles every purchase)
        self.doubler_lvl = 1 # sets the doubler's level
        self.menu = 1 # 1 - main menu, 2 - game, 3 - shop, 4 - settings
        self.fullscreen = False # False - not fullscreen, True - fullscreen
        self.autoclicker_lvl = 1 # sets the autoclicker's lvl
        self.autoclicker_price = 1500 # sets the price for the autoclicker (doubles every time)