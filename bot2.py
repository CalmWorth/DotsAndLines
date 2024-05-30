# bot2.py

import random
from calculations import possible_moves, initialise_grid, sequence_mover

def bot2_move(sequence, grid_size):
    grid = initialise_grid(grid_size)
    grid = sequence_mover(grid, sequence)
    moves = possible_moves(grid, grid_size)
    return random.choice(moves)
