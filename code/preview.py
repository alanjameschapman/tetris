from settings import *
from display_component import DisplayComponent
from pygame.image import load
from os import path

class Preview(DisplayComponent):
    def __init__(self):
        super().__init__(SIDEBAR_WIDTH, PREVIEW_HEIGHT_FRACTION * GAME_HEIGHT, {'topright': (WINDOW_WIDTH - PADDING, PADDING)})

        # shapes
        graphics_path = path.join(path.dirname(__file__), '..', 'graphics')
        self.shape_surfaces = {shape: load(path.join(graphics_path, f'{shape}.bmp')).convert_alpha() for shape in TETROMINOS.keys()}

    def display_piece(self, shape):
        shape_surface = self.shape_surfaces[shape]
        self.surface.blit(shape_surface, shape_surface.get_rect(center=self.surface.get_rect().center))
    
    def run(self, next_shape):
        self.surface.fill(LIGHT)
        self.display_piece(next_shape)
        super().run()
        pygame.draw.rect(self.display_surface, MID_LIGHT, self.rect, 2, 2)