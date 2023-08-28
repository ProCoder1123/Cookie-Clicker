# This code uses my own universal PyGame label and button producer class, which you can find at https://github.com/ProCoder1123/pygame-button-creator
# It's the UniversalLabel class (edit: and the UniversalImage class, added later thru an update)

import pygame
import sys
import messagebox
from time import sleep

from settings import Settings
from universal import UniversalLabel
from universal import UniversalImage

class CookieClicker:
    """An overall class to manage the game."""
    def __init__(self):
        """Initialize the game, and create game settings."""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.caption = pygame.display.set_caption("Cookie Clicker")

        # Core game elements
        self.cookies = 1
    
    def run_game(self):
        """Run the game."""
        """Explanation: All three menus in the game have separate while loops, which are all into one big/master loop."""
        while True:
            while self.settings.menu == 1: # SCREEN I - MAIN MENU
                # Run all parts of the game that apply to the main menu.
                
                if not self.settings.menu == 1:
                    break # If the user clicked "Play", get out of the main menu and start the game. 

                self.events()
                self.elements1()
                self.autoclicker(self.settings.autoclicker_lvl)

                # Update screen
                pygame.display.flip()

            while self.settings.menu == 2: # SCREEN II - GAME MENU
                # Run all parts of the game before updating the screen.
                
                if self.settings.menu == 3 or self.settings.menu == 1:
                    break # If the user decided to enter the shop or to go back to the main menu, break out of this loop and go into the shop one

                self.events()
                self.elements2()
                self.autoclicker(self.settings.autoclicker_lvl)

                # Update screen
                pygame.display.flip()
            
            while self.settings.menu == 3: # SCREEN III - SHOP MENU
                # Again, run all parts of the game, but this time only the ones that apply to the shop. 
                
                if not self.settings.menu == 3:
                    break # If the user decided to go back, break out of this loop and enter the first one

                self.events()
                self.elements3()
                self.autoclicker(self.settings.autoclicker_lvl)

                # Update screen
                pygame.display.flip()

            while self.settings.menu == 4: # SCREEN IV - SETTINGS MENU
                # Run the parts of the game that apply to the settings menu.

                if not self.settings.menu == 4:
                    break # If the user decided to go back to the main menu, break out of this loop and enter the first one.

                self.events()
                self.elements4()
                self.autoclicker(self.settings.autoclicker_lvl)

                # Update screen
                pygame.display.flip()

    def events(self):
        """Check for any user interaction."""
        for event in pygame.event.get():
            self.quit(event)
            self.keydown(event)
            self.keyup(event)
            self.mousedown(event)
    
    def quit(self, event):
        """Check for a QUIT event."""
        if event.type == pygame.QUIT:
            sys.exit()
    
    def keydown(self, event):
        """Check for keydown events."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_a:
                messagebox.showinfo("About This Program", "This small little game was developed by Boyan Karshakov on Python 3.12, just for fun. \nI hope you enjoy playing it :)")
                messagebox.showinfo("Credits", "Program: Boyan Karshakov \nPyGame Label & Button Maker: Boyan Karshakov \nLanguage: Python 3.12 :)")
            if event.key == pygame.K_f:
                fullscreen_prompt = messagebox.askyesno("Cookie Clicker", "WARNING: \n\nGoing in fullscreen mode is irreversible! \n\nAre you sure you want to continue?")
                if fullscreen_prompt:
                    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    self.settings.fullscreen = True
                    
    
    def keyup(self, event):
        """Check for keyup events."""
        if event.type == pygame.KEYUP:
            pass # none for now
    
    def mousedown(self, event):
        """Check for mousebuttondown events."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            if self.settings.menu == 1:
                self.clicks1(mousepos)
            elif self.settings.menu == 2:
                self.clicks2(mousepos)
            elif self.settings.menu == 3:
                self.clicks3(mousepos)
            elif self.settings.menu == 4:
                self.clicks4(mousepos)
    
    def elements1(self):
        """Add elements to the main menu."""
        
        # First, fill the background with white.
        self.screen.fill(self.settings.bg_color)
        
        # Then, run factories and draweries for the main menu.
        self.factory1()
        self.drawing1()

    def factory1(self):
        """Produce buttons and labels for the main menu."""
        self.play_button = UniversalLabel(self, "Play", 600, 125, (255, 255, 0), (0, 0, 0), "Arial Bold", 108, None, 300, 200)
        self.play_button_fs = UniversalLabel(self, "Play", 600, 125, (255, 255, 0), (0, 0, 0), "Arial Bold", 108, None, 500, 200)
        self.intro_text = UniversalLabel(self, "Welcome to Cookie Clicker :)", 650, 75, (255, 255, 255), (0, 0, 0), "Arial Bold", 102, "midtop", 0, 0)
        self.about_button = UniversalLabel(self, "About", 600, 125, (0, 255, 0), (0, 0, 0), "Arial Bold", 104, None, 300, 350)
        self.about_button_fs = UniversalLabel(self, "About", 600, 125, (0, 255, 0), (0, 0, 0), "Arial Bold", 104, None, 500, 350)
        self.exit_button_main_menu = UniversalLabel(self, "Exit", 600, 125, (0, 0, 255), (0, 0, 0), "Arial Bold", 108, None, 300, 500)
        self.exit_button_main_menu_fs = UniversalLabel(self, "Exit", 600, 125, (0, 0, 255), (0, 0, 0), "Arial Bold", 108, None, 500, 500)
    
    def drawing1(self):
        """Draw the buttons and labels from above."""
        if not self.settings.fullscreen:
            self.play_button.draw()
            self.about_button.draw()
            self.exit_button_main_menu.draw()
        else:
            self.play_button_fs.draw()
            self.about_button_fs.draw()
            self.exit_button_main_menu_fs.draw()
        self.intro_text.draw()
        
        
    
    def clicks1(self, mouse_pos):
        """Register clicks for the main menu."""
        # First, save click results in vars.
        play = self.play_button.rect.collidepoint(mouse_pos)
        about = self.about_button.rect.collidepoint(mouse_pos)
        exitmainmenu = self.exit_button_main_menu.rect.collidepoint(mouse_pos)
        play_fs = self.play_button_fs.rect.collidepoint(mouse_pos)
        about_fs = self.about_button_fs.rect.collidepoint(mouse_pos)
        exitmainmenu_fs = self.exit_button_main_menu_fs.rect.collidepoint(mouse_pos)

