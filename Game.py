import pygame
from Config import Config
from Snake import Snake
from Apple import Apple
from ai import Ai


class Game:

    def __init__(self, screen):
        self.display = screen
        self.player1score = 0
        self.player2score = 0
        self.map(screen)

    def map(self, screen):
        screen.fill(Config["colors"]["gray"])
        pygame.draw.rect(
            self.display,
            Config['colors']['black'],
            [
                Config['game']['bumper_size'],
                Config['game']['bumper_size'],
                Config['game']['width'] - 2*Config['game']['bumper_size'],
                Config['game']['height'] - 2*Config['game']['bumper_size']
            ])
        font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = font.render(f"Green: {self.player2score}", True,
                                Config['colors']['green'], Config['colors']['gray'])
        self.text2 = font.render(f"Blue: {self.player1score}", True,
                                 Config['colors']['blue'], Config['colors']['gray'])
        self.textRect = self.text.get_rect()
        self.textRect.center = (
            Config['game']['bumper_size']*2.5, Config['game']['bumper_size'] // 2)
        self.textRect2 = self.text.get_rect()
        self.textRect2.center = (
            Config['game']['width']-Config['game']['bumper_size']*2.5, Config['game']['bumper_size'] // 2)

    def loop(self, screen):
        screen.blit(self.text, self.textRect)
        screen.blit(self.text2, self.textRect2)
        clock = pygame.time.Clock()
        self.snake = Snake(self.display, -(Config['snake']['width']))
        self.snake2 = Snake(self.display, (Config['snake']['width']))
        apple = Apple(self.display)
        ai = Ai()
        x_change = Config['snake']['speed']
        y_change = 0
        x_change2 = -Config['snake']['speed']
        y_change2 = 0

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and x_change == 0:
                        x_change = -Config['snake']['speed']
                        y_change = 0
                    elif event.key == pygame.K_RIGHT and x_change == 0:
                        x_change = Config['snake']['speed']
                        y_change = 0
                    elif event.key == pygame.K_UP and y_change == 0:
                        x_change = 0
                        y_change = -Config['snake']['speed']
                    elif event.key == pygame.K_DOWN and y_change == 0:
                        x_change = 0
                        y_change = Config['snake']['speed']

                    if event.key == pygame.K_a and x_change2 == 0:
                        x_change2 = -Config['snake']['speed']
                        y_change2 = 0
                    elif event.key == pygame.K_d and x_change2 == 0:
                        x_change2 = Config['snake']['speed']
                        y_change2 = 0
                    elif event.key == pygame.K_w and y_change2 == 0:
                        x_change2 = 0
                        y_change2 = -Config['snake']['speed']
                    elif event.key == pygame.K_s and y_change2 == 0:
                        x_change2 = 0
                        y_change2 = Config['snake']['speed']

            snake_rect = self.snake.draw(Config['colors']['blue'])
            snake_rect2 = self.snake2.draw(Config['colors']['green'])

            apple_rect = apple.draw()
            ai.update(pos=(snake_rect[0], snake_rect[1]),  apple=(apple_rect[0], apple_rect[1]),
                      size=self.snake.max_size)
            move = ai.action()

            bumper_x = Config['game']['width'] - Config['game']['bumper_size']
            bumper_y = Config['game']['height'] - Config['game']['bumper_size']

            if apple_rect.colliderect(snake_rect):
                apple.remove()
                apple.randomize()
                self.snake.eat()
            elif apple_rect.colliderect(snake_rect2):
                apple.remove()
                apple.randomize()
                self.snake2.eat()

            snakehit = self.snake.hit(self.snake2.body, bumper_x, bumper_y)
            snakehit2 = self.snake2.hit(self.snake.body, bumper_x, bumper_y)

            if (snakehit or snakehit2):
                if (snakehit and snakehit2):
                    print("Tie")
                elif snakehit:
                    self.snake2.score += 1
                    self.player2score += 1
                else:
                    self.snake.score += 1
                    self.player1score += 1
                apple.remove()
                # snake.remove()
                self.map(screen)
                self.loop(screen)
            self.snake.move(x_change, y_change)
            self.snake2.move(x_change2, y_change2)
            pygame.display.update()
            clock.tick(Config['game']['fps'])
