import pygame.font

class UniversalLabel:
    def __init__(self, game, msg, width, height, bg_color, text_color, font, size, pos, x, y):
        """A class to manage the the universal label."""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        
        # Dimensions and properties
        self.width, self.height = width, height
        self.bg_color = bg_color
        self.text_color = text_color
        self.font = pygame.font.SysFont(font, size)

        #  Making the label (had to go thru hell to figure how to make this part universal :D)
        if x == 0 and y == 0:
            # This scenario occurs if the user specified a pos and not x and y coordinates.
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            rect = self.rect # This is for getattr() to do its job
            screen_rect = self.screen_rect # This is for getattr() to do its job
            rect2 = getattr(screen_rect, pos) # This is the equivalent of "self.screen_rect.pos"
            setattr(rect, pos, rect2) # Finally, equalize the two rects (this is just self.rect.pos = self.screen_rect.pos)
        else:
            # This happens if the user wants to use exact coordinates.
            self.rect = pygame.Rect(x, y, self.width, self.height)

        # render
        self.rendermsg(msg=msg)

    def rendermsg(self, msg):
        """Render the label in the requested part of the screen (taking the flag into account)."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.bg_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """Draw the label to the screen (taking the flag in account)."""
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class UniversalImage:
    """A class to manage the universal image to be rendered in."""
    def __init__(self, game, image, pos, x, y):
        """Initialize the cookie."""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Load the cookie image and get its rect.
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        # Positioning (according to x and y specifications)
        if x == 0 and y == 0:
            # This scenario occurs when the user has not specified any x/y coordinates and wishes to use the PyGame positions.
            rect = self.rect
            screen_rect = self.screen_rect
            rect2 = getattr(screen_rect, pos)
            setattr(rect, pos, rect2)
        else:
            # This happens when the user has specified x/y coords and wishes to use them rather than PyGame positions.
            # First, save the x and y poses of the rect as floats for editing.
            self.x = float(self.rect.x)
            self.y = float(self.rect.y)
            
            # Then, edit the floats appropriately as requested by the user.
            self.x = x
            self.y = y

            # Finally, equalize the floats with the rect.x and rect.y vars.
            self.rect.x = self.x
            self.rect.y = self.y
    
    def draw(self):
        """Finally, draw the image to the screen at the specified size and position."""
        self.screen.blit(self.image, self.rect)