import tkinter as tk
import random

class Minesweeper:
    def __init__(self, master, rows, cols, num_mines):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.cells = []
        self.game_over = False
        self.create_grid()
        self.place_mines()
        self.create_buttons()
        self.create_restart_button()
        
    def create_grid(self):
        for row in range(self.rows):
            self.cells.append([])
            for col in range(self.cols):
                self.cells[row].append(0)

    def place_mines(self):
        for _ in range(self.num_mines):
            row, col = random.randint(0, self.rows-1), random.randint(0, self.cols-1)
            while self.cells[row][col] == -1:
                row, col = random.randint(0, self.rows-1), random.randint(0, self.cols-1)
            self.cells[row][col] = -1

    def create_buttons(self):
        for row in range(self.rows):
            for col in range(self.cols):
                button = tk.Button(self.master, text='', width=2, command=lambda row=row, col=col: self.click(row, col))
                button.grid(row=row, column=col)
                button.bind('<Button-3>', lambda event, row=row, col=col: self.mark(row, col))

    def click(self, row, col):
        if self.cells[row][col] == -1:
            print("Game Over! You clicked on a mine.")
            self.game_over = True
            self.reveal_board()
            self.create_play_again_button()
        else:
            self.reveal(row, col)

    def mark(self, row, col):
        button = self.master.grid_slaves(row=row, column=col)[0]
        button.config(text='X')

    def reveal(self, row, col):
        pass  # Implement this to reveal cells around the clicked cell

    def reveal_board(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.cells[row][col] == -1:
                    button = self.master.grid_slaves(row=row, column=col)[0]
                    button.config(text='*')

    def restart_game(self):
        self.game_over = False
        self.master.destroy()
        root = tk.Tk()
        root.title("Minesweeper")
        game = Minesweeper(root, self.rows, self.cols, self.num_mines)
        root.mainloop()

    def create_restart_button(self):
        restart_button = tk.Button(self.master, text='Restart', command=self.restart_game)
        restart_button.grid(row=self.rows, columnspan=self.cols)

    def create_play_again_button(self):
        play_again_button = tk.Button(self.master, text='Play Again', command=self.restart_game)
        play_again_button.grid(row=self.rows, columnspan=self.cols)

def main():
    rows, cols, num_mines = 5, 5, 5
    root = tk.Tk()
    root.title("Minesweeper")
    game = Minesweeper(root, rows, cols, num_mines)
    root.mainloop()

if __name__ == "__main__":
    main()