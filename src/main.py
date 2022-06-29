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
size = (1920, 1080)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Starship Galactica')
player = spaceship(screen, white)


def main():
    run_game = True
    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
        screen.fill(black)

        ####################
        # game logic
        ####################
        player.create_player()
        player.move_player()

        pygame.display.update()

    pygame.quit()


main()
