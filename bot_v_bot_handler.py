# bot_v_bot_handler.py
from bot1 import bot1_move
from bot2 import bot2_move
from draw_grid import draw_grid
from calculations import update_scores, check_game_over, move_and_square_tracker,print_game_progression
from event_handler import game_over_actions
import time
from tkinter import messagebox





def bot_vs_bot_handler(canvas, root, grid_size, sequence, player_scores):


    def make_move():
        current_player = move_and_square_tracker(sequence, grid_size)[3][-1]
        # print(current_player)

        if current_player == 0:
            move = bot1_move(sequence, grid_size)
        else:
            move = bot2_move(sequence, grid_size)

        sequence.append(move)
        update_scores(sequence, player_scores, grid_size)
        draw_grid(canvas, sequence, player_scores, grid_size)

        game_over_message = check_game_over(player_scores, grid_size)
        if game_over_message:
            game_over_actions(sequence, grid_size,canvas,game_over_message,root)
        else:
            root.after(500, make_move)  # Schedule the next move

    # Start the loop by scheduling the first move
    root.after(500, make_move)



def run_simulation(grid_size, num_games):
    bot1_wins = 0
    bot2_wins = 0
    draws = 0
    start_time = time.time()

    for game in range(num_games):
        sequence = []
        player_scores = [0, 0]
        current_player = game % 2  # Alternating starting player

        while True:
            if current_player == 0:
                move = bot1_move(sequence, grid_size)
            else:
                move = bot2_move(sequence, grid_size)

            sequence.append(move)
            update_scores(sequence, player_scores, grid_size)
            current_player = move_and_square_tracker(sequence, grid_size)[3][-1]

            game_over_message = check_game_over(player_scores, grid_size)
            if game_over_message:
                if "Player 1" in game_over_message:
                    bot1_wins += 1
                elif "Player 2" in game_over_message:
                    bot2_wins += 1
                else:
                    draws += 1
                break

        # Print progress
        # print(f"Progress: {game + 1}/{num_games} games completed", end='\r')
        # print('-|',end='')
        time.sleep(0.01)  # To ensure the print statement updates correctly

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("\nSimulation results:")
    print(f"Bot 1 wins: {bot1_wins}")
    print(f"Bot 2 wins: {bot2_wins}")
    print(f"Draws: {draws}")
    print(f"Time elapsed: {elapsed_time:.2f} seconds")

