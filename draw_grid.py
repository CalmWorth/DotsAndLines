#draw_grid.py

import tkinter as tk
from calculations import move_and_square_tracker

def draw_grid(canvas, sequence, player_scores, grid_size):
    cell_size = 40
    offset = 20  # Margin offset
    canvas_width = canvas.winfo_reqwidth()
    canvas_height = canvas.winfo_reqheight()
    
    # Calculate the center coordinates of the canvas
    center_x = canvas_width // 2
    center_y = canvas_height // 2

    # Calculate the top left corner of the grid
    grid_start_x = center_x - (cell_size * grid_size // 2)
    grid_start_y = center_y - (cell_size * grid_size // 2)

    grid, sqaure_list0, sqaure_list1, player_list = move_and_square_tracker(sequence, grid_size)
    turn = player_list[-1]
    
    canvas.delete("all")
    
    for row in range(grid_size):
        for col in range(grid_size):
            # x1 = offset + col * cell_size
            # y1 = offset + row * cell_size
            x1 = grid_start_x + col * cell_size
            y1 = grid_start_y + row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            if (row, col) in sqaure_list0:
                canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
            if (row, col) in sqaure_list1:
                canvas.create_rectangle(x1, y1, x2, y2, fill="red")

            # Draw horizontal link
            if grid[row][col][0] == 1:
                canvas.create_line(x1, y1, x2, y1, fill="black", width=2)
            elif grid[row][col][0] == 0:
                canvas.create_line(x1, y1, x2, y1, fill="grey", dash=(2, 2))

            # Draw vertical link
            if grid[row][col][1] == 1:
                canvas.create_line(x1, y1, x1, y2, fill="black", width=2)
            elif grid[row][col][1] == 0:
                canvas.create_line(x1, y1, x1, y2, fill="grey", dash=(2, 2))

            # Draw node as a small circle
            canvas.create_oval(x1-3, y1-3, x1+3, y1+3, fill="green")
    


    # Display whose turn it is at the top center
    canvas.create_text(center_x, 10, text=f"Player {turn+1}'s Turn", font=("Helvetica", 16))
    
    # Display player scores at the bottom corners
    canvas.create_text(100, canvas_height - 30, text=f"Player 1: {player_scores[0]} squares", font=("Helvetica", 12), fill="blue")
    canvas.create_text(canvas_width - 100, canvas_height - 30, text=f"Player 2: {player_scores[1]} squares", font=("Helvetica", 12), fill="red")
