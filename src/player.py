import pygame
pygame.init()


class player:
    ####################
    # player variables
    ####################
    player_x = 950
    player_y = 1020
    player_size = 25

    def __init__(self, display, colour):
        self.display = display
        self.colour = colour

    def create_player(self):
        player_coorinates = [
            self.player_x, self.player_y, self.player_size, self.player_size
        ]
        ####################
        # draw player
        ####################
        pygame.draw.rect(
            self.display,
            self.colour,
            player_coorinates
        )

    def move_player(self):
        key_pressed = pygame.key.get_pressed()
        ####################
        # players movement
        ####################
        if self.player_x < 0:
            self.player_x = 1895
        elif key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
            self.player_x -= 5
        elif self.player_x > 1895:
            self.player_x = 25
        elif key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
            self.player_x += 5
