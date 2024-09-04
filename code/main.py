from settings import *
from sys import exit

class Main:
    def __init__(self):

        #general setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Tetris")

    def run(self):
        while True:

            # event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # display
            self.display_surface.fill(GRAY)

            # update game
            pygame.display.update()
            self.clock.tick()

if __name__ == "__main__":
    main = Main()
    main.run()