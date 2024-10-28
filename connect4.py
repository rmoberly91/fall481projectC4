import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 700, 600
ROWS, COLS = 6, 7
SQUARE_SIZE = 100
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect 4")

# Create the board
board = [[0 for _ in range(COLS)] for _ in range(ROWS)]


def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, BLUE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)

def drop_piece(row, col, piece):
    board[row][col] = piece

def is_valid_location(col):
    return board[0][col] == 0

def get_next_open_row(col):
    for r in range(ROWS):
        if board[r][col] == 0:
            return r

def winning_move(board, piece):
    # Check horizontal locations
    for c in range(COLS-3):
        for r in range(ROWS):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations
    for c in range(COLS):
        for r in range(ROWS-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(COLS-3):
        for r in range(ROWS-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(COLS-3):
        for r in range(3, ROWS):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def draw_piece(row, col, piece):
        pygame.draw.circle(screen, RED if piece == 1 else YELLOW, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)
