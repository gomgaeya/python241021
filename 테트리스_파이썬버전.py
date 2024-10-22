import pygame
import random

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255),
    (255, 255, 0),
    (128, 0, 128),
    (0, 255, 0),
    (255, 0, 0),
    (0, 0, 255),
    (255, 127, 0)
]

# 게임 설정
BLOCK_SIZE = 30
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
SCREEN_WIDTH = BOARD_WIDTH * BLOCK_SIZE
SCREEN_HEIGHT = BOARD_HEIGHT * BLOCK_SIZE

# 테트로미노 모양
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]]
]

class Tetromino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = BOARD_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = list(zip(*self.shape[::-1]))

class TetrisGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("테트리스")
        self.clock = pygame.time.Clock()
        self.board = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.current_piece = Tetromino()
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def draw_board(self):
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, cell, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(self.screen, WHITE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

    def draw_current_piece(self):
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, self.current_piece.color,
                                     ((self.current_piece.x + x) * BLOCK_SIZE,
                                      (self.current_piece.y + y) * BLOCK_SIZE,
                                      BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(self.screen, WHITE,
                                     ((self.current_piece.x + x) * BLOCK_SIZE,
                                      (self.current_piece.y + y) * BLOCK_SIZE,
                                      BLOCK_SIZE, BLOCK_SIZE), 1)

    def check_collision(self, dx=0, dy=0):
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = self.current_piece.x + x + dx
                    new_y = self.current_piece.y + y + dy
                    if new_x < 0 or new_x >= BOARD_WIDTH or new_y >= BOARD_HEIGHT or (new_y >= 0 and self.board[new_y][new_x]):
                        return True
        return False

    def merge_piece(self):
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.board[self.current_piece.y + y][self.current_piece.x + x] = self.current_piece.color

    def remove_full_rows(self):
        full_rows = [i for i, row in enumerate(self.board) if all(row)]
        for row in full_rows:
            del self.board[row]
            self.board.insert(0, [0 for _ in range(BOARD_WIDTH)])
        self.score += len(full_rows) ** 2 * 100

    def game_over(self):
        return any(self.board[0])

    def run(self):
        fall_time = 0
        fall_speed = 0.5
        running = True

        while running:
            fall_time += self.clock.get_rawtime()
            self.clock.tick()

            if fall_time / 1000 > fall_speed:
                if not self.check_collision(dy=1):
                    self.current_piece.y += 1
                else:
                    self.merge_piece()
                    self.remove_full_rows()
                    self.current_piece = Tetromino()
                    if self.check_collision():
                        running = False
                fall_time = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and not self.check_collision(dx=-1):
                        self.current_piece.x -= 1
                    if event.key == pygame.K_RIGHT and not self.check_collision(dx=1):
                        self.current_piece.x += 1
                    if event.key == pygame.K_DOWN and not self.check_collision(dy=1):
                        self.current_piece.y += 1
                    if event.key == pygame.K_UP:
                        rotated = list(zip(*self.current_piece.shape[::-1]))
                        if not self.check_collision():
                            self.current_piece.shape = rotated

            self.screen.fill(BLACK)
            self.draw_board()
            self.draw_current_piece()
            score_text = self.font.render(f"점수: {self.score}", True, WHITE)
            self.screen.blit(score_text, (10, 10))
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game = TetrisGame()
    game.run()