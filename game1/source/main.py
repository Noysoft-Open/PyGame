import pygame


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Game 1")
        self.win = pygame.display.set_mode((500, 500))
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
