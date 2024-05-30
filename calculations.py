#calculations.py

def create_grid(size):
    grid = []
    for row in range(size):
        grid_row = []
        for col in range(size):
            if col == size - 1:  # Right edge nodes
                grid_row.append([-1, 0])
            elif row == size - 1:  # Bottom edge nodes
                grid_row.append([0, -1])
            else:
                grid_row.append([0, 0])
        grid.append(grid_row)
    grid[size - 1][size - 1] = [-1, -1]
    return grid

def initialise_grid(grid_size):
    return create_grid(grid_size)

def grid_changer(grid, move):
    if grid[move[0]][move[1]][move[2]] == 0:
        grid[move[0]][move[1]][move[2]] = 1
    return grid

def sequence_mover(grid, sequence):
    for move in sequence:
        grid = grid_changer(grid, move)
    return grid

def check_and_shade_square(grid, grid_size):
    shaded_squares = []
    for row in range(0, grid_size-1):
        for col in range(0, grid_size-1):
            if (grid[row][col][0] == 1 and
                grid[row][col][1] == 1 and
                grid[row+1][col][0] == 1 and
                grid[row][col+1][1] == 1):
                shaded_squares.append((row, col))
    return shaded_squares

def move_and_square_tracker(sequence, grid_size):
    player_list = []
    sqaure_list0 = []
    sqaure_list1 = []
    for i in range(0, len(sequence) + 1):
        if i == 0:
            player_list.append(0)
        else:
            if player_list[i-1] == 0:
                default_player = 1
            else:
                default_player = 0
            grid = initialise_grid(grid_size)
            squares0 = check_and_shade_square(sequence_mover(grid, sequence[0:i]), grid_size)
            squares1 = check_and_shade_square(sequence_mover(grid, sequence[0:i+1]), grid_size)
            new_squares = [x for x in squares1 if x not in squares0]
            if len(new_squares) > 0:
                default_player = player_list[i-1]
                if default_player == 0:
                    sqaure_list1 += new_squares
                else:
                    sqaure_list0 += new_squares
            player_list.append(default_player)
    grid = initialise_grid(grid_size)
    final_grid = sequence_mover(grid, sequence)
    return final_grid, sqaure_list0, sqaure_list1, player_list

def update_scores(sequence, player_scores, grid_size):
    _, sqaure_list0, sqaure_list1, _ = move_and_square_tracker(sequence, grid_size)
    player_scores[0] = len(sqaure_list0)
    player_scores[1] = len(sqaure_list1)



def check_game_over(player_scores, grid_size):
    total_squares = (grid_size - 1) ** 2
    if sum(player_scores) == total_squares:
        if player_scores[0] > player_scores[1]:
            return "Player 1 wins!"
        elif player_scores[1] > player_scores[0]:
            return "Player 2 wins!"
        else:
            return "It's a draw!"
    return None

def possible_moves(grid, grid_size):
    move_list=[]
    for row in range(grid_size):
        for col in range(grid_size):
            if grid[row][col][0]==0:
                move_list.append((row,col,0))
            if grid[row][col][1]==0:
                move_list.append((row,col,1))
    return move_list



def game_progression(sequence, grid_size):
    game_prog_list=[None]*len(sequence)
    for i in range(len(sequence)):
        # print(i)
        _, sqaure_list0_old, sqaure_list1_old, player_list = move_and_square_tracker(sequence[0:i], grid_size)
        turn=player_list[-1]
        _, sqaure_list0_new, sqaure_list1_new, _ = move_and_square_tracker(sequence[0:i+1], grid_size)
        game_prog_list[i]={'Move No.':i+1,
                           'turn':turn+1,
                           'Move':sequence[i],
                        #    'Player 1 Squares Before':len(sqaure_list0_old),
                           'Player 1 Squares After':len(sqaure_list0_new),
                           'Player 1 Gain':len(sqaure_list0_new)-len(sqaure_list0_old),
                        #    'Player 2 Squares Before':len(sqaure_list1_old),
                           'Player 2 Squares After':len(sqaure_list1_new),
                           'Player 2 Gain':len(sqaure_list1_new)-len(sqaure_list1_old)
                           }
    return game_prog_list


def print_game_progression(sequence, grid_size):
    game_progress=game_progression(sequence, grid_size)
    for idx, d in enumerate(game_progress, start=1):
        # print(f"Move {idx}:")
        for key, value in d.items():
            print(f"  {key}: {value}",end='|')
        print()  # Add an empty line between dictionaries