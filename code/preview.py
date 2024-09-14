from settings import *
from display_component import DisplayComponent

class Preview(DisplayComponent):
    def __init__(self):
        super().__init__(SIDEBAR_WIDTH, PREVIEW_HEIGHT_FRACTION * GAME_HEIGHT, {'topright': (WINDOW_WIDTH - PADDING, PADDING)})

    def run(self):
        super().run()