from settings import *

class Preview:
    def __init__(self):
        self.surface = pygame.Surface((SIDEBAR_WIDTH, PREVIEW_HEIGHT_FRACTION * GAME_HEIGHT))
        self.rect = self.surface.get_rect(topright=(WINDOW_WIDTH - PADDING, PADDING))
        self.display_surface = pygame.display.get_surface()

    def run(self):
        self.display_surface.blit(self.surface, self.rect)