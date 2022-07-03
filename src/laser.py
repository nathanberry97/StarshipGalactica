import pygame


class laser:

    def __init__(self, screen, colour, y_axis):
        self.screen = screen
        self.colour = colour
        ####################
        # laser variables
        ####################
        self.laser = [[]]
        self.bullet_next_tick = 0
        self.bullet_interval = 200
        self.laser_y_axis = y_axis / 100 * 90
        self.laser_dimension = 5

    def create_laser(self, key_pressed, player_x_axis):
        laser_x_axis = player_x_axis + 10
        laser_y_axis = self.laser_y_axis
        ####################
        # add laser
        ####################
        tick = pygame.time.get_ticks()
        if key_pressed[pygame.K_LCTRL] or key_pressed[pygame.K_SPACE]:
            if tick > self.bullet_next_tick:
                self.bullet_next_tick = tick + self.bullet_interval
                self.laser.append(
                    [laser_x_axis,
                     laser_y_axis]
                )

    def move_laser(self):
        range_laser = len(self.laser)
        ####################
        # move laser
        ####################
        if range_laser > 1:
            index = 0
            for bullet in self.laser:
                # first array is emtpy, here to prevent an error
                if index != 0:
                    bullet_coorinates = [
                       bullet[0],
                       bullet[1],
                       self.laser_dimension,
                       self.laser_dimension
                    ]

                    pygame.draw.rect(
                        self.screen,
                        self.colour,
                        bullet_coorinates
                    )
                    # decreasing lasers x axis
                    bullet[1] -= 5
                    if bullet[1] <= 0:
                        self.laser.remove(self.laser[0])
                else:
                    index += 1
