import pygame

# game settings
COLUMNS = 10
ROWS = 20
CELL_SIZE = 40
GAME_WIDTH, GAME_HEIGHT = COLUMNS * CELL_SIZE, ROWS * CELL_SIZE

# sidebar settings
SIDEBAR_WIDTH = 200

# SIDEBAR_HEIGHT = GAME_HEIGHT
PREVIEW_HEIGHT_FRACTION = 0.5
SCORE_HEIGHT_FRACTION = 1 - PREVIEW_HEIGHT_FRACTION

# window settings
PADDING = 20
WINDOW_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH + PADDING * 3
WINDOW_HEIGHT = GAME_HEIGHT + PADDING * 2

# game behaviour 
UPDATE_START_SPEED = 200 
MOVE_WAIT_TIME = 200
ROTATE_WAIT_TIME = 200
BLOCK_OFFSET = pygame.Vector2(COLUMNS // 2, -1)

# gameboy display palette
LIGHT = (176, 191, 142)
MID_LIGHT = (105, 133, 40)
MID_DARK = (53, 70, 16)
DARK = (10, 13, 3)

# gameboy tetromino palette
TET_T = (128, 64, 128) # Muted Purple
TET_O = (200, 168, 0) # Faded Yellow
TET_J = (72, 88, 128) # Slate Blue-Grey
TET_L = (168, 104, 32) # Dusty Orange
TET_I = (88, 176, 160) # Soft Cyan-Green
TET_S = (96, 120, 72) # Muted Green
TET_Z = (128, 64, 48) # Brick Red

# tetromino settings
TETROMINOS = {
    'T': {'shape': [(0,0), (-1,0), (1,0), (0,-1)], 'color': TET_T},
    'O': {'shape': [(0,0), (0,-1), (1,0), (1,-1)], 'color': TET_O},
    'J': {'shape': [(0,0), (0,-1), (0,1), (-1,1)], 'color': TET_J},
    'L': {'shape': [(0,0), (0,-1), (0,1), (1,1)], 'color': TET_L},
    'I': {'shape': [(0,0), (0,-1), (0,-2), (0,1)], 'color': TET_I},
    'S': {'shape': [(0,0), (-1,0), (0,-1), (1,-1)], 'color': TET_S},
    'Z': {'shape': [(0,0), (1,0), (0,-1), (-1,-1)], 'color': TET_Z}
}

SCORE_DATA = {1: 40, 2: 100, 3: 300, 4: 1200}