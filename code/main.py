from settings import *
from sys import exit
import pygame

# components
from game import Game
from score import Score
from preview import Preview

from random import choice

class Main:
    def __init__(self):

        #general setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Tetris")

        # shapes
        self.next_shape = [choice(list(TETROMINOS.keys()))]
        print(self.next_shape)

        # components
        self.game = Game(self.get_next_shape)
        self.score = Score()
        self.preview = Preview()
    
    def get_next_shape(self):
        next_shape = self.next_shape  # Get the next shape
        self.next_shape = choice(list(TETROMINOS.keys()))  # Update to a new shape
        return next_shape

    def run(self):
        while True:

            # event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # display
            self.display_surface.fill(MID_DARK)

            # run components
            self.game.run()
            self.score.run()
            self.preview.run(self.next_shape)

            # update game
            pygame.display.update()
            self.clock.tick()

if __name__ == "__main__":
    main = Main()
    main.run()