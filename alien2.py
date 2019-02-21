import pygame

import constants

from spritesheet_functions import SpriteSheet
from pygame.sprite import Sprite


class Alien2(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien, and set its starting position."""
        super(Alien2, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.blueframes = []
        self.exframes = []
        self.lives = 0

        # Load the alien image, and set its rect attribute.
        sprite_sheet = SpriteSheet('images/spreadsheet3.png')

        # self.image = sprite_sheet.get_image(352, 0, 32, 32)
        image = sprite_sheet.get_image(0, 128, 32, 32)
        self.blueframes.append(image)
        image = sprite_sheet.get_image(32, 128, 32, 32)
        self.blueframes.append(image)
        image = sprite_sheet.get_image(64, 128, 32, 32)
        self.blueframes.append(image)
        image = sprite_sheet.get_image(0, 160, 32, 32)
        self.blueframes.append(image)
        image = sprite_sheet.get_image(32, 160, 32, 32)
        self.blueframes.append(image)
        image = sprite_sheet.get_image(64, 160, 32, 32)
        self.blueframes.append(image)
        image = sprite_sheet.get_image(0, 192, 32, 32)
        self.blueframes.append(image)

        self.image = self.blueframes[0]

        sprite_sheet = SpriteSheet('images/spreadsheet.png')

        image2 = sprite_sheet.get_image(96, 0, 32, 32)
        image2 = pygame.transform.rotate(image2, 90)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        image2 = sprite_sheet.get_image(96, 32, 32, 32)
        image2 = pygame.transform.rotate(image2, 90)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        image2 = sprite_sheet.get_image(96, 64, 32, 32)
        image2 = pygame.transform.rotate(image2, 90)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        image2 = sprite_sheet.get_image(64, 0, 32, 32)
        image2 = pygame.transform.rotate(image2, 90)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        image2 = sprite_sheet.get_image(64, 32, 32, 32)
        image2 = pygame.transform.rotate(image2, 90)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        image2 = sprite_sheet.get_image(64, 64, 32, 32)
        image2 = pygame.transform.rotate(image2, 90)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        image2 = sprite_sheet.get_image(32, 0, 32, 32)
        image2 = pygame.transform.rotate(image2, 90)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        image2 = sprite_sheet.get_image(32, 32, 32, 32)
        image2 = pygame.transform.rotate(image2, 90)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        image2 = sprite_sheet.get_image(32, 64, 32, 32)
        image2 = pygame.transform.rotate(image2, 90)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        image2 = sprite_sheet.get_image(0, 0, 32, 32)
        image2 = pygame.transform.rotate(image2, 90)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)
        self.exframes.append(image2)

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
        frame = (pos // 30) % len(self.blueframes)
        self.image = self.blueframes[frame]

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
