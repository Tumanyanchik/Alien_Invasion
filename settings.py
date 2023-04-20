class Settings:
    """Initialize game settings"""

    def __init__(self):
        # Screen parameters
        self.SCREEN_HEIGHT = 800
        self.SCREEN_WIDTH = 1200
        self.bg_color = (230, 230, 230)

        # Speed of sheep
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        self.bullets_alowed = 3
