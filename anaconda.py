import pygame

from Game import Game
from Config import Config


def loop(self):
    print('game loop')


def main():
    screen = pygame.display.set_mode(
        (Config['game']['width'], Config['game']['height']))
    pygame.display.set_caption(Config['game']['caption'])
    game = Game(screen)
    game.loop(screen)


if __name__ == "__main__":
    pygame.init()
    main()
