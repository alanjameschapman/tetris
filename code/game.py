from settings import *
from display_component import DisplayComponent

class Game(DisplayComponent):
    def __init__(self):
        # general
        super().__init__(GAME_WIDTH, GAME_HEIGHT, {'topleft': (PADDING, PADDING)})

        # grid
        # self.grid_surface = self.surface.copy()
        # self.grid_surface.fill(DARK)
        # self.grid_surface.set_colorkey(DARK)
        # self.grid_surface.set_alpha(120)

    # def draw_grid(self):
    #     for col in range(1, COLUMNS):
    #         x = col * BLOCK_SIZE
    #         pygame.draw.line(self.grid_surface, GRAY, (x, 0), (x, self.surface.get_height()), 1)

    #     for row in range(1, ROWS):
    #         y = row * BLOCK_SIZE
    #         pygame.draw.line(self.grid_surface, GRAY, (0, y), (self.surface.get_width(), y), 1)

    #     self.surface.blit(self.grid_surface, (0, 0))

    def run(self):
        # drawing
        # self.surface.fill(LIGHT)

        # self.draw_grid()
        super().run()