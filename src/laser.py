import pygame


class laser:

    def __init__(self, display, y_axis):
        self.display = display

        ####################
        # laser variables
        ####################
        self.laser_sprite = (
            pygame.image.load('assets/laser.png').convert_alpha()
        )
        self.laser = []

        self.bullet_next_tick = 0
        self.bullet_interval = 800
        self.laser_y_axis = y_axis / 100 * 82.5

    def create_laser(self, key_pressed, player_x_axis):
        laser_x_axis = player_x_axis + 25
        laser_coordinates = [laser_x_axis, self.laser_y_axis]
        ####################
        # add laser
        ####################
        tick = pygame.time.get_ticks()

        if (
            key_pressed[pygame.K_UP] and
            tick > self.bullet_next_tick or
            key_pressed[pygame.K_SPACE] and
            tick > self.bullet_next_tick
        ):

            self.bullet_next_tick = tick + self.bullet_interval
            self.laser.append(
                laser_coordinates
            )

    def move_laser(self):
        ####################
        # move laser
        ####################
        range_laser = len(self.laser)

        if range_laser > 0:
            for bullet in self.laser:
                self.display.blit(
                    self.laser_sprite, (bullet[0], bullet[1])
                )
                # decreasing lasers x axis
                bullet[1] -= 5
                if bullet[1] <= 0:
                    self.remove_laser(0)

        # return laser coordinates
        return(self.laser)

    def remove_laser(self, laser_index):
        self.laser.remove(
            self.laser[laser_index]
        )
