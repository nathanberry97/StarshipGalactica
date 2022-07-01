import pygame
from player import player as spaceship
pygame.init()

####################
# colours
###################
white = (255, 255, 255)
black = (0, 0, 0)

####################
# pygame variables
####################
screen_size = (1000, 1080)
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
        screen, white, x_axis, y_axis
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
        player.move_player(key_pressed)

        pygame.display.update()

    pygame.quit()


main()
