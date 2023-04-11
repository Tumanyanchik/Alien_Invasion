import pygame


class Ship:
    """Class for control ship"""

    def __init__(self, ai_game):
        """Initialize ship"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load image of ship and get recatangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # New ship appears near bottom edge of screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
