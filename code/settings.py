import pygame

# game settings
COLUMNS = 10
ROWS = 20
BLOCK_SIZE = 40
GAME_WIDTH, GAME_HEIGHT = COLUMNS * BLOCK_SIZE, ROWS * BLOCK_SIZE

# sidebar settings
SIDEBAR_WIDTH = 200

# SIDEBAR_HEIGHT = GAME_HEIGHT
PREVIEW_HEIGHT_FRACTION = 0.7
SCORE_HEIGHT_FRACTION = 1 - PREVIEW_HEIGHT_FRACTION

# window settings
PADDING = 20
WINDOW_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH + PADDING * 3
WINDOW_HEIGHT = GAME_HEIGHT + PADDING * 2

# color settings
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
