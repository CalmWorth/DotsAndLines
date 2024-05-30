# main.py

import tkinter as tk
import sys
from text_handler import TextHandler
from bot_v_bot_handler import run_simulation
from start_game import start_game
from tkinter.scrolledtext import ScrolledText

def main():
    # Setup the main window
    root = tk.Tk()
    root.title("Game Setup and Output")

    # Create the Text widget and redirect stdout and stderr
    text_area = ScrolledText(root, wrap=tk.WORD, width=145, height=30)
    text_area.pack(pady=10, padx=10)

    text_handler = TextHandler(text_area)
    sys.stdout = text_handler
    sys.stderr = text_handler

    # Setup input fields
    tk.Label(root, text="Enter grid size (even number has draws):").pack()
    grid_size_entry = tk.Entry(root)
    grid_size_entry.pack()

    tk.Label(root, text="Select game mode:").pack()
    game_mode_var = tk.StringVar(value='1')
    tk.Radiobutton(root, text="Human vs Human", variable=game_mode_var, value='1').pack()
    tk.Radiobutton(root, text="Human vs Bot", variable=game_mode_var, value='2').pack()
    tk.Radiobutton(root, text="Bot vs Bot", variable=game_mode_var, value='3').pack()
    tk.Radiobutton(root, text="Run Simulation (Bot vs Bot)", variable=game_mode_var, value='4').pack()

    tk.Label(root, text="Enter number of games for simulation (default 100):").pack()
    num_games_entry = tk.Entry(root)
    num_games_entry.pack()

    def on_start():
        grid_size = int(grid_size_entry.get()) + 1
        game_mode = game_mode_var.get()
        num_games = num_games_entry.get()
        if game_mode == '4':
            num_games = int(num_games) if num_games else 100  # Default to 100 games if not specified
            run_simulation(grid_size, num_games)
        else:
            start_game(grid_size, game_mode)

    start_button = tk.Button(root, text="Start Game", command=on_start)
    start_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
