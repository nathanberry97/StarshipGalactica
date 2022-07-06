import pygame
from player import player as spaceship
from enemy import enemy
from laser import laser
pygame.init()

####################
# pygame variables
####################
clock = pygame.time.Clock()
fps = 60
screen_size = (1280, 720)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Starship Galactica')


def main():
    ####################
    # dimensions screen
    ####################
    dimensions = (
        str(screen).split("(")[1].split(" ")[0].split("x")
    )

    x_axis = int(dimensions[0])
    y_axis = int(dimensions[1])

    ####################
    # player object
    ####################
    player = spaceship(
        screen, x_axis, y_axis
    )

    ####################
    # laser object
    ####################
    player_laser = laser(
        screen, y_axis
    )

    ####################
    # enemy objects
    ####################
    enemies = []
    enemy_x_axis = 100
    enemy_y_axis = y_axis / 100 * 10
    enemy_direction = 1
    enemy_count = 0
    amount_of_aliens = 23

    for create_aliens in range(amount_of_aliens):
        enemies.append(enemy(screen, enemy_x_axis, enemy_y_axis))
        enemy_x_axis += 140

        if create_aliens == 7:
            enemy_x_axis = 175
            enemy_y_axis = y_axis / 100 * 20

        elif create_aliens == 14:
            enemy_x_axis = 100
            enemy_y_axis = y_axis / 100 * 30

    ####################
    # background vars
    ####################
    background = pygame.image.load('assets/backgroud.png').convert()
    background_y_axis = [
        0, -720, -1440
    ]

    run_game = True
    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

        clock.tick(fps)
        ####################
        # game logic
        ####################
        for background_update in range(len(background_y_axis)):
            screen.blit(background, [0, background_y_axis[background_update]])
            background_y_axis[background_update] += 1
            if background_y_axis[background_update] > 720:
                background_y_axis[background_update] = -1440

        key_pressed = pygame.key.get_pressed()

        player.create_player()
        player_x_axis = player.move_player(key_pressed)

        player_laser.create_laser(key_pressed, player_x_axis)
        laser_coordinates = player_laser.move_laser()

        for test in enemies:
            test.create_enemy()
            enemy_count = test.move_enemy(enemy_direction)

        if enemy_count == 120:
            enemy_direction = 0
        elif enemy_count == 0:
            enemy_direction = 1

        pygame.display.update()

    pygame.quit()


main()
