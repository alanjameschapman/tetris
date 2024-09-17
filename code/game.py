from settings import *
from display_component import DisplayComponent
from random import choice

class Game(DisplayComponent):
    def __init__(self):
        # general
        super().__init__(GAME_WIDTH, GAME_HEIGHT, {'topleft': (PADDING, PADDING)})

        # tetromino
        self.tetromino = Tetromino(choice(list(TETROMINOS.keys())), self.sprites)

    def run(self):
        # drawing
        # self.surface.fill(LIGHT)
        self.sprites.draw(self.surface)

        # self.draw_grid()
        super().run()

class Tetromino(pygame.sprite.Sprite):
    def __init__(self, shape, group):

        # setup
        self.block_positions = TETROMINOS[shape]['shape']
        self.color = TETROMINOS[shape]['color']

        # create blocks
        self.blocks = [Block(group,pos,self.color) for pos in self.block_positions]

class Block(pygame.sprite.Sprite):
    def __init__(self, group, pos, color):
        # general
        super().__init__(group)
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(color)

        # position
        self.pos = pygame.Vector2(pos) + BLOCK_OFFSET
        x = self.pos.x * CELL_SIZE
        y = self.pos.y * CELL_SIZE
        self.rect = self.image.get_rect(topleft=(x, y))
