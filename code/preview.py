from settings import *
from display_component import DisplayComponent
from pygame.image import load
from os import path

class Preview(DisplayComponent):
    def __init__(self, next_shape):
        super().__init__(SIDEBAR_WIDTH, PREVIEW_HEIGHT_FRACTION * GAME_HEIGHT, {'topright': (WINDOW_WIDTH - PADDING, PADDING)})

    # shapes
        self.next_shape = next_shape
        self.shape_surfaces = {shape: load(path.join('..','graphics',f'{shape}.png')).convert_alpha() for shape in TETROMINOS.keys()}
        print(self.shape_surfaces)

    def run(self):
        super().run()