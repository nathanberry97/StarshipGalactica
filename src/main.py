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

    ####################
    # laser variables
    ####################
    laser = [[]]
    bullet_next_tick = 0
    bullet_interval = 200

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

        ####################
        # laser logic add
        ####################
        tick = pygame.time.get_ticks()
        if key_pressed[pygame.K_LCTRL] or key_pressed[pygame.K_SPACE]:
            if tick > bullet_next_tick:
                bullet_next_tick = tick + bullet_interval
                laser.append(
                    [(x_axis / 100 * 50) + 10,
                     (y_axis / 100 * 90)]
                )

        ####################
        # laser logic move
        ####################
        if len(laser) > 1:
            index = 0
            for bullet in laser:
                if index != 0:
                    bullet_coorinates = [
                       bullet[0], bullet[1], 5, 5
                    ]
                    pygame.draw.rect(
                        screen,
                        white,
                        bullet_coorinates
                    )
                    bullet[1] -= 5
                    if bullet[1] <= 0:
                        laser.remove(laser[0])
                else:
                    index += 1

        pygame.display.update()

    pygame.quit()


main()
