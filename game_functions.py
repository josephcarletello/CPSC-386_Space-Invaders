import sys
from time import sleep

import pygame
import inspect

from bullet import Bullet
from bulletA import Bullet2
from alien import Alien
from alien1 import Alien1
from alien2 import Alien2
from bunker import Bunker
from spritesheet_functions import SpriteSheet



def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to key presses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
        gun_sound = pygame.mixer.Sound('Laser Gun Sound Effect.wav')
        gun_sound.play()
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_button, high_button, ship, aliens, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, high_button, ship, aliens, bullets, mouse_x, mouse_y)
            check_high_button(ai_settings, screen, stats, sb, play_button, high_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_button, high_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()
        
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        
        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True
        
        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        
        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def check_high_button(ai_settings, screen, stats, sb, play_button, high_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks High."""
    button_clicked = high_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet, if limit not reached yet."""
    # Create a new bullet, add to bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def fire_bullet2(ai_settings, screen, alien, bullets2):
    """Fire a bullet, if limit not reached yet."""
    # Create a new bullet, add to bullets group.
    if len(bullets2) < 5:
        new_bullet2 = Bullet2(ai_settings, screen, alien)
        bullets2.add(new_bullet2)


def update_screen(ai_settings, screen, stats, sb, ship, alien, aliens, bunker, bunkers, bullets, bullets2, play_button, high_button):
    """Update images on the screen, and flip to the new screen."""
    # Redraw the screen, each pass through the loop.
    screen.fill(ai_settings.bg_color)
    
    # Redraw all bullets, behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for bulletA in bullets2.sprites():
        bulletA.draw_bullet2()
    ship.blitme()
    # aliens.draw(screen)
    # bunkers.draw(screen)
    for bunker in bunkers.sprites():
        bunker.blitme()
        if bunker.lives > 10:
            bunker.image = bunker.exframes[bunker.lives-10]
            bunker.lives = bunker.lives + 1
        if bunker.lives > 53:
            bunkers.remove(bunker)

    for alien in aliens:
        alien.blitme()
        if alien.lives >= 1:
                if alien.__class__ == Alien:
                    alien.image = alien.exframes[alien.lives]
                    alien.blitme()
                    alien.lives = alien.lives + 1
                    if alien.lives == 45:
                        aliens.remove(alien)

                if alien.__class__ == Alien1:
                    alien.image = alien.exframes[alien.lives]
                    alien.blitme()
                    alien.lives = alien.lives + 1
                    if alien.lives == 45:
                        aliens.remove(alien)

                if alien.__class__ == Alien2:
                    alien.image = alien.exframes[alien.lives]
                    alien.blitme()
                    alien.lives = alien.lives + 1
                    if alien.lives == 45:
                        aliens.remove(alien)
            # stats.score += ai_settings.alien_points * len(aliens)

    # alien.explosion()

    # Draw the score information.
    sb.show_score()
    
    # Draw the play button if the game is inactive.
    if not stats.game_active:
        high_button.draw_button()
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, alien, aliens, bunker, bunkers, bullets, bullets2, play_button, high_button):
    """Update position of bullets, and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, alien, aliens, bunker, bunkers, bullets, bullets2, play_button, high_button)
    check_bullet_bunker_collisions(ai_settings, screen, stats, sb, ship, aliens, bunker, bunkers, bullets, bullets2)


def update_bullets2(ai_settings, screen, stats, sb, ship, aliens, bunker, bunkers, bullets, bullets2):
    """Update position of bullets, and get rid of old bullets."""
    # Update bullet positions.
    bullets2.update()

    # Get rid of bullets that have disappeared.
    for bulletA in bullets2.copy():
        if bulletA.rect.top >= 600:
            bullets2.remove(bulletA)

    check_bullet_bunker_collisions(ai_settings, screen, stats, sb, ship, aliens, bunker, bunkers, bullets, bullets2)
    check_bullet_ship_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, bullets2)


def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def check_bullet_ship_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, bullets2):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.spritecollide(ship, bullets2, True)

    if collisions:
        death_sound = pygame.mixer.Sound('Minecraft Oof.wav')
        death_sound.play()
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, bullets2)




def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, alien, aliens, bunker, bunkers, bullets, bullets2, play_button, high_button):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, False)

    if collisions:

        death_sound = pygame.mixer.Sound('Minecraft Oof.wav')
        death_sound.play()

        for aliens in collisions.values():
            for alien in aliens:
                alien.lives = 1
                if alien.__class__ == Alien:
                    stats.score += ai_settings.alien_points3

                if alien.__class__ == Alien1:
                    stats.score += ai_settings.alien_points2

                if alien.__class__ == Alien2:
                    stats.score += ai_settings.alien_points
            # stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    
    if len(aliens) == 0:
        # If the entire fleet is destroyed, start a new level.
        bullets.empty()
        ai_settings.increase_speed()
        
        # Increase level.
        stats.level += 1
        sb.prep_level()
        
        create_fleet(ai_settings, screen, ship, aliens)


def update_screen4(ai_settings, screen, stats, sb, ship, alien, aliens, bunker, bunkers, bullets, bullets2, play_button, high_button):
    """Update images on the screen, and flip to the new screen."""
    # Redraw the screen, each pass through the loop.
    timer = pygame.time.get_ticks()
    alien.blitme()
    passed = pygame.time.get_ticks() - timer
    if passed <= 200 or 400 < passed <= 600:
        alien.blitme()
    elif 600 < passed:
        alien.update()


def check_bullet_bunker_collisions(ai_settings, screen, stats, sb, ship, aliens, bunker, bunkers, bullets, bullets2):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, bunkers, True, False)
    if collisions:
        bunker_hit(ai_settings, screen, stats, sb, bunker, bunkers, ship, aliens, bullets)
        bunker.lives = bunker.lives + 1

        # for bunkers in collisions.values():


def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet, and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_screen2(ai_settings, ship, screen, sb, aliens):
    """Update images on the screen, and flip to the new screen."""
    # Redraw the screen, each pass through the loop.
    screen.fill(ai_settings.bg_color)

    ship.blitme()
    aliens.draw(screen)

    # Draw the score information.
    sb.show_score()

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, bullets2):
    """Respond to ship being hit by alien."""

    x = 0
    death_sound = pygame.mixer.Sound('Minecraft Oof.wav')
    death_sound.play()
    while x < 10:
        ship.explosion(x)
        update_screen2(ai_settings, ship, screen, sb, aliens)
        sleep(0.15)
        x = x + 1

    sleep(0.5)

    if stats.ships_left > 0:
        # Decrement ships_left.
        stats.ships_left -= 1
        
        # Update scoreboard.
        sb.prep_ships()
        
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    
    # Empty the list of aliens and bullets.
    aliens.empty()
    bullets.empty()




    # Create a new fleet, and center the ship.
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()
    
    # Pause.
    # sleep(0.5)


def bunker_hit(ai_settings, screen, stats, sb, bunker, bunkers, ship, aliens, bullets):
    """Respond to bunker being hit by bullet."""

    if bunker.lives < 11:
        for bunker in bunkers:
            bunker.lives = bunker.lives + 1
            bunker.image = bunker.frames[bunker.lives]
            bunker.update()


def update_screen3(ai_settings, ship, screen, sb, aliens, bunker, bunkers):
    """Update images on the screen, and flip to the new screen."""
    # Redraw the screen, each pass through the loop.
    screen.fill(ai_settings.bg_color)

    ship.blitme()
    aliens.draw(screen)
    bunker.blitme()

    # Draw the score information.
    sb.show_score()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets, bullets2):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, bullets2)
            break


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, bullets2):
    """
    Check if the fleet is at an edge,
      then update the postions of all aliens in the fleet.
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, bullets2)

    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets, bullets2)


