import pygame


class Ship:
    """Class for control ship"""

    def __init__(self, ai_game):
        """Initialize ship"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load image of ship and get recatangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # New ship appears near bottom edge of screen
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Flags for move ship
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update position ship"""
        if self.moving_right and (self.rect.right < self.screen_rect.right):
            self.x += self.settings.ship_speed

        if self.moving_left and (self.rect.left > 0):
            self.x -= self.settings.ship_speed

        if self.moving_up and (self.rect.top > 0):
            self.y -= self.settings.ship_speed

        if self.moving_down and (self.rect.bottom < self.screen_rect.bottom):
            self.y += self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Output ship on screen"""
        self.screen.blit(self.image, self.rect)
