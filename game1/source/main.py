import pygame


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Game 1")
        self.win = pygame.display.set_mode((500, 500))
        self.running = True
        self.x_pos = 0
        self.y_pos = 0
        self.rec_width = 0
        self.rec_height = 0
        self.velocity = 0

    def character(self):
        self.x_pos = 50
        self.y_pos = 50
        self.rec_width = 40
        self.rec_height = 60
        self.velocity = 10

    def setvar(self):
        self.character()

    def keyevents(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_pos -= self.velocity

        if keys[pygame.K_RIGHT]:
            self.x_pos += self.velocity

        if keys[pygame.K_UP]:
            self.y_pos -= self.velocity

        if keys[pygame.K_DOWN]:
            self.y_pos += self.velocity

    def draw(self):
        self.win.fill((0, 0, 0))
        pygame.draw.rect(
            self.win,
            (255, 0, 0),
            (
                self.x_pos,
                self.y_pos,
                self.rec_width,
                self.rec_height
            )
        )
        pygame.display.update()

    def mainloop(self):
        while self.running:
            pygame.time.delay(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.keyevents()
            self.draw()

    def run(self):
        self.setvar()
        self.mainloop()
        self.close()

    def close(self):
        pygame.quit()
