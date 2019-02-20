import pygame

import constants

from spritesheet_functions import SpriteSheet
from pygame.sprite import Sprite


class Alien1(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien, and set its starting position."""
        super(Alien1, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.redframes = []

        # Load the alien image, and set its rect attribute.
        sprite_sheet = SpriteSheet('images/spreadsheet.png')

        # self.image = sprite_sheet.get_image(352, 0, 32, 32)
        image = sprite_sheet.get_image(352, 96, 32, 32)
        self.redframes.append(image)
        image = sprite_sheet.get_image(384, 96, 32, 32)
        self.redframes.append(image)
        image = sprite_sheet.get_image(416, 96, 32, 32)
        self.redframes.append(image)
        image = sprite_sheet.get_image(352, 128, 32, 32)
        self.redframes.append(image)
        image = sprite_sheet.get_image(384, 128, 32, 32)
        self.redframes.append(image)
        image = sprite_sheet.get_image(416, 128, 32, 32)
        self.redframes.append(image)
        image = sprite_sheet.get_image(352, 160, 32, 32)
        self.redframes.append(image)

        self.image = self.redframes[0]

        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
        pos = self.rect.x
        frame = (pos // 30) % len(self.redframes)
        self.image = self.redframes[frame]

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
