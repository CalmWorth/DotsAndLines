# event_handler.py

import tkinter as tk
from calculations import update_scores, check_game_over, move_and_square_tracker,print_game_progression
from draw_grid import draw_grid
from bot1 import bot1_move
from tkinter import messagebox

# event_handler.py

def click_handler(event, canvas, root, grid_size, sequence, player_scores, vs_bot):
    cell_size = 40
    canvas_width = canvas.winfo_reqwidth()
    canvas_height = canvas.winfo_reqheight()
    center_x = canvas_width // 2
    center_y = canvas_height // 2
    grid_start_x = center_x - (cell_size * grid_size // 2)
    grid_start_y = center_y - (cell_size * grid_size // 2)

    x_click = event.x
    y_click = event.y

    for row in range(grid_size):
        for col in range(grid_size):
            x1 = grid_start_x + col * cell_size
            y1 = grid_start_y + row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            if x1 <= x_click <= x2 and y1 - 5 <= y_click <= y1 + 5:  # Horizontal line
                move = (row, col, 0)
                if move not in sequence:
                    sequence.append(move)
                    current_player = move_and_square_tracker(sequence, grid_size)[3][-1]
                    update_scores(sequence, player_scores, grid_size)
                    draw_grid(canvas, sequence, player_scores, grid_size)
                    game_over_message = check_game_over(player_scores, grid_size)
                    if game_over_message:
                        game_over_actions(sequence, grid_size, canvas, game_over_message, root)
                    elif vs_bot and (current_player == 1):
                        root.after(500, lambda: bot_turn_handler(canvas, root, grid_size, sequence, player_scores))
                    return

            if x1 - 5 <= x_click <= x1 + 5 and y1 <= y_click <= y2:  # Vertical line
                move = (row, col, 1)
                if move not in sequence:
                    sequence.append(move)
                    current_player = move_and_square_tracker(sequence, grid_size)[3][-1]
                    update_scores(sequence, player_scores, grid_size)
                    draw_grid(canvas, sequence, player_scores, grid_size)
                    game_over_message = check_game_over(player_scores, grid_size)
                    if game_over_message:
                        game_over_actions(sequence, grid_size, canvas, game_over_message, root)
                    elif vs_bot and (current_player == 1):
                        root.after(500, lambda: bot_turn_handler(canvas, root, grid_size, sequence, player_scores))
                    return


def bot_turn_handler(canvas, root, grid_size, sequence, player_scores):
    move = bot1_move(sequence, grid_size)
    sequence.append(move)
    current_player = move_and_square_tracker(sequence, grid_size)[3][-1]
    new_scores = player_scores.copy()
    update_scores(sequence, new_scores, grid_size)
    draw_grid(canvas, sequence, new_scores, grid_size)
    game_over_message = check_game_over(new_scores, grid_size)
    if game_over_message:
        game_over_actions(sequence, grid_size,canvas,game_over_message,root)
    elif current_player == 1:  # Bot gets another turn if it completes a square
        root.after(500, lambda: bot_turn_handler(canvas, root, grid_size, sequence, new_scores))

def game_over_actions(sequence, grid_size,canvas,game_over_message,root):
    canvas_width = canvas.winfo_reqwidth()
    canvas_height = canvas.winfo_reqheight()
    
    # Calculate the center coordinates of the canvas
    center_x = canvas_width // 2
    center_y = canvas_height // 2
    
    print_game_progression(sequence, grid_size)
    canvas.create_text(center_x, canvas_height - 60, text=game_over_message, font=("Helvetica", 16), fill="green")
    root.after(100, lambda: messagebox.showinfo("Game Over", game_over_message))