def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height -
                            (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_bunker(ai_settings, screen, bunkers, bunker_number, row_number):
    bunker = Bunker(ai_settings, screen)
    bunker_width = bunker.rect.width
    bunker.x = bunker_width + 4 * bunker_width * bunker_number
    bunker.rect.x = bunker.x
    bunker.rect.y = 450
    # bunker.rect.y = bunker.rect.height + 4 * bunker.rect.height * row_number * 0.5
    bunkers.add(bunker)


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien, and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number * 0.75
    aliens.add(alien)


def create_alien1(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien, and place it in the row."""
    alien = Alien1(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number * 0.75
    aliens.add(alien)


def create_alien2(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien, and place it in the row."""
    alien = Alien2(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number * 0.75
    aliens.add(alien)


def create_bunkers(ai_settings, screen, ship, bunkers):

    number_bunkers_x = 4
    number_rows = 1

    # Create the fleet of bunkers.
    for row_number in range(number_rows):
        for bunker_number in range(number_bunkers_x):
            create_bunker(ai_settings, screen, bunkers, bunker_number, row_number)


def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    # Create an alien, and find number of aliens in a row.
    alien = Alien(ai_settings, screen)
    alien1 = Alien1(ai_settings, screen)
    # number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    # number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    number_aliens_x = 11
    number_rows = 2
    
    # Create the fleet of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien1(ai_settings, screen, aliens, alien_number, row_number + 2)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien2(ai_settings, screen, aliens, alien_number, row_number + 4)

