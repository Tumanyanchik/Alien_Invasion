import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Class for manage game resources and behavior"""

    def __init__(self):
        """Initialize and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.SCREEN_WIDTH,
                                               self.settings.SCREEN_HEIGHT))

        pygame.display.set_caption("AlienInvasion")
        self.ship = Ship(self)

    def run_game(self):
        """Start main game cycle"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Process keys and mouse clicks"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Redraw screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        """Output last element which was drawn"""
        pygame.display.flip()


if __name__ == '__main__':
    """Create and start game"""
    ai = AlienInvasion()
    ai.run_game()
