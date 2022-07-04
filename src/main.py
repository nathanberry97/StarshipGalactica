import pygame
from player import player as spaceship
from laser import laser
pygame.init()

####################
# pygame variables
####################
screen_size = (1280, 720)
screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
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

        ####################
        # game logic
        ####################
        for background_update in range(len(background_y_axis)):
            screen.blit(background, [0, background_y_axis[background_update]])
            background_y_axis[background_update] += 1.5
            if background_y_axis[background_update] > 720:
                background_y_axis[background_update] = -1440

        key_pressed = pygame.key.get_pressed()

        player.create_player()
        player_x_axis = player.move_player(key_pressed)

        player_laser.create_laser(key_pressed, player_x_axis)
        player_laser.move_laser()

        pygame.display.update()

    pygame.quit()


main()
