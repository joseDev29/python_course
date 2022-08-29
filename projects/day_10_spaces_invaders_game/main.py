import math
import sys
from typing import Tuple
import pygame
import random


def get_speed_change_by_game_object(object_type: str, ) -> Tuple[float, float]:
    is_mac_os = sys.platform.startswith('darwin')

    match object_type:
        case 'player':
            return (3, 0) if is_mac_os else (0.4, 0)
        case 'enemy':
            return (3, 32) if is_mac_os else (0.4, 32)
        case 'bullet':
            return (0, 4) if is_mac_os else (0, 0.5)
        case _:
            return 0, 0


def draw_player(display: pygame.Surface, player: pygame.Surface, coords: Tuple[float, float]):
    display.blit(player, coords)


def draw_enemy(display: pygame.Surface, enemy: pygame.surface, coords: Tuple[float, float]):
    display.blit(enemy, coords)


def draw_bullet(display: pygame.Surface, bullet: pygame.surface, coords: Tuple[float, float]) -> bool:
    display.blit(bullet, (coords[0] + 16, coords[1] + 10))
    return True


def detect_collision(coords_1: Tuple[float, float], coords_2: Tuple[float, float]) -> bool:
    # distance = sqrt( (x2 - x1)^2 + (y2-y1)^2 )
    x_result = math.pow(coords_2[0] - coords_1[0], 2)
    y_result = math.pow(coords_2[1] - coords_1[1], 2)
    distance = math.sqrt(x_result + y_result)
    return distance < 24


def draw_score(display: pygame.Surface, font: pygame.font.Font, count: int, coords: Tuple[float, float]):
    text = font.render(f'Score: {count}', True, (255, 255, 255))
    display.blit(text, coords)


def draw_end_text(display: pygame.Surface, font: pygame.font, coords: Tuple[float, float]):
    text = font.render('GAME OVER', True, (255, 255, 255))
    display.blit(text, coords)


def main():
    # Init package
    pygame.init()

    # Create display
    display = pygame.display.set_mode((800, 600))

    # Load images
    alien_icon = pygame.image.load('assets/images/alien_icon.png')
    space_background_img = pygame.image.load('assets/images/space_background.jpg')
    space_ship_img = pygame.image.load('assets/images/space_ship.png')
    alien_enemy_img = pygame.image.load('assets/images/alien_enemy.png')
    bullet_img = pygame.image.load('assets/images/bullet.png')

    # Load sounds
    pygame.mixer.music.load('assets/sounds/background_song.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    shot_sound = pygame.mixer.Sound('assets/sounds/shot.mp3')
    collision_sound = pygame.mixer.Sound('assets/sounds/collision.mp3')

    # Set icon and title
    pygame.display.set_caption('Space Invaders')
    pygame.display.set_icon(alien_icon)

    # Player
    player_x = 368
    player_y = 536
    player_x_change = 0
    player_y_change = 0

    # Enemy
    enemies_x = []
    enemies_y = []
    enemies_x_change = []
    enemies_y_change = []
    enemies_count = 8

    for index in range(enemies_count):
        enemy_speed_change = get_speed_change_by_game_object('enemy')
        enemies_x.append(random.randint(0, 736))
        enemies_y.append(random.randint(50, 200))
        enemies_x_change.append(enemy_speed_change[0])
        enemies_y_change.append(enemy_speed_change[1])

    # Bullet
    bullet_x = 0
    bullet_y = 500
    bullet_x_change = 0
    bullet_y_change = get_speed_change_by_game_object('bullet')[0]
    bullet_visible = False

    score = 0
    font = pygame.font.Font('freesansbold.ttf', 32)
    score_x = 10
    score_y = 10

    exit_program = False

    while not exit_program:

        # display.fill((205, 144, 228))
        display.blit(space_background_img, (0, 0))

        for event in pygame.event.get():

            match event.type:
                case pygame.QUIT:
                    exit_program = True
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_LEFT:
                            player_x_change = -get_speed_change_by_game_object('player')[0]
                        case pygame.K_RIGHT:
                            player_x_change = get_speed_change_by_game_object('player')[0]
                        case pygame.K_SPACE:
                            if not bullet_visible:
                                shot_sound.play()
                                bullet_x = player_x
                                bullet_visible = draw_bullet(display, bullet_img, (bullet_x, bullet_y))
                case pygame.KEYUP:
                    match event.key:
                        case pygame.K_LEFT:
                            player_x_change = 0
                        case pygame.K_RIGHT:
                            player_x_change = 0

        # Change player position
        player_x += player_x_change
        player_y += player_y_change

        # Avoid player collapse
        if player_x <= 0:
            player_x = 0
        if player_x >= 736:
            player_x = 736

        if bullet_y <= -64:
            bullet_y = 500
            bullet_visible = False

        if bullet_visible:
            draw_bullet(display, bullet_img, (bullet_x, bullet_y))
            bullet_y -= bullet_y_change

        for index in range(enemies_count):

            if enemies_y[index] > 500:
                for sub_index in range(enemies_count):
                    enemies_y[sub_index] = 1000
                draw_end_text(display, font, (60, 200))
                break

            # Change enemy position
            enemies_x[index] += enemies_x_change[index]

            # Avoid enemy collapse
            if enemies_x[index] <= 0:
                enemies_x_change[index] = get_speed_change_by_game_object('enemy')[0]
                enemies_y[index] += enemies_y_change[index]
            if enemies_x[index] >= 736:
                enemies_x_change[index] = -get_speed_change_by_game_object('enemy')[0]
                enemies_y[index] += enemies_y_change[index]

            collision = detect_collision((enemies_x[index], enemies_y[index]), (bullet_x, bullet_y))

            if collision and bullet_visible:
                collision_sound.play()
                bullet_y = 500
                bullet_visible = False
                score += 1
                enemies_x[index] = random.randint(0, 736)
                enemies_y[index] = random.randint(50, 200)

            draw_enemy(display, alien_enemy_img, (enemies_x[index], enemies_y[index]))

        draw_player(display, space_ship_img, (player_x, player_y))
        draw_score(display, font, score, (score_x, score_y))

        pygame.display.update()


main()
