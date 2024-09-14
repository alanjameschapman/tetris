import pygame

class DisplayComponent:
    def __init__(self, width, height, position):
        self.display_surface = pygame.display.get_surface()
        self.surface = pygame.Surface((width, height))
        self.rect = self.surface.get_rect(**position)

    def run(self):
        self.display_surface.blit(self.surface, self.rect)