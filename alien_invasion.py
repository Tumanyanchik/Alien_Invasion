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
        self.defaultscreen()
        pygame.display.set_caption("AlienInvasion")
        self.ship = Ship(self)

    def run_game(self):
        """Start main game cycle"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Process keys and mouse clicks"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        """Redraw screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        """Output last element which was drawn"""
        pygame.display.flip()

    def fullscreen(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

    def defaultscreen(self):
        self.screen = pygame.display.set_mode((self.settings.SCREEN_WIDTH,
                                               self.settings.SCREEN_HEIGHT))

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()

        if event.key == pygame.K_ESCAPE:
            self.defaultscreen()

        if event.key == pygame.K_f:
            self.fullscreen()

        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = True

        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = True

        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_down = True

        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_up = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = False

        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = False

        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_down = False

        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_up = False


if __name__ == '__main__':
    """Create and start game"""
    ai = AlienInvasion()
    ai.run_game()
