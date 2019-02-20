import pygame
import constants
from time import sleep
from pygame.sprite import Sprite
from spritesheet_functions import SpriteSheet


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the ship, and set its starting position."""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.shipframes = []
        self.shipex = []

        # Load the ship image, and get its rect.
        sprite_sheet = SpriteSheet('images/spreadsheet.png')
        image = sprite_sheet.get_image(256, 128, 32, 32)
        self.shipframes.append(image)
        image = sprite_sheet.get_image(288, 128, 32, 32)
        self.shipframes.append(image)
        image = sprite_sheet.get_image(256, 160, 32, 32)
        self.shipframes.append(image)
        self.image = self.shipframes[0]

        image = sprite_sheet.get_image(96, 96, 32, 32)
        image = pygame.transform.rotate(image, 90)
        self.shipex.append(image)
        image = sprite_sheet.get_image(96, 128, 32, 32)
        image = pygame.transform.rotate(image, 90)
        self.shipex.append(image)
        image = sprite_sheet.get_image(96, 160, 32, 32)
        image = pygame.transform.rotate(image, 90)
        self.shipex.append(image)
        image = sprite_sheet.get_image(64, 96, 32, 32)
        image = pygame.transform.rotate(image, 90)
        self.shipex.append(image)
        image = sprite_sheet.get_image(64, 128, 32, 32)
        image = pygame.transform.rotate(image, 90)
        self.shipex.append(image)
        image = sprite_sheet.get_image(64, 160, 32, 32)
        image = pygame.transform.rotate(image, 90)
        self.shipex.append(image)
        image = sprite_sheet.get_image(32, 96, 32, 32)
        image = pygame.transform.rotate(image, 90)
        self.shipex.append(image)
        image = sprite_sheet.get_image(32, 128, 32, 32)
        image = pygame.transform.rotate(image, 90)
        self.shipex.append(image)
        image = sprite_sheet.get_image(32, 160, 32, 32)
        image = pygame.transform.rotate(image, 90)
        self.shipex.append(image)
        image = sprite_sheet.get_image(0, 96, 32, 32)
        image = pygame.transform.rotate(image, 90)
        self.shipex.append(image)
        image = sprite_sheet.get_image(0, 128, 32, 32)
        image = pygame.transform.rotate(image, 90)
        self.shipex.append(image)

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False
        
    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx

    def explosion(self, x):
        self.image = self.shipex[x]
        self.blitme()

    def update(self):

        """Update the ship's position, based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        frame = (pygame.time.get_ticks() // 300) % len(self.shipframes)
        self.image = self.shipframes[frame]

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
