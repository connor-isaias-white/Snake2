import random
import pygame

from Config import Config


class Apple:
    def __init__(self, display):
        self.x_pos = 0
        self.y_pos = 0

        self.display = display

        self.randomize()

    def randomize(self):
        height = Config['game']['height']
        width = Config['game']['width']
        bumper = Config['game']['bumper_size']

        max_x = (height - bumper - Config['snake']['width'])
        max_y = (height - bumper - Config['snake']['height'])

        self.x_pos = random.randint(bumper, max_x)
        self.x_pos -= self.x_pos % 20
        self.y_pos = random.randint(bumper, max_y)
        self.y_pos -= self.y_pos % 20

    def draw(self):
        return pygame.draw.rect(
            self.display,
            Config['colors']['red'],
            [
                self.x_pos,
                self.y_pos,
                Config['apple']['height'],
                Config['apple']['width']
            ]
        )

    def remove(self):
        pygame.draw.rect(
            self.display,
            Config['colors']['black'],
            [
                self.x_pos,
                self.y_pos,
                Config['apple']['height'],
                Config['apple']['width']
            ]
        )
