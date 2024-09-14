from settings import *
from display_component import DisplayComponent

class Game(DisplayComponent):
    def __init__(self):
        super().__init__(GAME_WIDTH, GAME_HEIGHT, {'topleft': (PADDING, PADDING)})

    # def draw_grid(self):
    #     for x in range(0, GAME_WIDTH, TILE_SIZE):
    #         pygame.draw.line(self.surface, GRAY, (x, 0), (x, GAME_HEIGHT))
    #     for y in range(0, GAME_HEIGHT, TILE_SIZE):
    #         pygame.draw.line(self.surface, GRAY, (0, y), (GAME_WIDTH, y))

    def run(self):
        super().run()