import pygame


class player:

    def __init__(self, display, x_axis, y_axis):
        self.display = display
        self.x_axis = x_axis

        ####################
        # player variables
        ####################
        self.ship_sprite = (
            pygame.image.load('assets/spaceship.png').convert_alpha()
        )
        self.player_size = 75
        self.player_x = x_axis / 100 * 47
        self.player_y = y_axis / 100 * 85

    def create_player(self):
        ####################
        # import sprite
        ####################
        self.display.blit(
            self.ship_sprite, (self.player_x, self.player_y)
        )

    def move_player(self, key_pressed):
        ####################
        # players movement
        ####################
        if self.player_x < 0:
            self.player_x = 0
        elif key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
            self.player_x -= 5
        elif self.player_x > self.x_axis - self.player_size:
            self.player_x = self.x_axis - self.player_size
        elif key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
            self.player_x += 5

        return(self.player_x)
