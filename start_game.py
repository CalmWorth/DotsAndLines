#start_game.py

import tkinter as tk
from draw_grid import draw_grid
from event_handler import click_handler
from bot_v_bot_handler import bot_vs_bot_handler



def start_game(grid_size, game_mode):
    player_scores = [0, 0]
    sequence = []

    def print_moves():
        print("Sequence of moves:", sequence)

    def create_window():
        root = tk.Tk()
        root.title("Grid Links Visualization")
        canvas = tk.Canvas(root, width=200+grid_size*50, height=200+grid_size*50)
        # canvas.pack(expand=True, fill=tk.BOTH)
        canvas.pack()
        draw_grid(canvas, sequence, player_scores, grid_size)

        if game_mode == '1':
            canvas.bind("<Button-1>", lambda event: click_handler(event, canvas, root, grid_size, sequence, player_scores, vs_bot=False))
        elif game_mode == '2':
            canvas.bind("<Button-1>", lambda event: click_handler(event, canvas, root, grid_size, sequence, player_scores, vs_bot=True))
        elif game_mode == '3':
            root.after(1000, lambda: bot_vs_bot_handler(canvas, root, grid_size, sequence, player_scores))

        print_button = tk.Button(root, text="Print Moves", command=print_moves)
        print_button.pack()
        root.mainloop()

    create_window()
