import pygame
import math
from Config import Config


class Snake:

    def __init__(self, display, left):
        self.x_pos = Config['game']['width'] / 2 - left
        self.y_pos = Config['game']['height'] / 2
        self.display = display
        self.body = []
        self.max_size = 3
        self.score = 0

    def eat(self):
        self.max_size += 4

    def draw(self, color):

        self.body.append(pygame.draw.rect(
            self.display,
            color,
            [
                self.x_pos,
                self.y_pos,
                Config['snake']['height'],
                Config['snake']['width']
            ]
        ))
        if len(self.body) > self.max_size:
            self.body[0][0]
            pygame.draw.rect(
                self.display,
                Config['colors']['black'],
                [
                    self.body[0][0],
                    self.body[0][1],
                    Config['snake']['height'],
                    Config['snake']['width']
                ]
            )
            self.body.remove(self.body[0])
        return self.body[-1]

    def move(self, x_change, y_change):
        self.body
        self.x_pos += x_change
        self.y_pos += y_change

    def remove(self):
        for i in self.body:
            pygame.draw.rect(
                self.display,
                Config['colors']['black'],
                [
                    i[0],
                    i[1],
                    Config['snake']['height'],
                    Config['snake']['width']
                ]
            )

    def hit(self, othersnake, bumper_x, bumper_y):
        if self.x_pos < Config['game']['bumper_size'] or self.y_pos < Config['game']['bumper_size'] or self.x_pos + Config['snake']['width'] > bumper_x or self.y_pos + Config['snake']['height'] > bumper_y:
            return True
        for i in self.body[:-1]:
            if (self.body[-1][0], self.body[-1][1]) == (i[0], i[1]):
                return True
        for i in othersnake[:-1]:
            # if (self.body[-1][0], self.body[-1][1]) == (i[0], i[1]):
            if abs(self.body[-1][0] - i[0]) <= 10 and abs(self.body[-1][1] - i[1]) <= 10:
                return True
        return False
