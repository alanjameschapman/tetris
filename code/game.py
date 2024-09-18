from settings import *
from display_component import DisplayComponent
from random import choice
from timer import Timer

class Game(DisplayComponent):
    def __init__(self):
        # general
        super().__init__(GAME_WIDTH, GAME_HEIGHT, {'topleft': (PADDING, PADDING)})

        # tetromino
        self.tetromino = Tetromino(choice(list(TETROMINOS.keys())), self.sprites)

        # timer
        self.timers = {
            'vertical move': Timer(UPDATE_START_SPEED, repeated=True, func=self.move_down)
        }
        self.timers['vertical move'].activate()

    def timer_update(self):
        for timer in self.timers.values():
            timer.update()

    def move_down(self):
        self.tetromino.move_down()

    def run(self):

        # update
        self.timer_update()
        self.sprites.update()

        # drawing
        self.surface.fill(LIGHT)
        self.sprites.draw(self.surface)

        super().run()

class Tetromino(pygame.sprite.Sprite):
    def __init__(self, shape, group):

        # setup
        self.block_positions = TETROMINOS[shape]['shape']
        self.color = TETROMINOS[shape]['color']

        # create blocks
        self.blocks = [Block(group,pos,self.color) for pos in self.block_positions]

    def move_down(self):
        for block in self.blocks:
            block.pos.y += 1

class Block(pygame.sprite.Sprite):
    def __init__(self, group, pos, color):
        # general
        super().__init__(group)
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(color)

        # position
        self.pos = pygame.Vector2(pos) + BLOCK_OFFSET
        self.rect = self.image.get_rect(topleft = self.pos * CELL_SIZE)

    def update(self):
        self.rect.topleft = self.pos * CELL_SIZE
