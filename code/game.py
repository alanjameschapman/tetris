from settings import *
from display_component import DisplayComponent
from random import choice
from sys import exit
from timer import Timer
from os.path import join, dirname, realpath


class Game(DisplayComponent):
    def __init__(self, get_next_shape, update_score):
        # general
        super().__init__(GAME_WIDTH, GAME_HEIGHT, {'topleft': (PADDING, PADDING)})

        # lines
        self.line_surface = self.surface.copy()
        self.line_surface.fill((0,255,0))
        self.line_surface.set_colorkey((0,255,0))
        self.line_surface.set_alpha(100)

        # game connection
        self.get_next_shape = get_next_shape
        self.update_score = update_score

        # tetromino
        self.field_data = [[0 for x in range(COLUMNS)] for y in range(ROWS)]

        self.tetromino = Tetromino(
            choice(list(TETROMINOS.keys())),
            self.sprites,
            self.create_new_tetromino,
            self.field_data)

        # timer
        self.down_speed = UPDATE_START_SPEED
        self.down_speed_faster = self.down_speed * 0.3
        self.down_pressed = False
        self.timers = {
            'vertical move': Timer(self.down_speed, repeated=True, func=self.move_down),
            'horizontal move': Timer(MOVE_WAIT_TIME),
            'rotate': Timer(ROTATE_WAIT_TIME)
        }
        self.timers['vertical move'].activate()

        # score
        self.current_level = 1
        self.current_score = 0
        self.current_lines = 0

        # audio
        base_path = dirname(realpath(__file__))
        self.landing_sound = pygame.mixer.Sound(join(base_path, '..', 'sound', 'landing.wav'))
        self.landing_sound.set_volume(0.2)

    def draw_grid(self):

        for col in range(1, COLUMNS):
            x = col * CELL_SIZE
            pygame.draw.line(self.surface, MID_DARK, (x, 0), (x, self.surface.get_height()), 1)

        for row in range(1, ROWS):
            y = row * CELL_SIZE
            pygame.draw.line(self.surface, MID_DARK, (0, y), (self.surface.get_width(), y), 1)

        self.surface.blit(self.line_surface, (0, 0))

    def calculate_score(self, num_lines):
        self.current_lines += num_lines
        self.current_score += SCORE_DATA[num_lines] * self.current_level

        if self.current_lines / 10 > self.current_level:
            self.current_level += 1
            self.down_speed *= 0.7
            self.down_speed_faster = self.down_speed * 0.3
            self.timers['vertical move'].duration = self.down_speed
        self.update_score(self.current_lines, self.current_score, self.current_level)

    def check_game_over(self):
        for block in self.tetromino.blocks:
            if block.pos.y < 0:
                exit()

    def create_new_tetromino(self):
        self.landing_sound.play()
        self.check_game_over()
        self.check_lines()
        self.tetromino = Tetromino(
            self.get_next_shape(),
            self.sprites,
            self.create_new_tetromino,
            self.field_data)
        
    def timer_update(self):
        for timer in self.timers.values():
            timer.update()

    def move_down(self):
        self.tetromino.move_down()

    def input(self):
        keys = pygame.key.get_pressed()

        # check horizontal movement
        if not self.timers['horizontal move'].active:
            if keys[pygame.K_LEFT]:
                self.tetromino.move_horizontal(-1)
                self.timers['horizontal move'].activate()
            if keys[pygame.K_RIGHT]:
                self.tetromino.move_horizontal(1)
                self.timers['horizontal move'].activate()
            # if keys[pygame.K_DOWN]:
            #     self.tetromino.move_down()

        # check for rotation
        if not self.timers['rotate'].active:
            if keys[pygame.K_UP]:
                self.tetromino.rotate()
                self.timers['rotate'].activate()

        # check for faster vertical movement
        if not self.down_pressed and keys[pygame.K_DOWN]:
            self.down_pressed = True
            self.timers['vertical move'].duration = self.down_speed_faster

        if self.down_pressed and not keys[pygame.K_DOWN]:
            self.down_pressed = False
            self.timers['vertical move'].duration = self.down_speed

    def check_lines(self):

        # get full row indexes
        delete_rows = []
        for i, row in enumerate(self.field_data):
            if all(row):
                delete_rows.append(i)
        
        if delete_rows:
            for delete_row in delete_rows:
                # delete full rows
                for block in self.field_data[delete_row]:
                    block.kill()

                # move rows down
                for row in self.field_data:
                    for block in row:
                        if block and block.pos.y < delete_row:
                            block.pos.y += 1

            # rebuild field data
            self.field_data = [[0 for x in range(COLUMNS)] for y in range(ROWS)]
            for block in self.sprites:
                self.field_data[int(block.pos.y)][int(block.pos.x)] = block

            # update score
            self.calculate_score(len(delete_rows))

    def run(self):

        # update
        self.input()
        self.timer_update()
        self.sprites.update()

        # drawing
        self.surface.fill(LIGHT)
        self.draw_grid()
        pygame.draw.rect(self.surface, MID_LIGHT, self.surface.get_rect(), 2, 2)
        self.sprites.draw(self.surface)

        super().run()

