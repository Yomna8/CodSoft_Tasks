import customtkinter as ctk
import random


class TicTacToe(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.initialize_window()
        self.reset_game()

    def initialize_window(self):
        """Setup the main game window properties."""
        self.title("TicTacToe")
        self.geometry("400x600")
        self.resizable(False, False)
        self.configure(bg="#282c34")

        self.title_label = ctk.CTkLabel(
            self, text="TicTacToe", font=("Verdana", 30, "bold"), text_color="#ffffff"
        )
        self.title_label.pack(pady=20)

        self.info_label = ctk.CTkLabel(
            self,
            text="Player's Turn",
            font=("Verdana", 18),
            text_color="#bfc9d1",
        )
        self.info_label.pack(pady=10)

        self.board_frame = ctk.CTkFrame(self, fg_color="#333842")
        self.board_frame.pack(pady=15)

        self.reset_button = ctk.CTkButton(
            self,
            text="Restart Game",
            font=("Verdana", 16),
            command=self.reset_game,
            fg_color="#007acc",
            hover_color="#005f99",
            text_color="#ffffff",
        )
        self.reset_button.pack(pady=10)

    def reset_game(self):
        """Reset the game to its initial state."""
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = []
        self.player_turn = True  # Player goes first
        self.info_label.configure(text="Player's Turn")
        self.setup_board()

    def setup_board(self):
        """Create the game board."""
        for widget in self.board_frame.winfo_children():
            widget.destroy()

        for row in range(3):
            button_row = []
            for col in range(3):
                button = ctk.CTkButton(
                    self.board_frame,
                    text="",
                    font=("Verdana", 24),
                    width=100,
                    height=100,
                    fg_color="#4f5a66",
                    hover_color="#5c6e7a",
                    text_color="#ffffff",
                    corner_radius=5,
                    command=lambda r=row, c=col: self.handle_turn(r, c),
                )
                button.grid(row=row, column=col, padx=5, pady=5)
                button_row.append(button)
            self.buttons.append(button_row)

    def handle_turn(self, row, col):
        """Handle a move on the board."""
        if self.board[row][col] == "" and self.player_turn:
            self.make_move(row, col, "X")
            if self.check_game_over("X"):
                return
            self.player_turn = False
            self.info_label.configure(text="AI's Turn")
            self.after(500, self.ai_move)

    def make_move(self, row, col, symbol):
        """Mark a cell on the board."""
        self.board[row][col] = symbol
        self.buttons[row][col].configure(text=symbol, state="disabled")

    def ai_move(self):
        """AI selects its move."""
        move = self.find_best_move()
        if move:
            self.make_move(move[0], move[1], "O")
        if not self.check_game_over("O"):
            self.player_turn = True
            self.info_label.configure(text="Player's Turn")

    def find_best_move(self):
        """Calculate AI's move."""
        empty_cells = [
            (r, c) for r in range(3) for c in range(3) if self.board[r][c] == ""
        ]
        # AI can use random moves for simplicity here
        return random.choice(empty_cells) if empty_cells else None

    def check_game_over(self, symbol):
        """Check if the game is won, lost, or drawn."""
        if self.is_winner(symbol):
            self.info_label.configure(text=f"{symbol} Wins!")
            self.disable_board()
            return True
        if self.is_draw():
            self.info_label.configure(text="It's a Draw!")
            self.disable_board()
            return True
        return False

    def is_winner(self, symbol):
        """Check if a specific player has won."""
        win_patterns = [
            [(0, 0), (0, 1), (0, 2)],  # Rows
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],  # Columns
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],  # Diagonals
            [(0, 2), (1, 1), (2, 0)],
        ]
        return any(all(self.board[r][c] == symbol for r, c in pattern) for pattern in win_patterns)

    def is_draw(self):
        """Check if the board is completely filled without a winner."""
        return all(self.board[r][c] != "" for r in range(3) for c in range(3))

    def disable_board(self):
        """Disable all buttons after the game ends."""
        for row in self.buttons:
            for button in row:
                button.configure(state="disabled")


if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")
    game = TicTacToe()
    game.mainloop()
