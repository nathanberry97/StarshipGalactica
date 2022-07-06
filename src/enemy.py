import pygame


class enemy:

    def __init__(self, display, x_axis, y_axis):
        self.display = display
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.count = 60
        self.enemy_sprite = (
            pygame.image.load('assets/enemy.png').convert_alpha()
        )

    def create_enemy(self):
        enemy_coordinates = (self.x_axis, self.y_axis)
        self.display.blit(
            self.enemy_sprite, enemy_coordinates
        )

    def move_enemy(self, direction):
        if direction == 1:
            self.x_axis += 0.5
            self.count += 1

        elif direction == 0:
            self.x_axis -= 0.5
            self.count -= 1

        return(self.count)
