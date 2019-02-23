import pygame
import pygame.font
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from Button2 import Button1
from ship import Ship
from alien import Alien
from alien1 import Alien1
from alien2 import Alien2
from bunker import Bunker
import game_functions as gf
from spritesheet_functions import SpriteSheet



def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Space Invaders")

    pygame.mixer.music.load('Super Space Invader Theme.mp3')
    pygame.mixer.music.play(-1)
    # Make the Play button.
    high_button = Button1(ai_settings, screen, "")
    play_button = Button(ai_settings, screen, "Play Now")

    high_score_file = open("high_score.txt", "r")
    high_score = int(high_score_file.read())
    high_score_file.close()
    print("The high score is", high_score)

    
    # Create an instance to store game statistics, and a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    bullets2 = Group()
    aliens = Group()
    bunkers = Group()
    bunker = Bunker(ai_settings, screen)
    alien = Alien(ai_settings, screen)

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    gf.create_bunkers(ai_settings, screen, ship, bunkers)

    # Start the main loop for the game.
    while True:

        gf.check_events(ai_settings, screen, stats, sb, play_button, high_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, alien, aliens, bunker, bunkers, bullets, bullets2, play_button, high_button)
            gf.update_bullets2(ai_settings, screen, stats, sb, ship, aliens, bunker, bunkers, bullets, bullets2)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, bullets2)

            if pygame.time.get_ticks() % 300 == 10:
                gf.fire_bullet2(ai_settings, screen, aliens, bullets2)

        gf.update_screen(ai_settings, screen, stats, sb, ship, alien, aliens, bunker, bunkers, bullets, bullets2, play_button, high_button)

        if stats.score > high_score:
            high_score_file = open("high_score.txt", "w")
            high_score_file.write(str(stats.score))
            high_score_file.close()

run_game()
