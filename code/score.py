from settings import *
from display_component import DisplayComponent

class Score(DisplayComponent):
    def __init__(self):
        super().__init__(SIDEBAR_WIDTH, SCORE_HEIGHT_FRACTION * GAME_HEIGHT - PADDING, {'bottomright': (WINDOW_WIDTH - PADDING, WINDOW_HEIGHT - PADDING)})

    def run(self):
        super().run()