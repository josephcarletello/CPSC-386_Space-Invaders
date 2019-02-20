import pygame
import constants
from time import sleep
from pygame.sprite import Sprite
from spritesheet_functions import SpriteSheet


class Bunker(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the ship, and set its starting position."""
        super(Bunker, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.lives = 0
        self.i = 0
        self.x = 0
        self.frames = []
        self.exframes = []

        # Load the ship image, and get its rect.
        sprite_sheet = SpriteSheet('images/spreadsheet4.png')
        image = sprite_sheet.get_image(0, 0, 32, 32)
        image = pygame.transform.scale(image, (64, 64))
        self.frames.append(image)
        image = sprite_sheet.get_image(32, 0, 32, 32)
        image = pygame.transform.scale(image, (64, 64))
        self.frames.append(image)
        image = sprite_sheet.get_image(64, 0, 32, 32)
        image = pygame.transform.scale(image, (64, 64))
        self.frames.append(image)
        image = sprite_sheet.get_image(0, 32, 32, 32)
        image = pygame.transform.scale(image, (64, 64))
        self.frames.append(image)
        image = sprite_sheet.get_image(32, 32, 32, 32)
        image = pygame.transform.scale(image, (64, 64))
        self.frames.append(image)
        image = sprite_sheet.get_image(64, 32, 32, 32)
        image = pygame.transform.scale(image, (64, 64))
        self.frames.append(image)
        image = sprite_sheet.get_image(0, 64, 32, 32)
        image = pygame.transform.scale(image, (64, 64))
        self.frames.append(image)
        image = sprite_sheet.get_image(32, 64, 32, 32)
        image = pygame.transform.scale(image, (64, 64))
        self.frames.append(image)
        image = sprite_sheet.get_image(64, 64, 32, 32)
        image = pygame.transform.scale(image, (64, 64))
        self.frames.append(image)
        image = sprite_sheet.get_image(0, 96, 32, 32)
        image = pygame.transform.scale(image, (64, 64))
        self.frames.append(image)
        image = sprite_sheet.get_image(32, 96, 32, 32)
        image = pygame.transform.scale(image, (64, 64))
        self.frames.append(image)
        image = sprite_sheet.get_image(64, 96, 32, 32)
        image = pygame.transform.scale(image, (64, 64))
        self.frames.append(image)
        self.image = self.frames[0]

        # Load the ship image, and get its rect.
        sprite_sheet = SpriteSheet('images/spreadsheet5.png')
        image2 = sprite_sheet.get_image(0, 0, 32, 32)
        image2 = pygame.transform.scale(image, (64, 64))
        self.exframes.append(image)
        image2 = sprite_sheet.get_image(32, 0, 32, 32)
        image2 = pygame.transform.scale(image, (64, 64))
        self.exframes.append(image)
        image2 = sprite_sheet.get_image(64, 0, 32, 32)
        image2 = pygame.transform.scale(image, (64, 64))
        self.exframes.append(image)
        image2 = sprite_sheet.get_image(0, 32, 32, 32)
        image2 = pygame.transform.scale(image, (64, 64))
        self.exframes.append(image)
        image2 = sprite_sheet.get_image(32, 32, 32, 32)
        image2 = pygame.transform.scale(image, (64, 64))
        self.exframes.append(image)
        image2 = sprite_sheet.get_image(64, 32, 32, 32)
        image2 = pygame.transform.scale(image, (64, 64))
        self.exframes.append(image)
        image2 = sprite_sheet.get_image(0, 64, 32, 32)
        image2 = pygame.transform.scale(image, (64, 64))
        self.exframes.append(image)
        image2 = sprite_sheet.get_image(32, 64, 32, 32)
        image2 = pygame.transform.scale(image, (64, 64))
        self.exframes.append(image)
        image2 = sprite_sheet.get_image(64, 64, 32, 32)
        image2 = pygame.transform.scale(image, (64, 64))
        self.exframes.append(image)
        image2 = sprite_sheet.get_image(0, 96, 32, 32)
        image2 = pygame.transform.scale(image, (64, 64))
        self.exframes.append(image)
        image2 = sprite_sheet.get_image(32, 96, 32, 32)
        image2 = pygame.transform.scale(image, (64, 64))
        self.exframes.append(image)

        self.rect = self.image.get_rect()
        self.x = self.rect.width + 4 * self.rect.width * 4
        self.rect.x = self.x
        self.rect.y = 450

    def hit(self):
        if self.lives < 11:
            self.lives = self.lives + 1
            print(self.lives)
            self.image = self.frames[self.lives]
            self.update()
        else:
            # self.explosion(self.lives)
            self.lives = 0

    def explosion(self, x):
        x = 0
        while x < 10:
            self.image = self.exframes[x]
            self.update()
            x = x + 1

    def update(self):
        self.blitme()

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