# pygame.sprite.Sprite - was arg in Tetromino class below. Seems to work without it.
class Tetromino():
    def __init__(self, shape, group, create_new_tetromino, field_data):

        # setup
        self.shape = shape
        self.block_positions = TETROMINOS[shape]['shape']
        self.color = TETROMINOS[shape]['color']
        self.create_new_tetromino = create_new_tetromino
        self.field_data = field_data

        # create blocks
        self.blocks = [Block(group,pos,self.color) for pos in self.block_positions]

    # collision detection
    def next_move_horizontal_collide(self, blocks, amount):
        collision_list = [block.horizontal_collide(int(block.pos.x + amount), self.field_data) for block in self.blocks]
        return True if any(collision_list) else False
    
    def next_move_vertical_collide(self, blocks, amount):
        collision_list = [block.vertical_collide(int(block.pos.y + amount), self.field_data) for block in self.blocks]
        return True if any(collision_list) else False

    # movement
    def move_horizontal(self, amount):
        if not self.next_move_horizontal_collide(self.blocks, amount):
            for block in self.blocks:
                block.pos.x += amount

    def move_down(self):
        if not self.next_move_vertical_collide(self.blocks, 1):
            for block in self.blocks:
                block.pos.y += 1
        else:
            for block in self.blocks:
                self.field_data[int(block.pos.y)][int(block.pos.x)] = block
            self.create_new_tetromino()

    # rotation
    def rotate(self):
        if self.shape != 'O':
            
            # fulcrum
            fulcrum = self.blocks[0].pos

            # calculate new positions
            new_positions = [block.rotate(fulcrum) for block in self.blocks]

            # check for collisions
            for pos in new_positions:
                
                # horizontal
                if pos.x < 0 or pos.x >= COLUMNS:
                    return

                # vertical / bottom
                if pos.y >= ROWS:
                    return

                # field i.e. with other blocks
                if self.field_data[int(pos.y)][int(pos.x)]:
                    return
            
            # implement new positions
            for i, block in enumerate(self.blocks):
                block.pos = new_positions[i]

class Block(pygame.sprite.Sprite):
    def __init__(self, group, pos, color):
        # general
        super().__init__(group)
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(color)

        # position
        self.pos = pygame.Vector2(pos) + BLOCK_OFFSET
        self.rect = self.image.get_rect(topleft = self.pos * CELL_SIZE)

    def rotate(self, fulcrum):
        return fulcrum + (self.pos - fulcrum).rotate(90)

    def horizontal_collide(self, x, field_data):
        if not 0 <= x < COLUMNS:
            return True
        if field_data[int(self.pos.y)][x]:
            return True
        
    def vertical_collide(self, y, field_data):
        if y >= ROWS:
            return True
        
        if y >=0 and field_data[y][int(self.pos.x)]:
            return True
    
    def update(self):
        self.rect.topleft = self.pos * CELL_SIZE