# new programming next for fs buttons.
        # Then, if any of them showed positives, perform the appropriate action. 
        if play:
            self.settings.menu = 2
        elif about:
            messagebox.showinfo("About This Program", "This small little game was developed by Boyan Karshakov on Python 3.12, just for fun. \nI hope you enjoy playing it :)")
            messagebox.showinfo("Credits", "Program: Boyan Karshakov \nPyGame Label & Button Maker: Boyan Karshakov \nLanguage: Python 3.12 :)")
        elif exitmainmenu:
            sys.exit()
        elif play_fs:
            self.settings.menu = 2
        elif about_fs:
            messagebox.showinfo("About This Program", "This small little game was developed by Boyan Karshakov on Python 3.12, just for fun. \nI hope you enjoy playing it :)")
            messagebox.showinfo("Credits", "Program: Boyan Karshakov \nPyGame Label & Button Maker: Boyan Karshakov \nLanguage: Python 3.12 :)")
        elif exitmainmenu_fs:
            sys.exit()

    def elements2(self):
        """Add elements to the screen."""
        self.screen.fill(self.settings.bg_color)
        self.factory2()
        self.drawing2()

    def factory2(self):
        """This is where buttons and labels are 'produced' for the game part of the program."""
        self.counter1 = UniversalLabel(self, f"{self.cookies}", 75, 75, (255, 255, 255), (0, 0, 0), "Arial Bold", 108, "midtop", 0, 0)
        self.exit_button = UniversalLabel(self, "Exit", 225, 125, (255, 0, 0), (255, 255, 255), "Arial Bold", 108, "bottomright", 0, 0)
        self.shop_button = UniversalLabel(self, "Shop", 225, 125, (0, 0, 255), (255, 255, 255), "Arial Bold", 108, "bottomleft", 0, 0)
        self.main_button = UniversalLabel(self, "Main Menu", 700, 125, (0, 255, 0), (255, 255, 255), "Arial Bold", 106, "midbottom", 0, 0)
        self.settings_icon = UniversalImage(self, 'images/settingsicon.bmp', "topright", 0, 0)
        self.cookie = UniversalImage(self, 'images/cookie.bmp', "center", 0, 0)

    def drawing2(self):
        """And now they're displayed to the screen :D"""
        self.counter1.draw()
        self.exit_button.draw()
        self.shop_button.draw()
        self.main_button.draw()
        self.settings_icon.draw()
        self.cookie.draw()
    
    def clicks2(self, mouse_pos):
        """Check if any of the buttons in the game were clicked (for the main menu only)."""
        # First, save all click results in separate variables.
        cookie = self.cookie.rect.collidepoint(mouse_pos)
        exit = self.exit_button.rect.collidepoint(mouse_pos)
        shop1 = self.shop_button.rect.collidepoint(mouse_pos)
        main = self.main_button.rect.collidepoint(mouse_pos)
        settings = self.settings_icon.rect.collidepoint(mouse_pos)
        
        # Then, if any of them were clicked, do the appropriate action.
        if cookie: 
            self.cookies += self.settings.increment
        elif exit:
            sys.exit()
        elif shop1:
            self.settings.menu = 3
        elif main:
            self.settings.menu = 1
        elif settings:
            self.settings.menu = 4
    
    def clicks3(self, mouse_pos):
        """Check if any of the shop buttons were clicked."""
        # First, save click results as vars.
        back = self.back_button.rect.collidepoint(mouse_pos)
        doubler = self.double_button.rect.collidepoint(mouse_pos)
        autoclicker = self.autoclicker_button.rect.collidepoint(mouse_pos)

        # Then, if any of the vars were positive, perform the appropriate action.
        if back:
            self.settings.menu = 2
        elif doubler:
            if self.cookies >= self.settings.doubler_price and self.settings.doubler_lvl < 10:
                self.cookies -= self.settings.doubler_price
                self.settings.increment = self.settings.increment * 2
                self.settings.doubler_price = self.settings.doubler_price * 2
                self.settings.doubler_lvl += 1
            else:
                pass
        elif autoclicker:
            if self.cookies >= self.settings.autoclicker_price and self.settings.autoclicker_lvl < 10:
                self.cookies -= self.settings.autoclicker_price
                self.settings.autoclicker_lvl += 1
                self.settings.autoclicker_price = self.settings.autoclicker_price * 2

    def elements3(self):
        """Run the factory and drawery for the shop part of the game."""
        self.screen.fill(self.settings.bg_color)
        self.factory3()
        self.drawing3()

    def factory3(self):
        """Produce buttons and labels for the shop part of the game."""
        self.back_button = UniversalLabel(self, "Back", 225, 125, (255, 0, 0), (255, 255, 255), "Arial Bold", 108, "bottomleft", 0, 0)
        self.counter2 = UniversalLabel(self, f"{self.cookies}", 75, 75, (255, 255, 255), (0, 0, 0), "Arial Bold", 108, "midtop", 0, 0)
        self.double_button = UniversalLabel(self, f"Double Click {self.settings.doubler_lvl} (Price: {self.settings.doubler_price})", 750, 50, (176, 191, 26), (255, 255, 255), "Arial Bold", 60, None, 225, 250)
        self.double_button_max = UniversalLabel(self, "Max Level", 750, 50, (128, 128, 128), (0, 0, 0), "Arial Bold", 60, None, 225, 250)
        self.double_button_fs = UniversalLabel(self, f"Double Click {self.settings.doubler_lvl} (Price: {self.settings.doubler_price})", 750, 50, (176, 191, 26), (255, 255, 255), "Arial Bold", 60, None, 425, 250)
        self.double_button_max_fs = UniversalLabel(self, "Max Level", 750, 50, (128, 128, 128), (0, 0, 0), "Arial Bold", 60, None, 425, 250)
        self.autoclicker_button = UniversalLabel(self, f"AutoClicker {self.settings.autoclicker_lvl} (Price: {self.settings.autoclicker_price})", 750, 50, (255, 0, 0), (255, 255, 255), "Arial Bold", 60, None, 225, 300)
        self.autoclicker_button_max = UniversalLabel(self, "Max Level", 750, 50, (128, 128, 128), (0, 0, 0), "Arial Bold", 60, None, 225, 300)
        self.autoclicker_button_fs = UniversalLabel(self, f"AutoClicker {self.settings.autoclicker_lvl} (Price: {self.settings.autoclicker_price})", 750, 50, (255, 0, 0), (255, 255, 255), "Arial Bold", 60, None, 425, 300)
        self.autoclicker_button_max_fs = UniversalLabel(self, "Max Level", 750, 50, (128, 128, 128), (0, 0, 0), "Arial Bold", 60, None, 425, 300)

        
    
    def drawing3(self):
        """Drawing of the buttons and labels for the shop part of the game."""
        self.back_button.draw()
        self.counter2.draw()
        if not self.settings.fullscreen:
            if not self.settings.doubler_lvl == 10:
                self.double_button.draw()
            else:
                self.double_button_max.draw()
            
            if not self.settings.autoclicker_lvl == 10:
                self.autoclicker_button.draw()
            else:
                self.autoclicker_button_max.draw()
        else:
            if not self.settings.doubler_lvl == 10:
                self.double_button_fs.draw()
            else:
                self.double_button_max_fs.draw()
            
            if not self.settings.autoclicker_lvl == 10:
                self.autoclicker_button_fs.draw()
            else:
                self.autoclicker_button_max_fs.draw()

    def elements4(self):
        """Run the elements that apply to the settings part of the game."""
        self.screen.fill(self.settings.bg_color)
        self.factory4()
        self.drawing4()

    def factory4(self):
        """Produce the buttons and labels for the settings."""
        self.back_button_settings = UniversalLabel(self, "Back", 225, 125, (225, 0, 0), (255, 255, 255), "Arial Bold", 108, "bottomleft", 0, 0)
        self.settings_text = UniversalLabel(self, "Settings", 500, 75, (255, 255, 255), (0, 0, 0), "Arial Bold", 108, "midtop", 0, 0)
        self.fullscreen_button = UniversalLabel(self, "Fullscreen", 500, 150, (255, 0, 255), (0, 0, 0), "Arial Bold", 106, "center", 0, 0)
        self.fullscreen_on = UniversalLabel(self, "Fullscreen is ON", 700, 150, (128, 128, 128), (0, 0, 0), "Arial Bold", 106, "center", 0, 0)

    def drawing4(self):
        """Draw the elements from above."""
        self.back_button_settings.draw()
        self.settings_text.draw()
        if not self.settings.fullscreen:
            self.fullscreen_button.draw()
        else:
            self.fullscreen_on.draw()

    def clicks4(self, mouse_pos):
        """Register clicks for the settings part of the game."""
        # First, record click results
        back = self.back_button_settings.rect.collidepoint(mouse_pos)
        fullscreen = self.fullscreen_button.rect.collidepoint(mouse_pos)

        # Then, check all of them for needed actions
        if back:
            self.settings.menu = 2
        elif fullscreen:
            fullscreen_prompt = messagebox.askyesno("Cookie Clicker", "WARNING: \n\nGoing in fullscreen mode is irreversible! \n\nAre you sure you want to continue?")
            if fullscreen_prompt:
                pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                self.settings.fullscreen = True
            else:
                pass
    def autoclicker(self, lvl):
        """Keeps the autoclicker running whenever activated."""
        if not lvl == 1: 
            if lvl == 2:
                self.cookies += 2
            elif lvl == 3:
                self.cookies += 5
            elif lvl == 4:
                self.cookies += 33
            elif lvl == 5:
                self.cookies += 55
            elif lvl == 6:
                self.cookies += 102
            elif lvl == 7:
                self.cookies += 211
            elif lvl == 8:
                self.cookies += 453
            elif lvl == 9:
                self.cookies += 781
            elif lvl == 10:
                self.cookies += 1432
            elif lvl == 11:
                self.cookies += 2132


if __name__ == '__main__':
    # Create a game instance and run the game.
    instance = CookieClicker()
    instance.run_game()