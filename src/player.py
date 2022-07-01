import pygame


class player:

    def __init__(self, display, colour, x_axis, y_axis):
        self.display = display
        self.colour = colour
        self.x_axis = x_axis
        self.y_axis = y_axis

        ####################
        # player variables
        ####################
        self.player_size = 25
        self.player_x = x_axis / 100 * 50
        self.player_y = y_axis / 100 * 90

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

    def move_player(self, key_pressed):
        ####################
        # players movement
        ####################
        if self.player_x < 0:
            self.player_x = self.x_axis - self.player_size
        elif key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
            self.player_x -= 5
        elif self.player_x > self.x_axis - self.player_size:
            self.player_x = 25
        elif key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
            self.player_x += 5
