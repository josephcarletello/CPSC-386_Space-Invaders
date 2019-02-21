import pygame
from pygame.sprite import Sprite


class Bullet2(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_settings, screen, alien):
        """Create a bullet object, at the alien's current position."""
        super(Bullet2, self).__init__()
        self.screen = screen

        # Create bullet rect at (0, 0), then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        for alien1 in alien:
            self.rect.centerx = alien1.rect.x
            self.rect.top = alien1.rect.y

        # Store a decimal value for the bullet's position.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = 0.75

    def update(self):
        """Move the bullet down the screen."""
        # Update the decimal position of the bullet.
        self.y += self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet2(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
