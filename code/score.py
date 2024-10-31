from settings import *
from display_component import DisplayComponent
from os.path import dirname, realpath, join
import pygame


class Score(DisplayComponent):
    def __init__(self):
        super().__init__(SIDEBAR_WIDTH, SCORE_HEIGHT_FRACTION * GAME_HEIGHT - PADDING, {'bottomright': (WINDOW_WIDTH - PADDING, WINDOW_HEIGHT - PADDING)})

        
        # font
        if not pygame.font.get_init():
            pygame.font.init()
        
        base_path = dirname(realpath(__file__))  # current file's directory
        font_path = join(base_path, '..', 'graphics', 'Russo_One.ttf')  # sibling directory 'graphics'
        self.font = pygame.font.Font(font_path, 30)

		# increment
        self.increment_height = self.surface.get_height() / 3

		# data 
        self.score = 0
        self.level = 1
        self.lines = 0

    def display_text(self, pos, text):
        text_surface = self.font.render(f'{text[0]}: {text[1]}', True, MID_DARK)
        text_rect = text_surface.get_rect(center = pos)
        self.surface.blit(text_surface, text_rect)
            
    def run(self):
        super().run()

        self.surface.fill(LIGHT)
        for i, text in enumerate([('Score',self.score), ('Level', self.level), ('Lines', self.lines)]):
            x = self.surface.get_width() / 2
            y = self.increment_height / 2 + i * self.increment_height
            self.display_text((x,y), text)

        self.display_surface.blit(self.surface,self.rect)
        pygame.draw.rect(self.display_surface, MID_LIGHT, self.rect, 2, 2)