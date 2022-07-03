import pygame
from player import player as spaceship
from laser import laser
pygame.init()

####################
# colours
###################
black = (10, 10, 10)

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

    run_game = True
    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

        ####################
        # game logic
        ####################
        screen.fill(black)
        key_pressed = pygame.key.get_pressed()

        player.create_player()
        player_x_axis = player.move_player(key_pressed)

        player_laser.create_laser(key_pressed, player_x_axis)
        player_laser.move_laser()

        pygame.display.update()

    pygame.quit()


main()
